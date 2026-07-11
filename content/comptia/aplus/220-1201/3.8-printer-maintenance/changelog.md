# Objective 3.8 changelog

## 2026-07-11

- Created Objective 3.8 draft for printer maintenance.
- Used CompTIA 220-1201 v4.0 Objective 3.8 as primary scope authority and
  Professor Messer 220-1201 v1.70 pages 43-45 as secondary validation.
- Used Professor Messer 220-1201 practice exams only as a private gap check.
- Added study guide, checklist, 19 Basic cards, and 5 Cloze cards.
- No image cards were created in this draft; printer component visuals may be
  revisited after text review.
- Automated verification passed:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`,
  `.venv/bin/python -m pytest`, `.venv/bin/ruff check .`, and
  `.venv/bin/ruff format --check .`.
- Recorded user-reported manual Anki smoke test pass for 19 Basic notes and 5
  Cloze notes. Objective 3.8 has no Image cards, so image/media smoke testing
  was not applicable.
- Applied required independent-review fix to `3.8-B018` so impact printhead
  coverage tests an action-oriented replacement maintenance decision.
- Status: drafted with smoke test passed; required independent-review fix
  completed; omitted-concepts review is pending.
