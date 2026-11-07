#!/usr/bin/env python3
"""post_column.py — turn dials/column/<RUN_ID>.md into a blog post on the macrodials site and publish it.

Usage:
  python3 -I dials/tools/post_column.py dials/column/<RUN_ID>.md [--site-dir PATH] [--mode push|pr] [--dry-run]

The column file is written by the macro-column skill: YAML front matter, then the column body in
Markdown, starting with the H1 headline. Front matter keys (all strings unless noted):

  run_id        2026-11-07T0700-column          (required; names the post and the PR branch)
  built_from    2026-11-07T0610-dials           (required; the dials run folder the column was written from)
  date          2026-11-07                      (required; the column date, America/Boise)
  headline      ...                             (required; becomes the H1 if the body has none)
  deck          ...                             (optional; the one-line deck under the headline)
  description   ...                             (optional; Open Graph description; defaults to the deck)
  slug          the-spenders-kept-spending      (optional; defaults to a slug of the headline)
  stale         false                           (optional bool; true adds the stale banner line)
  words         3400                            (optional int)

What it writes on the site (a clone of tyrel-beede/macrodials; cloned into --site-dir if absent):
  docs/blog/posts/<date>-<slug>.md   with the blog front matter the site's Pages build expects
  (date.created, categories [Columns], card, kicker, card_foot, description), the excerpt marker after
  the first body paragraph, and a release stamp that names the run folder the column was generated from.

Modes (default from dials/config.json → column.post_mode; the flag overrides):
  push  commit on main and push — one revert undoes a bad week
  pr    commit on a branch column/<RUN_ID>, push it, open a pull request with `gh api` (REST; `gh pr
        create` is blocked by the proxy) and print its URL — the setting for the first generated columns

The column copy itself lives in the data repository (dials/column/<RUN_ID>.md) and is committed by the
macro-column skill together with its run folder; this script never edits the data repository.
Exit status is non-zero on any failure so the calling skill can report it.
"""
import argparse, datetime as dt, json, os, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve()
DIALS = HERE.parent.parent
SITE_URL = "https://github.com/tyrel-beede/macrodials.git"
SITE_REPO = "tyrel-beede/macrodials"
FEED_REPO = "tyrel-beede/fred_data_feed"


def parse_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit("column file has no front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        meta[k.strip()] = v
    return meta, m.group(2).lstrip("\n")


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)[:80] or "column"


def yq(s):
    """Quote a YAML scalar safely."""
    return json.dumps(str(s), ensure_ascii=False)


def build_post(meta, body):
    for k in ("run_id", "built_from", "date", "headline"):
        if not meta.get(k):
            sys.exit(f"column front matter lacks {k}")
    date = meta["date"]
    dt.date.fromisoformat(date)
    headline = meta["headline"]
    deck = meta.get("deck", "")
    desc = meta.get("description") or deck or headline
    slug = meta.get("slug") or slugify(headline)
    stale = str(meta.get("stale", "false")).lower() in ("1", "true", "yes")
    pretty = dt.date.fromisoformat(date).strftime("%b %-d, %Y")
    run_url = f"https://github.com/{FEED_REPO}/tree/main/dials/runs/{meta['built_from']}"
    col_url = f"https://github.com/{FEED_REPO}/blob/main/dials/column/{meta['run_id']}.md"

    lines = body.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = "\n".join(lines).strip("\n")
    first_break = body.find("\n\n")
    if first_break == -1:
        sys.exit("column body is a single paragraph")
    body = body[:first_break] + "\n\n<!-- more -->" + body[first_break:]

    front = (
        "---\n"
        f"date:\n  created: {date}\n"
        "categories:\n  - Columns\n"
        f"card: column-{date}\n"
        f"kicker: {yq('Bulls, Bears, and the Pigs · built from run ' + meta['built_from'])}\n"
        f"card_foot: {yq('Column · ' + pretty)}\n"
        f"description: {yq(desc)}\n"
        "---\n\n"
    )
    head = f"# {headline}\n\n"
    if deck:
        head += f"*{deck}*\n\n"
    if stale:
        head += ("!!! warning \"Built from a stale run\"\n"
                 f"    This column was written from the `/macro-dials` run `{meta['built_from']}`; every number is as of that run.\n\n")
    stamp = (f"*Generated from `/macro-dials` run [{meta['built_from']}]({run_url}) on {pretty}; "
             f"column source [{meta['run_id']}]({col_url}). Analysis, not advice.*{{ .release-stamp }}\n")
    return f"{date}-{slug}.md", front + head + body.rstrip("\n") + "\n\n" + stamp


def run(cmd, cwd, check=True):
    print("$", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if r.stdout.strip():
        print(r.stdout.strip())
    if r.returncode and check:
        print(r.stderr.strip(), file=sys.stderr)
        sys.exit(f"command failed: {' '.join(cmd)}")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("column")
    ap.add_argument("--site-dir", default=str(pathlib.Path.home() / "macrodials"))
    ap.add_argument("--mode", choices=["push", "pr"])
    ap.add_argument("--dry-run", action="store_true", help="write the post into the site clone but do not commit")
    a = ap.parse_args()

    cfg = json.load(open(DIALS / "config.json"))
    col_cfg = cfg.get("column", {})
    mode = a.mode or col_cfg.get("post_mode", "pr")
    meta, body = parse_front_matter(pathlib.Path(a.column).read_text(encoding="utf-8"))
    name, post = build_post(meta, body)

    site = pathlib.Path(a.site_dir)
    if not (site / ".git").exists():
        site.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", "--depth", "1", SITE_URL, str(site)], cwd=site.parent)
    else:
        run(["git", "fetch", "origin", "main"], cwd=site)
        run(["git", "checkout", "-q", "main"], cwd=site)
        run(["git", "reset", "-q", "--hard", "origin/main"], cwd=site)

    target = site / "docs" / "blog" / "posts" / name
    if target.exists() and target.read_text(encoding="utf-8") == post:
        print("post unchanged:", target)
        return
    target.write_text(post, encoding="utf-8")
    print("wrote", target, len(post), "chars")
    if a.dry_run:
        print("dry run: not committed")
        return

    rel = f"docs/blog/posts/{name}"
    msg = f"column: {meta['run_id']} (from {meta['built_from']})\n\nGenerated by dials/tools/post_column.py from dials/column/{meta['run_id']}.md."
    branch = f"column/{meta['run_id'].replace('T', '-').lower()}"
    if mode == "pr":
        run(["git", "checkout", "-q", "-B", branch], cwd=site)
    run(["git", "add", rel], cwd=site)
    run(["git", "-c", "user.name=macro-column", "-c", "user.email=noreply@macrodials", "commit", "-q", "-m", msg], cwd=site)
    if mode == "push":
        r = run(["git", "push", "origin", "main"], cwd=site, check=False)
        if r.returncode:
            print("push failed once; retrying", file=sys.stderr)
            run(["git", "push", "origin", "main"], cwd=site)
        print("posted to main:", rel)
        return
    run(["git", "push", "-f", "origin", branch], cwd=site)
    title = f"Column {meta['date']}: {meta['headline']}"
    pr_body = (f"Weekly column generated from `/macro-dials` run `{meta['built_from']}` "
               f"(https://github.com/{FEED_REPO}/tree/main/dials/runs/{meta['built_from']}).\n\n"
               f"Column source: `dials/column/{meta['run_id']}.md` in {FEED_REPO}. Review and merge to publish.")
    payload = json.dumps({"title": title, "head": branch, "base": "main", "body": pr_body})
    r = subprocess.run(["gh", "api", f"repos/{SITE_REPO}/pulls", "--method", "POST", "--input", "-"],
                       input=payload, text=True, capture_output=True)
    if r.returncode:
        # an open PR for this branch already exists (a re-run) is the common failure; report rather than fail
        print(r.stderr.strip(), file=sys.stderr)
        ls = subprocess.run(["gh", "api", f"repos/{SITE_REPO}/pulls?head=tyrel-beede:{branch}&state=open"],
                            text=True, capture_output=True)
        try:
            urls = [p["html_url"] for p in json.loads(ls.stdout)]
        except Exception:
            urls = []
        if urls:
            print("branch pushed; existing PR:", urls[0])
            return
        sys.exit("branch pushed but the pull request could not be opened")
    print("pull request:", json.loads(r.stdout)["html_url"])


if __name__ == "__main__":
    main()
