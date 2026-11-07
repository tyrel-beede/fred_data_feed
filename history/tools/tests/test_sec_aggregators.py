#!/usr/bin/env python3
"""Self-test for the two SEC aggregators in corporate_pull.py, on synthetic data sets built in memory (no network: the
real zips can only be fetched from a desktop). Run: python3 -I history/tools/corporate_pull.py --selftest, or this
file directly. qc.py runs it as one of its checks.

What it exercises:
  13F, thousands era (a 2019-style set with the TSVs inside a folder): filers reporting in thousands and one in
      dollars; a notice (no table); a restatement replacing its original; a new-holdings amendment adding to its
      original; a late filing for the previous period; an options line. Checks the report period, the filings kept,
      the per-filer unit correction, the dollar totals, an issuer's total and the median filer's concentration.
  13F, dollars era (a 2024-style window set at the zip root): one filer still reporting in thousands.
  FSDS: a 10-K/A replacing its original, a co-registrant row, a segment row and an unlisted tag set aside.
"""
import csv, io, json, os, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import corporate_pull as cp  # noqa: E402


def tsv(rows, cols):
    b = io.StringIO(); w = csv.DictWriter(b, fieldnames=cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    return b.getvalue().encode()


def zip_of(members):
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members.items():
            z.writestr(name, data)
    return b.getvalue()


SUB_COLS = ["ACCESSION_NUMBER", "FILING_DATE", "SUBMISSIONTYPE", "CIK", "PERIODOFREPORT"]
COV_COLS = ["ACCESSION_NUMBER", "REPORTCALENDARORQUARTER", "ISAMENDMENT", "AMENDMENTNO", "AMENDMENTTYPE", "FILINGMANAGER_NAME", "REPORTTYPE"]
INFO_COLS = ["ACCESSION_NUMBER", "INFOTABLE_SK", "NAMEOFISSUER", "TITLEOFCLASS", "CUSIP", "VALUE", "SSHPRNAMT", "SSHPRNAMTTYPE", "PUTCALL",
             "INVESTMENTDISCRETION", "OTHERMANAGER", "VOTING_AUTH_SOLE", "VOTING_AUTH_SHARED", "VOTING_AUTH_NONE"]


def line(acc, k, cusip, shares, price, unit, putcall=""):
    value = shares * price / (1000.0 if unit == "thousands" else 1.0)
    return {"ACCESSION_NUMBER": acc, "INFOTABLE_SK": str(k), "NAMEOFISSUER": f"ISSUER {cusip}", "TITLEOFCLASS": "COM", "CUSIP": cusip,
            "VALUE": f"{value:.0f}", "SSHPRNAMT": str(shares), "SSHPRNAMTTYPE": "SH", "PUTCALL": putcall, "INVESTMENTDISCRETION": "SOLE",
            "OTHERMANAGER": "", "VOTING_AUTH_SOLE": str(shares), "VOTING_AUTH_SHARED": "0", "VOTING_AUTH_NONE": "0"}


def build_13f(set_unit, nested):
    """A synthetic set whose filings mostly use set_unit. Returns (zip bytes, expectations)."""
    other = "dollars" if set_unit == "thousands" else "thousands"
    cusips = [f"X{i:02d}" for i in range(1, 13)]; price = {c: 20.0 * (i + 1) for i, c in enumerate(cusips)}
    subs, cov, info, k = [], [], [], 0
    def filing(acc, cik, stype, filed, period, amend="", is_amend="N", report="13F HOLDINGS REPORT"):
        subs.append({"ACCESSION_NUMBER": acc, "FILING_DATE": filed, "SUBMISSIONTYPE": stype, "CIK": cik, "PERIODOFREPORT": period})
        cov.append({"ACCESSION_NUMBER": acc, "REPORTCALENDARORQUARTER": period, "ISAMENDMENT": is_amend, "AMENDMENTNO": "1" if is_amend == "Y" else "",
                    "AMENDMENTTYPE": amend, "FILINGMANAGER_NAME": f"MANAGER {cik}", "REPORTTYPE": report})
    P, P0 = "30-SEP-2019", "30-JUN-2019"
    expect_total, expect_x01, expect_shares = 0.0, 0.0, {}
    def hold(acc, cusip, shares, unit, putcall="", counted=True, filer=None):
        nonlocal k, expect_total, expect_x01
        k += 1
        info.append(line(acc, k, cusip, shares, price[cusip], unit, putcall))
        if counted:
            expect_total += shares * price[cusip]
            if cusip == "X01" and not putcall:
                expect_x01 += shares * price[cusip]
            if filer and not putcall:
                expect_shares.setdefault(filer, []).append(shares * price[cusip])
    # A: twelve positions in the set's unit (its top-10 share is below one)
    filing("A-1", "1", "13F-HR", "15-NOV-2019", P)
    for i, c in enumerate(cusips):
        hold("A-1", c, 10000 * (i + 1), set_unit, filer="1")
    # B: ten positions in the set's unit
    filing("B-1", "2", "13F-HR", "14-NOV-2019", P)
    for c in cusips[:10]:
        hold("B-1", c, 5000, set_unit, filer="2")
    # C: five positions in the OTHER unit (the filer the first aggregator multiplied a thousandfold)
    filing("C-1", "3", "13F-HR", "13-NOV-2019", P)
    for c in cusips[:5]:
        hold("C-1", c, 3000, other, filer="3")
    # D: a notice, no table
    filing("D-1", "4", "13F-NT", "12-NOV-2019", P, report="13F NOTICE")
    # E: original then a restatement (the restatement counts, the original does not)
    filing("E-1", "5", "13F-HR", "10-NOV-2019", P)
    hold("E-1", "X01", 1000, set_unit, counted=False)
    filing("E-2", "5", "13F-HR/A", "20-NOV-2019", P, amend="RESTATEMENT", is_amend="Y")
    hold("E-2", "X01", 2000, set_unit, filer="5")
    # F: original plus a new-holdings amendment (both count, as one filer)
    filing("F-1", "6", "13F-HR", "11-NOV-2019", P)
    hold("F-1", "X02", 1000, set_unit, filer="6")
    filing("F-2", "6", "13F-HR/A", "21-NOV-2019", P, amend="NEW HOLDINGS", is_amend="Y")
    hold("F-2", "X03", 1000, set_unit, filer="6")
    # G: a late report for the previous period (set aside)
    filing("G-1", "7", "13F-HR", "02-OCT-2019", P0)
    hold("G-1", "X01", 100000, set_unit, counted=False)
    # H: one share line and one put
    filing("H-1", "8", "13F-HR", "14-NOV-2019", P)
    hold("H-1", "X02", 1000, set_unit, filer="8")
    hold("H-1", "X01", 50000, set_unit, putcall="PUT", filer="8")
    expect_putcall = 50000 * price["X01"]
    conc = sorted(sum(sorted(v, reverse=True)[:10]) / sum(v) for v in expect_shares.values())
    exp = {"report_period": "2019-09-30", "n_filers": 6, "n_filings_used": 7, "n_filings_other_period": 1, "n_notices": 1,
           "n_restatements_replacing": 1, "n_amendments_new_holdings": 1, "n_filers_unit_corrected": 1, "value_unit_set": set_unit,
           "total": expect_total, "x01": expect_x01, "putcall_share": expect_putcall / expect_total, "median_conc": conc[len(conc) // 2]}
    pre = "2019q4_form13f/" if nested else ""
    return zip_of({pre + "SUBMISSION.tsv": tsv(subs, SUB_COLS), pre + "COVERPAGE.tsv": tsv(cov, COV_COLS), pre + "INFOTABLE.tsv": tsv(info, INFO_COLS)}), exp


def check_13f(set_unit, nested, out):
    data, exp = build_13f(set_unit, nested)
    s, top = cp.aggregate_13f(data)
    def close(a, b, tol=1e-6):
        return abs(float(a) - float(b)) <= tol * max(1.0, abs(float(b)))
    checks = [("report period", s.get("report_period") == exp["report_period"]),
              ("filers counted", s["n_filers"] == exp["n_filers"]),
              ("filings used", s.get("n_filings_used") == exp["n_filings_used"]),
              ("late filing set aside", s.get("n_filings_other_period") == exp["n_filings_other_period"]),
              ("notice set aside", s.get("n_notices") == exp["n_notices"]),
              ("restatement replaces", s.get("n_restatements_replacing") == exp["n_restatements_replacing"]),
              ("new-holdings amendment adds", s.get("n_amendments_new_holdings") == exp["n_amendments_new_holdings"]),
              ("set unit", s["value_unit_set"] == exp["value_unit_set"]),
              ("one filer in the other unit", s["n_filers_unit_corrected"] == exp["n_filers_unit_corrected"]),
              ("total in dollars", close(s["total_value_reported"], exp["total"], 1e-4)),
              ("issuer X01 total", close(next(t["value"] for t in top if t["cusip"] == "X01"), exp["x01"], 1e-4)),
              ("put/call share", close(s["putcall_value_share"], exp["putcall_share"], 1e-3)),
              ("median filer top-10 share", close(s["median_filer_top10_share"], exp["median_conc"], 1e-3)),
              ("aggregator version", s["aggregator_version"] == cp.AGG_VERSION_13F)]
    for name, ok in checks:
        out.append((f"13F {set_unit} era{' (nested)' if nested else ''}: {name}", ok))
    return s


SUB_FSDS = ["adsh", "cik", "name", "sic", "form", "period", "fy", "fp", "filed", "prevrpt", "detail", "instance", "nciks", "aciks"]
NUM_FSDS = ["adsh", "tag", "version", "coreg", "ddate", "qtrs", "uom", "segments", "value", "footnote"]


def check_fsds(out):
    subs, nums = [], []
    for cik in range(1, 26):
        adsh = f"0000{cik:06d}-20-000001"
        subs.append({"adsh": adsh, "cik": str(cik), "name": f"CO {cik}", "sic": "3570", "form": "10-K", "period": "20191231", "fy": "2019", "fp": "FY",
                     "filed": "20200228", "prevrpt": "1" if cik == 1 else "0", "detail": "1", "instance": "x", "nciks": "1", "aciks": ""})
        nums.append({"adsh": adsh, "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "USD",
                     "segments": "", "value": f"{cik * 1e6:.0f}", "footnote": ""})
        nums.append({"adsh": adsh, "tag": "Assets", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "0", "uom": "USD",
                     "segments": "", "value": f"{cik * 1e7:.0f}", "footnote": ""})
    # cik 1 amends its 10-K: the amended net income replaces the original; its assets stay from the original (the 10-K/A does not carry them)
    subs.append({"adsh": "0000000001-20-000009", "cik": "1", "name": "CO 1", "sic": "3570", "form": "10-K/A", "period": "20191231", "fy": "2019", "fp": "FY",
                 "filed": "20200415", "prevrpt": "0", "detail": "1", "instance": "x", "nciks": "1", "aciks": ""})
    nums.append({"adsh": "0000000001-20-000009", "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "USD",
                 "segments": "", "value": "999000000", "footnote": ""})
    # rows that must be set aside: a co-registrant, a segment, a tag off the list, a non-USD unit, an 8-K
    nums.append({"adsh": "0000000002-20-000001", "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "SUBCO", "ddate": "20191231", "qtrs": "4", "uom": "USD", "segments": "", "value": "5e9", "footnote": ""})
    nums.append({"adsh": "0000000002-20-000001", "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "USD", "segments": "Segment=Widgets;", "value": "5e9", "footnote": ""})
    nums.append({"adsh": "0000000002-20-000001", "tag": "SomeOtherTag", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "USD", "segments": "", "value": "5e9", "footnote": ""})
    nums.append({"adsh": "0000000002-20-000001", "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "EUR", "segments": "", "value": "5e9", "footnote": ""})
    subs.append({"adsh": "0000000099-20-000001", "cik": "99", "name": "CO 99", "sic": "3570", "form": "8-K", "period": "20191231", "fy": "2019", "fp": "FY",
                 "filed": "20200228", "prevrpt": "0", "detail": "0", "instance": "x", "nciks": "1", "aciks": ""})
    nums.append({"adsh": "0000000099-20-000001", "tag": "NetIncomeLoss", "version": "us-gaap/2019", "coreg": "", "ddate": "20191231", "qtrs": "4", "uom": "USD", "segments": "", "value": "5e9", "footnote": ""})
    data = zip_of({"2020q1/sub.txt": tsv(subs, SUB_FSDS), "2020q1/num.txt": tsv(nums, NUM_FSDS)})
    rows, meta = cp.aggregate_fsds(data)
    ni = next((r for r in rows if r["tag"] == "NetIncomeLoss"), {}); at = next((r for r in rows if r["tag"] == "Assets"), {})
    exp_ni = sum(c * 1e6 for c in range(2, 26)) + 999e6
    out.append(("FSDS: one value per filer, the amendment replacing its original", ni.get("n_filers") == 25 and abs(float(ni.get("sum_usd", 0)) - exp_ni) < 1))
    out.append(("FSDS: a tag the amendment does not carry keeps the original's value", at.get("n_filers") == 25 and abs(float(at.get("sum_usd", 0)) - sum(c * 1e7 for c in range(1, 26))) < 1))
    out.append(("FSDS: co-registrant, segment, off-list, non-USD and 8-K rows set aside", len(rows) == 2))
    out.append(("FSDS: filing counts", meta["n_filings_10k_10q"] == 26 and meta["n_filings_amendments"] == 1 and meta["n_filers_cik"] == 25))
    out.append(("FSDS: aggregator version", meta["aggregator_version"] == cp.AGG_VERSION_FSDS))


def check_names(out):
    out.append(("13F period end from a quarterly set name", cp.period_end_13f("2014q4_form13f") == "2014-09-30" and cp.period_end_13f("2014q1_form13f") == "2013-12-31"))
    out.append(("13F period end from a window name", cp.period_end_13f("01mar2024-31may2024_form13f") == "2024-03-31" and cp.period_end_13f("01dec2024-28feb2025_form13f") == "2024-12-31"))
    out.append(("dates in the SEC's spellings", cp._iso_date("30-SEP-2014") == "2014-09-30" and cp._iso_date("2014-09-30") == "2014-09-30" and cp._iso_date("20140930") == "2014-09-30"))


def run():
    out = []
    check_names(out)
    check_13f("thousands", True, out)
    check_13f("dollars", False, out)
    check_fsds(out)
    return out


def main():
    out = run()
    bad = [n for n, ok in out if not ok]
    for n, ok in out:
        print(("ok   " if ok else "FAIL ") + n)
    print(f"{len(out) - len(bad)}/{len(out)} checks pass")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
