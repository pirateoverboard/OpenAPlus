# Objective 3.5 changelog

## 2026-07-08

- Created Objective 3.5 standard-objective draft for motherboards, CPUs, and
  add-on cards.
- Used CompTIA 220-1201 v4.0 Objective 3.5 as primary scope authority and
  Professor Messer 220-1201 v1.70 pages 34-39 as secondary validation.
- Used Professor Messer 220-1201 practice exams only as a private gap check.
- Added study guide, checklist, 25 Basic cards, and 11 Cloze cards.
- Added generated Domain 3 and Messer validation tag mapping for the new
  objective folder.
- Generated TSV output with 25 Basic notes and 11 Cloze notes.
- Completed required content-review fixes: corrected SATA/eSATA and M.2 Messer
  page citations, narrowed header wording to approved-source support, added a
  direct video-card purpose card, and corrected card counts.
- Automated verification passed:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`,
  `.venv/bin/python -m pytest`, `.venv/bin/ruff check .`, and
  `.venv/bin/ruff format --check .`.
- No image cards were created in this draft; motherboard visual identification
  was considered but deferred to avoid introducing diagram/media scope before
  text coverage is reviewed.
- Status: required content-review fixes complete; clean recheck and Anki smoke
  test pending.

## 2026-07-11

- Added official objective context using the official CompTIA domain, objective
  number, and full objective phrase.
- Completed omitted-concepts review; exact board dimensions, socket part
  numbers, PCIe generation speeds, fan RPM ratings, temperature thresholds, and
  vendor-specific firmware key sequences remain study-guide-only.
- Completed clean content-review recheck with GO for manual Anki smoke test.
- Recorded user-reported manual Anki smoke test pass for 25 Basic notes and 11
  Cloze notes. Objective 3.5 has no Image cards, so image/media smoke testing
  was not applicable.
- Status: ready for maintainer acceptance.
