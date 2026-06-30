# Objective 3.1 changelog

## 2026-06-30 - Initial Objective 3.1 draft

- Created Objective 3.1 directory using slug `3.1-display-types-and-attributes`.
- Used Professor Messer 220-1201 v1.70 pages 21-22 only as a private validation
  source and for page citations.
- Drafted `study-guide.md`, `checklist.md`, and 19 cards: 9 Basic, 9 Cloze, and
  1 Image.
- Created original SVG diagrams for the LCD-backlight versus OLED
  self-emissive distinction.
- Added scoped Domain 3 Hardware and Messer v1.70 source-validation tag support
  for Objective 3.1 generated output.
- Regenerated TSV and staged media output for Objective 3.1.
- Verified `validate.py`, `build.py`, `pytest`, Ruff check, Ruff format check,
  website typecheck, and website build pass.
- Intentionally did not modify Objectives 1.1 through 2.8 and did not create
  Objective 3.2 content.
- Manual Anki smoke testing remains pending because this draft includes an Image
  card.

## 2026-06-30 - Review blocker fixes before Anki smoke test

- Removed question-side SVG answer leaks from title, description, and visible
  panel captions in `display-lighting-question.svg`.
- Added one compact screen-resolution active-recall Cloze card, `3.1-C010`.
- Kept exact refresh/resolution mode tables, vendor-specific display model
  claims, and laptop disassembly steps out of flashcards.
- Regenerated Objective 3.1 TSV and staged media output.
- Did not create Objective 3.2 content.

## 2026-06-30 - Final acceptance

- Accepted Objective 3.1 after manual Anki smoke testing passed in the
  `OpenAPlus Import Test` deck/profile.
- Verified `Basic.tsv`, `Cloze.tsv`, and `Image.tsv` imported successfully, with
  headers ignored as notes and Card ID used as the first-field update key.
- Verified custom OpenAPlus Basic, Cloze, and Image note types rendered HTML,
  Cloze deletions, Instructor Notes after answer reveal, and tags as Anki
  metadata rather than learner-facing fields.
- Verified Objective 3.1 SVG media rendered correctly: the question-side SVG did
  not reveal answer labels through visible text or accessibility metadata, and
  the answer-side SVG displayed the correct labels after reveal.
- Verified re-importing updated existing notes instead of creating duplicates.
- No Objective 3.2 content was created.
