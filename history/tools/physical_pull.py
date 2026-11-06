#!/usr/bin/env python3
"""Pull the physical-layer catalogs that are reachable by URL (runs in the GitHub Actions workflow, where the
network is open; the sandbox cannot reach these hosts). Each file lands under history/physical/raw/<id>/ with a
manifest recording the URL, size, SHA-256 and retrieval time. Nothing here transforms data; physical_build.py reads
the raw files.

  EI-OIL-PRICE-1861   Our World in Data grapher CSV of crude oil prices 1861- (Energy Institute / S&P Global Platts),
                      current US$ per cubic metre (1 m3 = 6.2898 barrels)
  CHAT                the NBER data appendix of Comin & Hobijn's CHAT dataset: every data file linked from the index
  EIA-TOTAL-ENERGY    EIA Total Energy API: annual US primary energy consumption by source 1949- (needs EIA_API_KEY)
  EIA-HISTORICAL-1635 EIA's table of estimated US energy consumption by source for selected years 1635-1945: the notes
                      page (HTML) and the table itself (PDF); eia_hist_parse.py turns the PDF into a CSV
  JACKS-COMMODITIES   Jacks's real commodity prices 1850-present: the files linked from his data page
  KMW-EUROPE-ENERGY   European energy consumption by carrier 1800-2009 (Kander, Malanima, Warde et al.), the Mendeley
                      Data deposit by Rubio-Varas and Munoz-Delgado (CC BY 4.0)
  USGS-DS140          USGS Data Series 140, historical statistics for mineral and material commodities (US production,
                      consumption, unit value nominal and real, world production where given, since 1900): every
                      commodity workbook linked from the series index
  FRED-PHYSICAL       FRED long physical price series: PPIACO (all-commodity PPI, 1913-), WTISPLC (WTI spot, 1946-),
                      PCOPPUSDM (copper, 1990-) (needs FRED_API_KEY)

Usage: python3 history/tools/physical_pull.py [--only oil,chat,eia,eia_hist,jacks,kmw,usgs,fred] [--refresh-days 30]
  The slow annual catalogs (chat, eia_hist, kmw, usgs) are re-pulled only when their last retrieval in the manifest is
  older than --refresh-days. jacks is off unless named: the author's site has not answered the Actions runner (it
  times out on every run), so it is run from a desktop: python3 history/tools/physical_pull.py --only jacks
"""
import hashlib, html, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "history", "physical", "raw")
UA = {"User-Agent": "fred_data_feed history layer (github.com/tyrel-beede/fred_data_feed)"}


def get(url, tries=4, timeout=180):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
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


class Skip(Exception):
    pass


SLOW = {"chat": "CHAT", "eia_hist": "EIA-HISTORICAL-1635", "kmw": "KMW-EUROPE-ENERGY", "usgs": "USGS-DS140"}
OFF_BY_DEFAULT = {"jacks"}


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma list of pulls to run (default: all except jacks)")
    ap.add_argument("--refresh-days", type=int, default=30, help="re-pull the slow annual catalogs only when older than this")
    a = ap.parse_args()
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    last = {}
    prev_path = os.path.join(RAW, "manifest.json")
    if os.path.exists(prev_path):
        try:
            for m in json.load(open(prev_path)).get("manifest", []):
                last[m["catalog"]] = max(last.get(m["catalog"], ""), m.get("retrieved", ""))
        except Exception:  # noqa
            pass

    def want(name):
        if only:
            return name in only
        if name in OFF_BY_DEFAULT:
            return False
        if name in SLOW and last.get(SLOW[name]):
            age = (time.time() - time.mktime(time.strptime(last[SLOW[name]], "%Y-%m-%dT%H:%M:%SZ"))) / 86400.0
            if age < a.refresh_days:
                print(f"  {SLOW[name]}: retrieved {age:.0f} days ago, skipped (refresh after {a.refresh_days} days)")
                return False
        return True

    manifest = []
    errors = []
    skipped = []
    # 1. oil prices since 1861 (OWID grapher CSV + metadata)
    try:
        if not want("oil"):
            raise Skip()
        base = "https://ourworldindata.org/grapher/crude-oil-prices"
        save("EI-OIL-PRICE-1861", "crude-oil-prices.csv", get(base + ".csv?v=1&csvType=full&useColumnShortNames=true"), base + ".csv", manifest)
        save("EI-OIL-PRICE-1861", "crude-oil-prices.metadata.json", get(base + ".metadata.json?v=1&csvType=full&useColumnShortNames=true"), base + ".metadata.json", manifest)
    except Exception as e:  # noqa
        errors.append(f"oil: {e}") if not isinstance(e, Skip) else None
    # 2. CHAT: every data file linked from the NBER data-appendix index
    try:
        if not want("chat"):
            raise Skip()
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
        errors.append(f"chat index: {e}") if not isinstance(e, Skip) else None
    # 3. EIA Total Energy: annual primary energy consumption by source, 1949- (TETCBUS = total; others by msn)
    key = os.environ.get("EIA_API_KEY", "").strip()
    if not want("eia"):
        key = ""; skipped.append("eia")
    if key:
        try:
            msns = ["TETCBUS", "CLTCBUS", "PATCBUS", "NNTCBUS", "NUETBUS", "RETCBUS"]  # total, coal, petroleum, gas, nuclear, renewables (ELTCBUS is not a Total Energy msn: returned nothing)
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
    elif "eia" not in skipped:
        errors.append("eia: EIA_API_KEY not set")
    # 3b. EIA's estimated US energy consumption 1635-1945 by source (an HTML table on the Energy Explained site; no key)
    try:
        if not want("eia_hist"):
            raise Skip()
        url = "https://www.eia.gov/energyexplained/us-energy-facts/estimated-consumption-1635-1945.php"
        save("EIA-HISTORICAL-1635", "estimated-consumption-1635-1945.html", get(url), url, manifest)
        # the table itself is a PDF linked from that page (the page holds the coverage notes)
        url = "https://www.eia.gov/energyexplained/us-energy-facts/images/U.S._Primary_Energy_Consumption_1635-1945.pdf"
        save("EIA-HISTORICAL-1635", "U.S._Primary_Energy_Consumption_1635-1945.pdf", get(url), url, manifest)
    except Exception as e:  # noqa
        errors.append(f"eia historical table: {e}") if not isinstance(e, Skip) else None
    # 3c. Jacks, real commodity prices 1850-present ("freely provided to all comers"; cite Jacks 2019, Cliometrica):
    #     every spreadsheet, archive or PDF linked from the author's data page
    try:
        if not want("jacks"):
            raise Skip()
        idx_url = "https://www.sfu.ca/~djacks/data/boombust/index.html"
        page = get(idx_url, tries=2, timeout=60).decode("utf-8", "replace")  # the site has timed out from the runner; keep the cost low
        save("JACKS-COMMODITIES", "index.html", page.encode(), idx_url, manifest)
        links = sorted(set(html.unescape(m) for m in re.findall(r'href="([^"]+)"', page)))
        files = [l for l in links if re.search(r"\.(xlsx?|csv|zip|pdf|dta)$", l, re.I)]
        if not files:
            errors.append("jacks: no data links found on the page")
        for l in files:
            url = urllib.parse.urljoin(idx_url, l)
            name = os.path.basename(urllib.parse.urlparse(url).path)
            try:
                save("JACKS-COMMODITIES", name, get(url), url, manifest)
            except Exception as e:  # noqa
                errors.append(f"jacks {name}: {e}")
            time.sleep(0.5)
    except Exception as e:  # noqa
        errors.append(f"jacks index: {e}") if not isinstance(e, Skip) else None
    # 3d. European energy consumption by carrier 1800-2009 (Kander, Malanima, Warde and the national compilers), as
    #     deposited by Rubio-Varas and Munoz-Delgado on Mendeley Data under CC BY 4.0 (doi 10.17632/dx7fwfj28g.2)
    try:
        if not want("kmw"):
            raise Skip()
        ds, ver = "dx7fwfj28g", "2"
        api = f"https://data.mendeley.com/public-api/datasets/{ds}/files?folder_id=root&version={ver}"
        got = 0
        try:
            js = json.loads(get(api))
            for fobj in js if isinstance(js, list) else js.get("files", []):
                name = fobj.get("filename") or fobj.get("name")
                furl = (fobj.get("content_details") or {}).get("download_url") or fobj.get("download_url")
                if name and furl:
                    save("KMW-EUROPE-ENERGY", name, get(furl), furl, manifest); got += 1; time.sleep(0.5)
        except Exception as e:  # noqa
            errors.append(f"kmw api: {e}")
        if not got:  # fall back to the dataset page's own file links
            page_url = f"https://data.mendeley.com/datasets/{ds}/{ver}"
            page = get(page_url).decode("utf-8", "replace")
            save("KMW-EUROPE-ENERGY", "dataset_page.html", page.encode(), page_url, manifest)
            for furl in sorted(set(re.findall(r'https://data\.mendeley\.com/public-files/datasets/[^"\s]+file_downloaded', page))):
                name = re.sub(r"[^A-Za-z0-9_.-]", "_", furl.split("/files/")[-1].split("/")[0]) + ".bin"
                try:
                    save("KMW-EUROPE-ENERGY", name, get(furl), furl, manifest); got += 1
                except Exception as e:  # noqa
                    errors.append(f"kmw file: {e}")
            if not got:
                errors.append("kmw: no files retrieved (download from the Mendeley page and add them under history/physical/raw/KMW-EUROPE-ENERGY/)")
    except Exception as e:  # noqa
        errors.append(f"kmw: {e}") if not isinstance(e, Skip) else None
    # 4. USGS DS140: index page -> commodity pages -> workbook links (S3)
    try:
        if not want("usgs"):
            raise Skip()
        idx = "https://www.usgs.gov/centers/national-minerals-information-center/historical-statistics-mineral-and-material-commodities"
        page = get(idx).decode("utf-8", "replace")
        pages = sorted(set(re.findall(r'href="(/media/files/[^"]*historical-statistics-data-series-140[^"]*)"', page)))
        save("USGS-DS140", "index.html", page.encode(), idx, manifest)
        n = 0
        for rel_ in pages[:120]:
            url = "https://www.usgs.gov" + rel_
            try:
                sub = get(url).decode("utf-8", "replace")
                m = re.search(r'href="(https://[^"]+\.xlsx?)"', sub)
                if not m:
                    errors.append(f"usgs {rel_}: no workbook link"); continue
                furl = html.unescape(m.group(1))
                name = os.path.basename(urllib.parse.urlparse(furl).path)
                save("USGS-DS140", name, get(furl), furl, manifest); n += 1
            except Exception as e:  # noqa
                errors.append(f"usgs {rel_}: {e}")
            time.sleep(0.7)
        print(f"  USGS-DS140: {n} workbooks")
    except Exception as e:  # noqa
        errors.append(f"usgs index: {e}") if not isinstance(e, Skip) else None
    # 5. FRED long physical price series
    fkey = os.environ.get("FRED_API_KEY", "").strip()
    if not want("fred"):
        fkey = ""; skipped.append("fred")
    if fkey:
        for sid in ("PPIACO", "WTISPLC", "PCOPPUSDM", "PIORECRUSDM"):
            try:
                url = ("https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(
                    {"series_id": sid, "api_key": fkey, "file_type": "json", "observation_start": "1900-01-01"}))
                obs = json.loads(get(url))["observations"]
                body = "date,value\n" + "\n".join(f"{o['date']},{o['value']}" for o in obs if o["value"] not in (".", "")) + "\n"
                save("FRED-PHYSICAL", f"{sid}.csv", body.encode(), f"FRED {sid}", manifest)
                time.sleep(0.3)
            except Exception as e:  # noqa
                errors.append(f"fred {sid}: {e}")
    elif "fred" not in skipped:
        errors.append("fred: FRED_API_KEY not set")
    os.makedirs(RAW, exist_ok=True)
    out = {"manifest": manifest, "errors": errors, "pulls_run": sorted(only) if only else "all except jacks (slow catalogs on a %d-day refresh)" % a.refresh_days}
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
