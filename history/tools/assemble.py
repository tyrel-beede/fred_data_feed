#!/usr/bin/env python3
"""Assemble history/ from the readers' extraction files.

Usage: python3 -I history/tools/assemble.py <extraction_dir>

The extraction directory holds the structured outputs produced by reading the source documents page by page
(our own words, page-cited; no source text reproduced). This script merges them into the repository layout:

  history/jst/data_dictionary.md|json       JST R6 documentation (variables, sources, breaks, terms of use)
  history/jst/crises_chronology.csv|_notes.md  the JST crisis chronology as a dated event table
  history/jst/returns_documentation.md, returns_variables.json   Rate of Return on Everything + 2016-2020 update
  history/jst/house_prices_documentation.md No Price Like Home appendix (house price construction)
  history/dalio/hcgb/*.md, hcgb_template.json, hcgb_reads.csv, hcgb_timeline.csv, hcgb_indicators.csv
  history/dalio/bdc/*.md, bdc_template.json, bdc_cases.csv, bdc_reads.csv
  history/dalio/cwo_gauges.json, cwo_charts_catalogue.md
  history/dalio/principles_mechanisms.json, principles_2011.md, principles_2017.md
  history/dalio/reads.csv                   every dated read by the voice, one ledger (provenance: stated; node: Dalio)

Missing inputs are skipped with a note so the script can run while readers are still working.
"""
import csv, json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
H = os.path.join(ROOT, "history")
SRC = sys.argv[1] if len(sys.argv) > 1 else "."


def have(name):
    p = os.path.join(SRC, name)
    if os.path.exists(p):
        return p
    print(f"  (missing) {name}")
    return None


def load_json(name):
    p = have(name)
    return json.load(open(p)) if p else None


def copy_md(name, dst, header=None):
    p = have(name)
    if not p:
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    body = open(p).read()
    with open(dst, "w") as f:
        if header:
            f.write(header + "\n\n")
        f.write(body)


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def cell(v):
    if v is None:
        return ""
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    return v


ENC = ("<!-- Encoding written from the source document in our own words with page citations; the source text is not "
       "reproduced. Provenance class: stated (a voice's template and reads). See history/sources.json. -->")

# ----------------------------------------------------------------------------------------------------- JST
print("JST")
jd = os.path.join(H, "jst")
p1, p2 = load_json("jst_doc_part1.json"), load_json("jst_doc_part2.json")
if p1 or p2:
    merged = {"variables": [], "countries": {}, "references": [], "terms_of_use": None, "citation": None, "release": None}
    byname = {}
    for p in (p1, p2):
        if not p:
            continue
        for v in p.get("variables", []):
            key = v.get("name") or ("component:" + (v.get("label") or ""))
            if key in byname:  # same column documented in both halves (different countries): merge the source lists
                m = byname[key]
                m["sources"] = (m.get("sources") or []) + (v.get("sources") or [])
                m["pages"] = sorted(set((m.get("pages") or []) + (v.get("pages") or [])))
                for f in ("definition", "construction", "caveats", "units"):
                    if v.get(f) and v[f] != m.get(f):
                        m[f] = (m.get(f) or "") + (" | " if m.get(f) else "") + v[f]
            else:
                byname[key] = dict(v)
        merged["countries"].update(p.get("countries", {}))
        merged["references"] += p.get("references", [])
        for k in ("terms_of_use", "citation", "release"):
            if p.get(k) and not merged[k]:
                merged[k] = p[k]
    merged["variables"] = list(byname.values())
    merged["references"] = sorted(set(r if isinstance(r, str) else json.dumps(r, ensure_ascii=False) for r in merged["references"]))
    json.dump(merged, open(os.path.join(jd, "data_dictionary.json"), "w"), indent=1, ensure_ascii=False)
parts = [have("jst_doc_part1.md"), have("jst_doc_part2.md")]
if any(parts):
    with open(os.path.join(jd, "data_dictionary.md"), "w") as f:
        f.write("# JST Macrohistory Database R6 — documentation, as encoded for this repository\n\n"
                "<!-- Written from the R6 documentation PDF in our own words; source citations and the terms of use are "
                "transcribed verbatim because they are references. -->\n\n")
        for p in parts:
            if p:
                f.write(open(p).read() + "\n\n")
copy_md("jst_crises_notes.md", os.path.join(jd, "crises_chronology_notes.md"))
if have("jst_crises.csv"):
    shutil.copy(os.path.join(SRC, "jst_crises.csv"), os.path.join(jd, "crises_chronology.csv"))
copy_md("rore.md", os.path.join(jd, "returns_documentation.md"))
rv = load_json("rore_vars.json")
if rv:
    json.dump(rv, open(os.path.join(jd, "returns_variables.json"), "w"), indent=1, ensure_ascii=False)
np_ = [have("nplh_part1.md"), have("nplh_part2.md")]
if any(np_):
    with open(os.path.join(jd, "house_prices_documentation.md"), "w") as f:
        f.write("# No Price Like Home — online appendix, as encoded for this repository\n\n")
        for p in np_:
            if p:
                f.write(open(p).read() + "\n\n")

# ----------------------------------------------------------------------------------------------------- Dalio: HCGB
print("HCGB")
dd = os.path.join(H, "dalio")
os.makedirs(os.path.join(dd, "hcgb"), exist_ok=True)
hc = [load_json(f"hcgb_part{i}.json") for i in (1, 2, 3, 4)]
for i in (1, 2, 3, 4):
    copy_md(f"hcgb_part{i}.md", os.path.join(dd, "hcgb", f"part{i}.md"), ENC)
all_reads = []  # (source_id, part, read dict)
if any(hc):
    t = {"source": "DALIO-HCGB-2025", "page_convention": "book pages (PDF page = book page + 10)",
         "concepts": [], "mechanisms": [], "equations": [], "indicators": [], "stages": [], "big_cycle": None,
         "monetary_regimes": [], "cases": [], "japan_numbers": None, "solution": None, "scenarios": [],
         "principles": [], "non_red_dot_rules": []}
    for i, p in enumerate(hc, 1):
        if not p:
            continue
        for k in ("concepts", "mechanisms", "equations", "stages", "monetary_regimes", "cases", "scenarios",
                  "non_red_dot_rules"):
            for item in p.get(k, []) or []:
                item = dict(item); item["part"] = i
                t[k].append(item)
        for item in p.get("indicators", []) or []:
            item = dict(item); item["part"] = i
            t["indicators"].append(item)
        for item in p.get("principles", []) or []:
            item = dict(item); item["part"] = i
            t["principles"].append(item)
        for k in ("big_cycle", "japan_numbers", "solution"):
            if p.get(k):
                t[k] = p[k]
        for r in p.get("reads", []) or []:
            all_reads.append(("DALIO-HCGB-2025", f"part{i}", r))
    json.dump(t, open(os.path.join(dd, "hcgb_template.json"), "w"), indent=1, ensure_ascii=False)
    # indicators flat
    rows = [[x.get("part"), x.get("name"), x.get("measures"), x.get("reading"), x.get("as_of"),
             x.get("threshold_or_range") or x.get("scale_or_threshold"), cell(x.get("rankings")), x.get("page")]
            for x in t["indicators"]]
    write_csv(os.path.join(dd, "hcgb_indicators.csv"),
              ["part", "indicator", "measures", "reading", "as_of", "scale_or_threshold", "rankings_json", "book_page"], rows)
    # timeline
    tl = (hc[2] or {}).get("timeline", [])
    write_csv(os.path.join(dd, "hcgb_timeline.csv"), ["date", "country", "event", "stage", "numbers", "book_page"],
              [[x.get("date"), x.get("country"), x.get("event"), x.get("stage"), cell(x.get("numbers")), x.get("page")] for x in tl])

# ----------------------------------------------------------------------------------------------------- Dalio: BDC
print("BDC")
os.makedirs(os.path.join(dd, "bdc"), exist_ok=True)
for name, dst in (("bdc_part1.md", "part1_template.md"), ("bdc_part2a.md", "part2a_germany_us1930s.md"),
                  ("bdc_part2b.md", "part2b_us2007.md"), ("bdc_part3a.md", "part3a_compendium.md"),
                  ("bdc_part3b.md", "part3b_compendium.md")):
    copy_md(name, os.path.join(dd, "bdc", dst), ENC)
b1 = load_json("bdc_part1.json")
if b1:
    b1["source"] = "DALIO-BDC-2018"
    json.dump(b1, open(os.path.join(dd, "bdc_template.json"), "w"), indent=1, ensure_ascii=False)
# compendium cases: the two halves were encoded with different column names for the same template slots;
# the second half's names are mapped onto the first half's where the slot is the same statistic.
B_TO_A = {
    "debt_gdp_precrisis_peak_pct": "debt_gdp_peak_pct",
    "fx_debt_gdp_pct": "fx_debt_pct_gdp",
    "investment_inflows_avg_gdp_pct": "capital_inflows_bubble_pct_gdp",
    "current_account_deficit_gdp_pct": "current_account_bubble_pct_gdp",
    "bubble_real_growth_pct": "real_growth_bubble_pct",
    "gdp_gap_peak_pct": "gdp_gap_peak_bubble_pct",
    "bubble_equity_return_ann_pct": "equity_return_bubble_ann_pct",
    "real_fx_peak_pct": "real_fx_peak_bubble_pct",
    "debt_service_precrisis_peak_gdp_pct": "debt_service_peak_pct_gdp",
    "shock_trigger": "shock",
    "capital_inflows_fall_gdp_pct": "capital_inflow_fall_depression_pct_gdp",
    "equity_decline_pct": "equity_drawdown_pct",
    "unemployment_change_pp": "unemployment_increase_depression_pct",
    "peak_fiscal_deficit_gdp_pct": "peak_fiscal_deficit_ugly_period_pct_gdp",
    "imf_program": "imf_program_yes_no",
    "years_to_regain_gdp_peak": "years_to_regain_real_gdp_peak",
    "deleveraging_driver": "debt_reduction_drivers_reflation",
    "ugly_phase_vs_average": "bust_length_vs_average",
}
ca, cb = have("bdc_cases_a.csv"), have("bdc_cases_b.csv")
if ca or cb:
    rows, cols = [], ["compendium_half"]
    for half, p in (("A domestic-currency (PDF 259-362)", ca), ("B non-domestic-currency (PDF 363-480)", cb)):
        if not p:
            continue
        for r in csv.DictReader(open(p)):
            r = {B_TO_A.get(k, k): v for k, v in r.items()}
            r["compendium_half"] = half
            for c in r:
                if c not in cols:
                    cols.append(c)
            rows.append(r)
    write_csv(os.path.join(dd, "bdc_cases.csv"), cols, [[r.get(c, "") for c in cols] for r in rows])
    with open(os.path.join(dd, "bdc_cases_schema.md"), "w") as f:
        f.write("# bdc_cases.csv schema note\n\nThe 2018 free edition has no statistics table; each case is a fixed-template "
                "auto-summary whose numbers sit in sentence slots. Columns are named after those slots. The two halves of the "
                "compendium were encoded separately; the second half's column names were mapped onto the first half's where "
                "the slot is the same statistic:\n\n")
        for k, v in B_TO_A.items():
            f.write(f"- `{k}` -> `{v}`\n")
        f.write("\nColumns that exist in only one half are kept as encoded (units can differ between halves for rate changes: "
                "`short_rate_rise_depression` vs `short_rate_hike_pct`; `inflation_peak_pct` vs `inflation_peak_depression_pct`). "
                "Blank cells mean the book gives no number for that slot. Provenance: DALIO-BDC-2018, Bridgewater-derived "
                "statistics; see history/sources.json.\n")
b2b = load_json("bdc_part2b.json")
if b2b:
    case = b2b.get("case", b2b)
    for r in case.get("reads", []) or []:
        all_reads.append(("DALIO-BDC-2018", "part2b daily observations",
                          {"claim": r.get("claim"), "as_of": r.get("date"), "horizon": "", "falsifiable": "",
                           "criterion": "", "outcome_per_author": r.get("outcome_per_author"), "page": r.get("page")}))
b2a = load_json("bdc_part2a.json")
if b2a:
    json.dump(b2a, open(os.path.join(dd, "bdc_cases_part2a.json"), "w"), indent=1, ensure_ascii=False)
if b2b:
    json.dump(b2b, open(os.path.join(dd, "bdc_case_us2007.json"), "w"), indent=1, ensure_ascii=False)

# ----------------------------------------------------------------------------------------------------- Dalio: CWO, Principles
print("CWO / Principles")
cw = load_json("cwo_charts.json")
if cw:
    cw["source"] = "DALIO-CWO-2021-CHARTS"
    json.dump(cw, open(os.path.join(dd, "cwo_gauges.json"), "w"), indent=1, ensure_ascii=False)
copy_md("cwo_charts.md", os.path.join(dd, "cwo_charts_catalogue.md"), ENC)
pm = {"sources": ["DALIO-PRINCIPLES-2011", "DALIO-PRINCIPLES-2017"], "mechanisms": [], "mapping": [], "principles_2017": []}
for ed, name in (("2011", "principles_2011.json"), ("2017", "principles_2017.json")):
    p = load_json(name)
    if not p:
        continue
    for m in p.get("mechanisms", []) or []:
        m = dict(m); m["edition"] = ed; pm["mechanisms"].append(m)
    for m in p.get("mapping", []) or []:
        m = dict(m); m["edition"] = ed; pm["mapping"].append(m)
    pm["principles_2017"] += p.get("principles", []) or [] if ed == "2017" else []
if pm["mechanisms"]:
    json.dump(pm, open(os.path.join(dd, "principles_mechanisms.json"), "w"), indent=1, ensure_ascii=False)
copy_md("principles_2011.md", os.path.join(dd, "principles_2011.md"), ENC)
copy_md("principles_2017.md", os.path.join(dd, "principles_2017.md"), ENC)

# ----------------------------------------------------------------------------------------------------- the reads ledger
print("reads ledger")
if all_reads:
    rows = []
    for n, (src, part, r) in enumerate(all_reads, 1):
        rows.append([f"DALIO-{n:04d}", src, part, "Dalio", r.get("as_of"), "2025-06" if src == "DALIO-HCGB-2025" else "2018-09",
                     r.get("claim"), r.get("horizon"), r.get("probability", ""), r.get("falsifiable"), r.get("criterion"),
                     r.get("outcome_per_author", ""), "open", "", "", r.get("page")])
    write_csv(os.path.join(dd, "reads.csv"),
              ["id", "source", "part", "node", "event_time_as_of", "observed_time_published", "claim", "horizon", "probability",
               "falsifiable", "criterion", "outcome_per_author", "status", "resolved_date", "outcome", "book_page"], rows)
    print(f"  reads: {len(rows)}")
print("done")
