# Objective 5.1 changelog

## 2026-06-30 - Initial Objective 5.1 draft

- Created Objective 5.1 directory using slug `5.1-troubleshooting-hardware`.
- Used CompTIA 220-1201 Objective 5.1 as the scope authority and Professor
  Messer 220-1201 v1.70 pages 48-50 as a private validation source.
- Drafted `study-guide.md`, `checklist.md`, and 21 cards: 17 Basic, 4 Cloze,
  and 0 Image.
- Prioritized help desk and interview-style troubleshooting decisions:
  information gathering, simple first checks, theory testing, escalation
  details, and documentation.
- Added the study-guide section `Interview-ready troubleshooting language`.
- Did not create Objective 3.2 through 4.x content and did not create Objective
  5.2 content.
- Did not use image cards because the selected learning targets are technician
  decision points rather than visual-recognition tasks.
- Regenerated Objective 5.1 TSV output.
- Added the minimal Objective 5.1 generated tag mapping so TSV output receives
  Domain 5 troubleshooting and Messer v1.70 source-validation tags without
  manual derived tags in card front matter.
- Verified `validate.py`, `build.py`, `pytest`, Ruff check, and Ruff format
  check pass.

## 2026-06-30 - Final acceptance

- Accepted Objective 5.1 after omitted-concepts review, independent content
  review, and manual Anki smoke testing passed.
- Omitted-concepts review result: GO; exact POST code tables, vendor-specific
  diagnostic menus, exact voltage values, deep replacement procedures,
  Objective 5.2 storage details, and Objective 5.3 display fault trees were
  correctly omitted, left study-guide-only, or deferred.
- Independent content review result: GO; source fidelity, copyright safety,
  objective coverage, card quality, HighYield decisions, Instructor Notes,
  generated output, and scope boundaries passed review.
- Verified `Basic.tsv` and `Cloze.tsv` imported successfully in the
  `OpenAPlus Import Test` deck/profile; `Image.tsv` was not applicable because
  Objective 5.1 has no Image cards.
- Verified expected and actual note counts were both 21, headers were not
  imported as notes, Card ID was the first field and update key, HTML rendered
  correctly, Cloze cards generated correctly, and re-importing updated existing
  notes instead of creating duplicates.
- Verified custom OpenAPlus Basic and Cloze note types worked, Instructor Notes
  displayed correctly after answer reveal, and tags imported as Anki metadata
  rather than learner-facing fields.
- Objectives 3.2 through 4.x were not created.
- Objective 5.2 content was not created.
