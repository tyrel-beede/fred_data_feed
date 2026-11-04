#!/usr/bin/env python3
"""Pull the physical-layer catalogs that are reachable by URL (runs in the GitHub Actions workflow, where the
network is open; the sandbox cannot reach these hosts). Each file lands under history/physical/raw/<id>/ with a
manifest recording the URL, size, SHA-256 and retrieval time. Nothing here transforms data; physical_build.py reads
the raw files.

  EI-OIL-PRICE-1861   Our World in Data grapher CSV of crude oil prices 1861- (Energy Institute / S&P Global Platts),
                      current US$ per cubic metre (1 m3 = 6.2898 barrels)
  CHAT                the NBER data appendix of Comin & Hobijn's CHAT dataset: every data file linked from the index
  EIA-TOTAL-ENERGY    EIA Total Energy API: annual US primary energy consumption by source 1949- (needs EIA_API_KEY)

Usage: python3 history/tools/physical_pull.py
"""
import hashlib, html, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "history", "physical", "raw")
UA = {"User-Agent": "fred_data_feed history layer (github.com/tyrel-beede/fred_data_feed)"}


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except Exception as e:  # noqa
            if i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def save(cat, name, data, url, manifest):
    d = os.path.join(RAW, cat); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name)
    with open(p, "wb") as f:
        f.write(data)
    manifest.append({"catalog": cat, "file": f"history/physical/raw/{cat}/{name}", "url": url, "bytes": len(data),
                     "sha256": hashlib.sha256(data).hexdigest(), "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    print(f"  {cat}/{name}: {len(data)} bytes")


def main():
    manifest = []
    errors = []
    # 1. oil prices since 1861 (OWID grapher CSV + metadata)
    try:
        base = "https://ourworldindata.org/grapher/crude-oil-prices"
        save("EI-OIL-PRICE-1861", "crude-oil-prices.csv", get(base + ".csv?v=1&csvType=full&useColumnShortNames=true"), base + ".csv", manifest)
        save("EI-OIL-PRICE-1861", "crude-oil-prices.metadata.json", get(base + ".metadata.json?v=1&csvType=full&useColumnShortNames=true"), base + ".metadata.json", manifest)
    except Exception as e:  # noqa
        errors.append(f"oil: {e}")
    # 2. CHAT: every data file linked from the NBER data-appendix index
    try:
        idx_url = "https://data.nber.org/data-appendix/w15319/"
        page = get(idx_url).decode("utf-8", "replace")
        links = sorted(set(html.unescape(m) for m in re.findall(r'href="([^"]+)"', page)))
        files = [l for l in links if re.search(r"\.(xls|xlsx|csv|dta|zip|txt|pdf|do|sas7bdat)$", l, re.I)]
        save("CHAT", "index.html", page.encode(), idx_url, manifest)
        for l in files:
            url = urllib.parse.urljoin(idx_url, l)
            name = os.path.basename(urllib.parse.urlparse(url).path)
            try:
                save("CHAT", name, get(url), url, manifest)
            except Exception as e:  # noqa
                errors.append(f"chat {name}: {e}")
            time.sleep(0.5)
    except Exception as e:  # noqa
        errors.append(f"chat index: {e}")
    # 3. EIA Total Energy: annual primary energy consumption by source, 1949- (TETCBUS = total; others by msn)
    key = os.environ.get("EIA_API_KEY", "").strip()
    if key:
        try:
            msns = ["TETCBUS", "CLTCBUS", "PATCBUS", "NNTCBUS", "NUETBUS", "RETCBUS", "ELTCBUS"]  # total, coal, petroleum, gas, nuclear, renewables, electricity
            rows = []
            for msn in msns:
                url = ("https://api.eia.gov/v2/total-energy/data/?" + urllib.parse.urlencode({
                    "api_key": key, "frequency": "annual", "data[0]": "value", "facets[msn][]": msn, "sort[0][column]": "period",
                    "sort[0][direction]": "asc", "length": 5000}))
                js = json.loads(get(url))
                for d in js.get("response", {}).get("data", []):
                    rows.append((msn, d.get("period"), d.get("value"), d.get("unit"), d.get("seriesDescription")))
                time.sleep(0.5)
            body = "msn,year,value,unit,description\n" + "\n".join(
                ",".join('"' + str(x).replace('"', "'") + '"' for x in r) for r in rows) + "\n"
            save("EIA-TOTAL-ENERGY", "us_primary_energy_annual.csv", body.encode(), "https://api.eia.gov/v2/total-energy/data/ (annual, by msn)", manifest)
        except Exception as e:  # noqa
            errors.append(f"eia: {e}")
    else:
        errors.append("eia: EIA_API_KEY not set")
    os.makedirs(RAW, exist_ok=True)
    out = {"manifest": manifest, "errors": errors}
    prev = os.path.join(RAW, "manifest.json")
    if os.path.exists(prev):
        try:
            old = json.load(open(prev)).get("manifest", [])
            seen = {m["file"] for m in manifest}
            out["manifest"] = manifest + [m for m in old if m["file"] not in seen]
        except Exception:  # noqa
            pass
    json.dump(out, open(prev, "w"), indent=1)
    print(json.dumps({"files": len(manifest), "errors": errors}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
