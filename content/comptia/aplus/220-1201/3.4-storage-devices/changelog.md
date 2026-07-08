# Objective 3.4 changelog

## 2026-07-08

- Created initial standard-objective draft for Objective 3.4, Storage Devices.
- Added `study-guide.md`, `checklist.md`, and 22 draft cards: 15 Basic, 7 Cloze,
  and 0 Image.
- Used CompTIA 220-1201 Exam Objectives v4.0 Objective 3.4 as the primary scope
  source and Professor Messer 220-1201 v1.70 pages 32-34 as the approved
  validation reference.
- Used the Professor Messer 220-1201 practice exams only as a private gap check
  for official-scope storage and RAID concepts; no practice-question wording,
  answer choices, scenarios, or explanations were copied or cited in cards.
- Did not create image cards because this draft is focused on storage and RAID
  comparison decisions rather than visual recognition.
- Ran automated verification successfully:
  `.venv/bin/python scripts/validate.py`,
  `.venv/bin/python scripts/build.py`, `.venv/bin/python -m pytest`,
  `.venv/bin/ruff check .`, and `.venv/bin/ruff format --check .`.
- Generated Objective 3.4 TSV output with 15 Basic notes and 7 Cloze notes.
- Completed omitted-concepts review. Exact latency/performance tables,
  capacities, flash-memory electrical details, and full M.2 keying matrices
  remain study-guide-only because they are platform- or product-specific.
- Completed content review and fixed the only required issue by aligning SATA
  and mSATA acronym wording with the official CompTIA glossary expansions.
- Manual Anki smoke test reported passed with 15 Basic notes, 7 Cloze notes,
  and no Image notes. Maintainer acceptance remains pending.
