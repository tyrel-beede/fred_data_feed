#!/usr/bin/env python3
"""Quality-control checks for history/. Writes history/QC.md with PASS/FAIL per check and the evidence.

Run from the repo root: python3 -I history/tools/qc.py
Every check is mechanical and re-runnable; the review of content against the source documents is a separate,
human-or-agent pass recorded in QC.md's second section.
"""
import csv, json, os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
H = os.path.join(ROOT, "history")
sys.path.insert(0, os.path.join(H, "tools"))
from jstlib import load_jst, load_overrides, load_features  # noqa: E402

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    return ok


def rel(p):
    return os.path.relpath(p, ROOT)


# ------------------------------------------------------------------ 1. inventory
expected = [
    "history/README.md", "history/sources.json", "history/QC.md",
    "history/jst/JSTdatasetR6.xlsx", "history/jst/jst_r6.csv", "history/jst/LICENSE-JST.md", "history/jst/overrides.csv",
    "history/jst/data_dictionary.md", "history/jst/data_dictionary.json", "history/jst/crises_chronology.csv",
    "history/jst/crises_chronology_notes.md", "history/jst/crises_indicator.csv", "history/jst/returns_documentation.md",
    "history/jst/returns_variables.json", "history/jst/house_prices_documentation.md", "history/jst/coverage.csv",
    "history/jst/units.csv", "history/jst/features.csv", "history/jst/field_map.csv",
    "history/dalio/hcgb_template.json", "history/dalio/hcgb_indicators.csv", "history/dalio/hcgb_timeline.csv",
    "history/dalio/hcgb/part1.md", "history/dalio/hcgb/part2.md", "history/dalio/hcgb/part3.md", "history/dalio/hcgb/part4.md",
    "history/dalio/bdc_template.json", "history/dalio/bdc_cases.csv", "history/dalio/bdc_cases_schema.md",
    "history/dalio/bdc_cases_part2a.json", "history/dalio/bdc_case_us2007.json",
    "history/dalio/bdc/part1_template.md", "history/dalio/bdc/part2a_germany_us1930s.md", "history/dalio/bdc/part2b_us2007.md",
    "history/dalio/bdc/part3a_compendium.md", "history/dalio/bdc/part3b_compendium.md",
    "history/dalio/cwo_gauges.json", "history/dalio/cwo_charts_catalogue.md",
    "history/dalio/principles_mechanisms.json", "history/dalio/principles_2011.md", "history/dalio/principles_2017.md",
    "history/dalio/reads.csv",
    "history/tools/jst_build.py", "history/tools/bridge_pull.py", "history/tools/assemble.py", "history/tools/jstlib.py",
    "history/tools/analogs.py", "history/tools/qc.py", "history/tools/features2.py", "history/tools/wf.py",
    "history/tools/analog_test2.py", "history/tools/label_test.py", "history/jst/features2.csv",
    "history/analogs/test2.md", "history/analogs/label_test.md", "history/tools/lag_test.py", "history/analogs/lag_test.md",
    "history/tools/learner_test.py", "history/analogs/learner_test.md",
    "history/tools/physical_build.py", "history/physical/owid_extract.csv", "history/physical/physical_features.csv",
    "history/physical/catalog.json", "history/physical/README.md", "history/analogs/learner_test_physical.md",
]
missing = [p for p in expected if not os.path.exists(os.path.join(ROOT, p)) and not p.endswith("QC.md")]
check("inventory: every expected file exists", not missing, f"missing: {missing}" if missing else f"{len(expected)} files")

# ------------------------------------------------------------------ 2. parse everything
bad = []
for dp, _, fns in os.walk(H):
    for fn in fns:
        p = os.path.join(dp, fn)
        try:
            if fn.endswith(".json"):
                json.load(open(p))
            elif fn.endswith(".csv"):
                rows = list(csv.reader(open(p)))
                widths = {len(r) for r in rows}
                if len(widths) != 1:
                    bad.append((rel(p), f"ragged rows: widths {sorted(widths)[:5]}"))
        except Exception as e:  # noqa
            bad.append((rel(p), str(e)[:80]))
check("parse: every JSON parses and every CSV is rectangular", not bad, str(bad) if bad else "ok")

# ------------------------------------------------------------------ 3. the sheet
jst = load_jst(apply_overrides=False)
isos = sorted({r["iso"] for r in jst})
keys = {(r["iso"], r["year"]) for r in jst}
check("jst_r6: 2,718 rows, 18 countries x 1870-2020, no duplicate country-year",
      len(jst) == 2718 and len(isos) == 18 and len(keys) == 2718 and all(1870 <= r["year"] <= 2020 for r in jst),
      f"rows {len(jst)}, countries {len(isos)}")
cols = [c for c in jst[0].keys() if c != "overrides"]
check("jst_r6: 59 columns", len(cols) == 59, f"{len(cols)} columns")

# ------------------------------------------------------------------ 4. dictionary coverage
dd = json.load(open(os.path.join(H, "jst", "data_dictionary.json")))
names = {v.get("name") for v in dd["variables"]}
uncovered = [c for c in cols if c not in names]
check("data dictionary: every column has an entry", not uncovered, f"uncovered: {uncovered}" if uncovered else f"{len(dd['variables'])} entries")
check("data dictionary: terms of use and citation transcribed",
      dd.get("terms_of_use") and "Attribution-NonCommercial-ShareAlike" in dd["terms_of_use"] and dd.get("citation"), "")

# ------------------------------------------------------------------ 5. crises
chron = {(r["iso"], int(r["year"])) for r in csv.DictReader(open(os.path.join(H, "jst", "crises_chronology.csv")))}
flags = {(r["iso"], r["year"]) for r in jst if r["crisisJST"] == 1}
check("crises: chronology episodes equal crisisJST flags", chron == flags,
      f"chronology {len(chron)}, flags {len(flags)}, diff {sorted(chron ^ flags)}")
old = {(r["iso"], r["year"]) for r in jst if r["crisisJST_old"] == 1}
check("crises: the seven BVX recodings appear in crisisJST_old vs crisisJST",
      {("BEL", 1876), ("JPN", 1901)} <= (flags - old) and
      {("DEU", 1907), ("DNK", 1931), ("NLD", 1893), ("NLD", 1907), ("NLD", 1939)} <= (old - flags),
      f"added {sorted(flags - old)}, removed {sorted(old - flags)}")

# ------------------------------------------------------------------ 6. overrides
ov = load_overrides()
by = {(r["iso"], r["year"]): r for r in jst}
probs = []
for o in ov:
    r = by.get((o["iso"], int(o["year"])))
    if r is None or o["variable"] not in r:
        probs.append(f"{o['iso']} {o['year']} {o['variable']}: no such cell")
        continue
    jv = r[o["variable"]]
    if o["jst_value"] not in ("", None) and abs(float(o["jst_value"]) - (jv or 0)) > 1e-6 * max(1, abs(jv or 0)):
        probs.append(f"{o['iso']} {o['year']} {o['variable']}: jst_value {o['jst_value']} != sheet {jv}")
    if o["action"] == "replace" and not o["override_value"]:
        probs.append(f"{o['iso']} {o['year']} {o['variable']}: replace without value")
    if not o["source"] or not o["observed_time"] or not o["node"]:
        probs.append(f"{o['iso']} {o['year']} {o['variable']}: provenance incomplete")
check("overrides: every row points at a real cell, quotes the JST value correctly, and carries provenance", not probs, str(probs) if probs else f"{len(ov)} rows")

# ------------------------------------------------------------------ 7. features recomputed independently
feat = {(r["iso"], r["year"]): r for r in load_features()}
jo = {(r["iso"], r["year"]): r for r in load_jst(apply_overrides=True)}
random.seed(7)
sample = random.sample([k for k in feat if k[1] >= 1880], 40) + [("USA", 2007), ("USA", 2019), ("GBR", 2019), ("JPN", 1991)]
errs = []


def close(a, b, tol=1e-4):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


for iso, y in sample:
    f, r, r1, r5 = feat[(iso, y)], jo[(iso, y)], jo.get((iso, y - 1)), jo.get((iso, y - 5))
    lg = (r["tloans"] / r["gdp"]) if r.get("tloans") is not None and r.get("gdp") else None
    if not close(f["loans_gdp"], lg):
        errs.append((iso, y, "loans_gdp", f["loans_gdp"], lg))
    if r5 and r5.get("tloans") is not None and r5.get("gdp") and lg is not None:
        d5 = lg - r5["tloans"] / r5["gdp"]
        if not close(f["d5_loans_gdp"], d5):
            errs.append((iso, y, "d5_loans_gdp", f["d5_loans_gdp"], d5))
    if r1 and r.get("gdp") and r1.get("gdp") and r.get("ltrate") is not None:
        rmg = r["ltrate"] - 100 * (r["gdp"] / r1["gdp"] - 1)
        if not close(f["r_minus_g"], rmg):
            errs.append((iso, y, "r_minus_g", f["r_minus_g"], rmg))
    if r.get("unemp") is not None and not close(f["unemp"], r["unemp"]):
        errs.append((iso, y, "unemp", f["unemp"], r["unemp"]))
    nxt = [jo.get((iso, y + k), {}).get("crisisJST") for k in (1, 2, 3)]
    lab = None if any(v is None for v in nxt) else (1.0 if any(v == 1 for v in nxt) else 0.0)
    if not close(f["crisis_next_1_3y"], lab):
        errs.append((iso, y, "crisis_next_1_3y", f["crisis_next_1_3y"], lab))
check("features: 44 country-years recomputed independently (loans/GDP, 5y change, r-g, unemp, crisis label)", not errs,
      str(errs[:5]) if errs else "all match")
check("features: overrides applied and flagged, with propagation to dependent rows",
      feat[("USA", 2019)]["unemp"] == 3.7 and feat[("USA", 2019)]["overrides"] == "unemp@2019"
      and feat[("USA", 2020)]["overrides"] == "unemp@2019" and feat[("GBR", 2019)]["overrides"] == "stir@2019"
      and "stir@2019" in feat[("GBR", 2021)]["overrides"] if ("GBR", 2021) in feat else True, "")

# ------------------------------------------------------------------ 8. field map tokens
fm = list(csv.DictReader(open(os.path.join(H, "jst", "field_map.csv"))))
known = set(cols) | set(feat[("USA", 2007)].keys()) | {"none"}
unknown = []
for r in fm:
    for tok in r["jst_proxy"].replace("/", " ").replace(";", " ").replace("(", " ").replace(")", " ").replace(",", " ").split():
        if tok.islower() and "_" in tok and tok not in known:
            unknown.append((r["dials_field"], tok))
check("field map: every variable-looking token names a real column or feature", not unknown, str(unknown) if unknown else f"{len(fm)} rows")

# ------------------------------------------------------------------ 9. sources
src = json.load(open(os.path.join(H, "sources.json")))
miss = [(s["id"], p) for s in src["sources"] for p in s.get("local_files", []) if not os.path.exists(os.path.join(ROOT, p))]
check("sources.json: every local_files path exists", not miss, str(miss) if miss else f"{len(src['sources'])} sources")

# ------------------------------------------------------------------ 10. Dalio structures
t = json.load(open(os.path.join(H, "dalio", "hcgb_template.json")))
check("HCGB: nine numbered stages with names and gauges", len(t["stages"]) == 9 and all(s.get("name") and s.get("indicators") for s in t["stages"]),
      "; ".join(f"{s['number']} {s['name'][:40]}" for s in t["stages"]))
check("HCGB: five forces of the Big Cycle recorded", t.get("big_cycle") and len(t["big_cycle"].get("forces", [])) >= 5,
      str(t["big_cycle"].get("forces"))[:200] if t.get("big_cycle") else "none")
reads = list(csv.DictReader(open(os.path.join(H, "dalio", "reads.csv"))))
rp = [r["id"] for r in reads if not r["claim"] or not r["event_time_as_of"] or r["falsifiable"] not in ("True", "False", "")]
RANGE = {"DALIO-HCGB-2025": (1, 390), "DALIO-BDC-2018": (1, 190)}  # book pages; BDC Part 2 printed pages
pages_bad = [r["id"] for r in reads if r["book_page"] and (not str(r["book_page"]).isdigit()
             or not (RANGE[r["source"]][0] <= int(r["book_page"]) <= RANGE[r["source"]][1]))]
conv_bad = [r["id"] for r in reads if not r.get("page_convention") or r.get("falsifiability_grade") not in ("strict", "loose", "conditional", "no", "author-scored")]
check("reads ledger: every row has a claim and an as-of date; falsifiable flag well-formed; pages in each source's range; page convention and grade present",
      not rp and not pages_bad and not conv_bad, f"{len(reads)} reads; bad {rp[:5]} {pages_bad[:5]} {conv_bad[:5]}")
cases = list(csv.DictReader(open(os.path.join(H, "dalio", "bdc_cases.csv"))))
cn = [c["case_name"] for c in cases]
cyr = [c for c in cases if not (c["start_year"].isdigit() and c["end_year"].isdigit() and int(c["start_year"]) <= int(c["end_year"]))]
check("BDC compendium: 48 unique cases with ordered years and 3-letter codes",
      len(cases) == 48 and len(set(cn)) == 48 and not cyr and all(len(c["iso3"]) == 3 for c in cases), f"{len(cases)} cases")
b = json.load(open(os.path.join(H, "dalio", "bdc_template.json")))
check("BDC template: 7 deflationary and 5-6 inflationary phases, bubble checklist of 7",
      len(b["deflationary_phases"]) == 7 and 5 <= len(b["inflationary_phases"]) <= 6 and len(b["bubble_checklist"]) >= 7,
      f"defl {len(b['deflationary_phases'])}, infl {len(b['inflationary_phases'])}, checklist {len(b['bubble_checklist'])}")
cw = json.load(open(os.path.join(H, "dalio", "cwo_gauges.json")))
g = cw.get("gauges", {})
check("CWO: 8 measures of power and 18 determinants recorded",
      len(g.get("measures_of_power", [])) == 8 and len(g.get("determinants", [])) >= 18,
      f"measures {len(g.get('measures_of_power', []))}, determinants {len(g.get('determinants', []))}")
pm = json.load(open(os.path.join(H, "dalio", "principles_mechanisms.json")))
check("Principles: mechanisms and ledger mapping present from both editions",
      {m["edition"] for m in pm["mechanisms"]} == {"2011", "2017"} and len(pm["mapping"]) > 10,
      f"{len(pm['mechanisms'])} mechanisms, {len(pm['mapping'])} mappings")

# ------------------------------------------------------------------ 11. units sanity
units = {r["iso"]: float(r["to_billions_multiplier"]) for r in csv.DictReader(open(os.path.join(H, "jst", "units.csv")))}
wb = {"AUS": 1.39, "BEL": 0.535, "CAN": 1.74, "CHE": 0.73, "DEU": 3.89, "DNK": 0.347, "ESP": 1.39, "FIN": 0.268, "FRA": 2.73,
      "GBR": 2.86, "IRL": 0.40, "ITA": 2.01, "JPN": 5.12, "NLD": 0.91, "NOR": 0.405, "PRT": 0.24, "SWE": 0.53, "USA": 21.4}
off = []
for iso in isos:
    r = by[(iso, 2019)]
    usd_tn = r["gdp"] * units[iso] / r["xrusd"] / 1000
    if abs(usd_tn / wb[iso] - 1) > 0.10:
        off.append((iso, round(usd_tn, 2), wb[iso]))
check("units: 2019 GDP in USD within 10% of World Bank for all 18 countries", not off, str(off) if off else "ok")

# ------------------------------------------------------------------ 12. workflow and license
wf = open(os.path.join(ROOT, ".github", "workflows", "pull.yml")).read()
check("workflow: bridge step wired and the bridge script exists", "history/tools/bridge_pull.py" in wf and "history/bridge" in wf, "")
lic = " ".join(open(os.path.join(H, "jst", "LICENSE-JST.md")).read().replace("\n>", "\n").split())
check("license: CC BY-NC-SA 4.0 and both required citations stated", "CC BY-NC-SA 4.0" in lic and "Macrofinancial History" in lic and "Rate of Return on Everything" in lic, "")
readme = open(os.path.join(H, "README.md")).read()
check("README: documents overrides, provenance classes, bitemporal fields", "overrides" in readme and "observed time" in readme and "provenance class" in readme, "")

# ------------------------------------------------------------------ report
n_ok = sum(1 for _, ok, _ in results if ok)
lines = ["# history/ — quality control", "",
         f"Mechanical checks run by `tools/qc.py`: **{n_ok} of {len(results)} pass**. Re-run after any change.", "",
         "| check | result | evidence |", "|---|---|---|"]
for name, ok, detail in results:
    lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail.replace('|', '/')[:220]} |")
lines += ["", "## Content review", "",
          "The content review (encodings against the source documents, design intent against the layout) is kept by hand in "
          "`QC_review.md` and included here verbatim; this script never edits it.", ""]
rev_path = os.path.join(H, "QC_review.md")
if os.path.exists(rev_path):
    lines.append(open(rev_path).read())
qc_path = os.path.join(H, "QC.md")
with open(qc_path, "w") as f:
    f.write("\n".join(lines))
print("\n".join(f"{'PASS' if ok else 'FAIL'}  {name}  {detail[:100]}" for name, ok, detail in results))
print(f"\n{n_ok}/{len(results)} pass -> {rel(qc_path)}")
sys.exit(0 if n_ok == len(results) else 1)
