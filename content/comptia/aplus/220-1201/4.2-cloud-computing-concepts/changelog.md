# Objective 4.2 changelog

## 2026-07-11

- Created Objective 4.2 draft for cloud computing concepts.
- Used CompTIA 220-1201 v4.0 Objective 4.2 as primary scope authority and
  Professor Messer 220-1201 v1.70 pages 47-48 as secondary validation.
- Used Professor Messer 220-1201 practice exams only as a private gap check.
- Added study guide, checklist, 19 Basic cards, and 8 Cloze cards.
- No image cards were created in this draft; cloud model recognition is better
  served by concise text cards than original diagrams.
- Omitted-concepts review passed with no required additions.
- Applied required independent-review fix: broadened `4.2-B001` so the cloud
  computing definition includes private and dedicated-resource cloud models
  without implying every cloud must be shared or externally provider-managed.
- Automated verification passed:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`,
  `.venv/bin/python -m pytest`, `.venv/bin/ruff check .`, and
  `.venv/bin/ruff format --check .`.
- Manual Anki smoke test passed per maintainer report for 19 Basic notes and
  8 Cloze notes; Image.tsv/media testing was not applicable because Objective
  4.2 has no Image cards.
- Status: drafted; omitted-concepts review passed and independent-review
  required fixes completed. Smoke testing passed, and maintainer acceptance is
  pending.
