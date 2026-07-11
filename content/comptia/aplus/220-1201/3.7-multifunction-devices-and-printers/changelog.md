# Objective 3.7 changelog

## 2026-07-11

- Created Objective 3.7 draft for multifunction devices and printers.
- Used CompTIA 220-1201 v4.0 Objective 3.7 as primary scope authority and
  Professor Messer 220-1201 v1.70 pages 41-42 as secondary validation.
- Used Professor Messer 220-1201 practice exams only as a private gap check.
- Added study guide, checklist, 18 Basic cards, and 5 Cloze cards.
- No image cards were created in this draft; device UI or connector visuals may
  be revisited after text review.
- Completed required content-review fixes: removed or narrowed
  finishing/collation references to stay inside official 3.7 scope, and updated
  the checklist review record.
- Regenerated TSV output with 18 Basic notes and 5 Cloze notes.
- Automated verification passed:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`,
  `.venv/bin/python -m pytest`, `.venv/bin/ruff check .`, and
  `.venv/bin/ruff format --check .`.
- Status: required content-review fixes complete; clean recheck and Anki smoke
  test pending.
- Recorded user-reported manual Anki smoke test pass for 18 Basic notes and 5
  Cloze notes. Objective 3.7 has no Image cards, so image/media smoke testing
  was not applicable.
- Status: ready for maintainer acceptance.
