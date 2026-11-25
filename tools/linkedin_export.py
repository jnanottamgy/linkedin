#!/usr/bin/env python3
"""Read LinkedIn's official data export (Settings > Data privacy > Get a copy of your data).

Turns the export ZIP (or its unzipped folder) into:
  <out>/profile.json  every CSV in the export, as lists of row dicts
  <out>/profile.md    readable profile summary for the linkedin-profile-optimizer skill

Usage:
  python3 tools/linkedin_export.py Basic_LinkedInDataExport_MM-DD-YYYY.zip
  python3 tools/linkedin_export.py path/to/unzipped_folder -o profile-data
Standard library only. Output goes to profile-data/ by default, which is gitignored.
"""
import argparse
import csv
import io
import json
import zipfile
from pathlib import Path


def _rows(text: str) -> list[dict]:
    text = text.lstrip("﻿")
    # Some files (e.g. Connections.csv) open with a "Notes:" block before the header.
    if text.startswith("Notes:"):
        _, _, text = text.partition("\n\n")
    reader = csv.DictReader(io.StringIO(text.strip()))
    return [{k.strip(): (v or "").strip() for k, v in row.items() if k} for row in reader]


def load_export(path: Path) -> dict[str, list[dict]]:
    data = {}
    if path.is_dir():
        for f in sorted(path.rglob("*.csv")):
            data[f.relative_to(path).as_posix()] = _rows(f.read_text(encoding="utf-8", errors="replace"))
    else:
        with zipfile.ZipFile(path) as z:
            for name in sorted(n for n in z.namelist() if n.lower().endswith(".csv")):
                data[name] = _rows(z.read(name).decode("utf-8", errors="replace"))
    return data


def _find(data: dict, filename: str) -> list[dict]:
    for name, rows in data.items():
        if Path(name).name.lower() == filename.lower():
            return rows
    return []


def _span(row: dict, start: str, end: str) -> str:
    s, e = row.get(start, ""), row.get(end, "")
    return f"{s or '?'} - {e or 'Present'}" if (s or e) else ""


def to_markdown(data: dict) -> str:
    out = []
    p = (_find(data, "Profile.csv") or [{}])[0]
    name = f"{p.get('First Name', '')} {p.get('Last Name', '')}".strip()
    out += [f"# {name or 'LinkedIn profile'}", ""]
    for label, key in [("Headline", "Headline"), ("Industry", "Industry"),
                       ("Location", "Geo Location"), ("Websites", "Websites")]:
        if p.get(key):
            out.append(f"**{label}:** {p[key]}  ")
    if p.get("Summary"):
        out += ["", "## About", "", p["Summary"]]

    sections = [
        ("Experience", "Positions.csv", lambda r: (
            f"### {r.get('Title', '')} - {r.get('Company Name', '')}",
            " | ".join(x for x in [_span(r, 'Started On', 'Finished On'), r.get('Location', '')] if x),
            r.get("Description", ""))),
        ("Education", "Education.csv", lambda r: (
            f"### {r.get('School Name', '')}",
            " | ".join(x for x in [r.get('Degree Name', ''), _span(r, 'Start Date', 'End Date')] if x),
            r.get("Notes", "") or r.get("Activities", ""))),
        ("Licenses & certifications", "Certifications.csv", lambda r: (
            f"### {r.get('Name', '')}",
            " | ".join(x for x in [r.get('Authority', ''), _span(r, 'Started On', 'Finished On'),
                                   r.get('License Number', '')] if x),
            r.get("Url", ""))),
        ("Recommendations received", "Recommendations_Received.csv", lambda r: (
            f"### {r.get('First Name', '')} {r.get('Last Name', '')} - {r.get('Job Title', '')}, {r.get('Company', '')}",
            " | ".join(x for x in [r.get('Creation Date', ''), r.get('Status', '')] if x),
            r.get("Text", ""))),
    ]
    for title, fname, fmt in sections:
        rows = _find(data, fname)
        if rows:
            out += ["", f"## {title} ({len(rows)})"]
            for r in rows:
                out += [""] + [line for line in fmt(r) if line]

    for title, fname, key in [("Skills", "Skills.csv", "Name"), ("Languages", "Languages.csv", "Name"),
                              ("Honors", "Honors.csv", "Title"), ("Courses", "Courses.csv", "Name")]:
        rows = _find(data, fname)
        if rows:
            out += ["", f"## {title} ({len(rows)})", "", ", ".join(r.get(key, "") for r in rows if r.get(key))]

    out += ["", "## Files in export", ""] + [f"- {n}: {len(r)} rows" for n, r in data.items()]
    out += ["", "_Not in the export: photo, banner, Featured section. Add screenshots of these for a full audit._"]
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", type=Path, help="export .zip or unzipped folder")
    ap.add_argument("-o", "--out", type=Path, default=Path("profile-data"))
    args = ap.parse_args()
    data = load_export(args.export)
    if not data:
        raise SystemExit(f"No CSV files found in {args.export}")
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "profile.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    (args.out / "profile.md").write_text(to_markdown(data), encoding="utf-8")
    print(f"Read {len(data)} files -> {args.out}/profile.json, {args.out}/profile.md")


if __name__ == "__main__":
    main()
