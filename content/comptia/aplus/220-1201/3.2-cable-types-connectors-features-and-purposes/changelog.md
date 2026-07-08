# Objective 3.2 changelog

## 2026-07-06 - Initial Objective 3.2 draft

- Created Objective 3.2 directory using slug
  `3.2-cable-types-connectors-features-and-purposes`.
- Used the official CompTIA 220-1201 Exam Objectives v4.0 PDF as the primary
  scope source. The documented private path was not present locally; the
  matching private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used
  instead.
- Used Professor Messer 220-1201 v1.70 pages 22-29 only as a private
  validation source and for page citations.
- Drafted `study-guide.md`, `checklist.md`, and 28 cards: 14 Basic, 12 Cloze,
  and 2 Image.
- Created original SVG diagrams for modular connector recognition and fiber
  connector recognition.
- Added scoped Domain 3 Hardware and Messer v1.70 source-validation tag support
  for Objective 3.2 generated output.
- Intentionally left exact pin-color order, detailed USB/Thunderbolt speed
  tables, full video bandwidth/distance tables, and every possible adapter
  pairing out of flashcards.
- Did not modify Objectives 1.1 through 3.1, did not create Objective 3.3, and
  did not modify Objectives 5.1 through 5.6.
- Manual Anki smoke testing remains pending because this draft includes Image
  cards.

## 2026-07-07 - USB connector image cards

- Added five original SVG Image cards for USB connector recognition:
  `3.2-I003` through `3.2-I007`.
- Covered USB-A, USB-B, MiniUSB, MicroUSB, and USB-C with generic original
  diagrams. The private PDF was used only as validation/reference context; no
  source diagrams, screenshots, or layouts were copied or traced.
- Updated the coverage map so MicroUSB and MiniUSB are no longer listed as
  study-guide-only omissions.
- Kept USB/Thunderbolt speed and revision tables out of flashcards to avoid
  unstable revision-heavy bloat.

## 2026-07-07 - USB connector image repair

- Replaced the five Codex-created USB connector SVG drawings for `3.2-I003`
  through `3.2-I007` with license-reviewed Wikimedia Commons photo-derived
  media.
- Preserved the existing USB card IDs and learning targets: USB-A, USB-B,
  MiniUSB, MicroUSB, and USB-C.
- Used the public-domain Commons photo `File:Usb connectors.JPG` by Viljo
  Viitanen for the legacy USB connector crops and `File:USB-C plug, focus
  stacked.jpg` by Tomato86 under CC BY-SA 4.0 for USB-C.
- Created source, author, license, attribution, local filename, and modification
  metadata in
  `docs/image-sources/3.2-cable-types-connectors-features-and-purposes.md`.
- Confirmed the question-side USB media contains no visible connector-name
  labels; answer-side media may reveal the connector name after the card answer.
- Kept non-USB Image cards unchanged.
- Removed the obsolete bad USB connector SVG files from use.
- Regenerated TSV/media output and verified that Image.tsv uses filename-only
  media references.
- Did not modify objectives outside 3.2, did not create Objective 3.3, and did
  not commit private PDFs, copied source PDFs, screenshots, OCR exports, or
  unlicensed images.

## 2026-07-08 - Basic/Cloze redundancy cleanup

- Recorded that the manual Anki smoke test failed because several Basic and
  Cloze cards tested the same learning targets.
- Completed a Basic-versus-Cloze redundancy review across all Objective 3.2
  Basic and Cloze cards.
- Deleted redundant Cloze cards instead of preserving card count:
  `3.2-C004`, `3.2-C005`, `3.2-C007`, `3.2-C008`, and `3.2-C011`.
- Kept the matching Basic cards because they test installation decisions,
  comparisons, practical recognition, or common exam traps with useful
  Instructor Notes.
- Kept Image cards only where they test distinct visual connector or diagram
  recognition; USB connector Image cards remain visually useful and
  license-reviewed.
- Did not expand Objective 3.2 scope, did not modify objectives outside 3.2,
  did not create Objective 3.3, and did not modify Objectives 5.1 through 5.6.
- Regenerated TSV/media output after the cleanup.
- New final card counts after TSV regeneration: 14 Basic, 7 Cloze, 7 Image,
  28 total.
