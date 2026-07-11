# Objective 4.1 changelog

## 2026-07-11

- Created Objective 4.1 draft for virtualization concepts.
- Used CompTIA 220-1201 v4.0 Objective 4.1 as primary scope authority and
  Professor Messer 220-1201 v1.70 pages 46-47 as secondary validation.
- Used Professor Messer 220-1201 practice exams only as a private gap check.
- Added study guide, checklist, 18 Basic cards, and 6 Cloze cards.
- No image cards were created in this draft; VM/container diagrams may be
  revisited after text review.
- Applied required independent-review fixes: tightened `4.1-B009` resource
  wording and added `4.1-B018` for hypervisor-security coverage.
- Automated verification passed:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`,
  `.venv/bin/python -m pytest`, `.venv/bin/ruff check .`, and
  `.venv/bin/ruff format --check .`.
- Manual Anki smoke test passed per maintainer report for 18 Basic notes and
  6 Cloze notes; Image.tsv/media testing was not applicable because Objective
  4.1 has no Image cards.
- Status: drafted; required independent-review fixes completed;
  omitted-concepts review and maintainer acceptance are pending.
