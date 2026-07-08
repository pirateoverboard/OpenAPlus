# Objective 3.3 changelog

## 2026-07-08 - Initial Objective 3.3 draft

- Determined Objective 3.3 title and slug: `RAM Characteristics`,
  `3.3-ram-characteristics`.
- Used the official CompTIA 220-1201 v4.0 Objective 3.3 as the primary scope
  source.
- Used Professor Messer 220-1201 v1.70 pages 30-31 only as a private validation
  source and for page citations.
- Created original `study-guide.md`, `checklist.md`, and 13 cards: 7 Basic and
  6 Cloze.
- Created no Image cards in this initial draft because the objective can be
  tested with selection, compatibility, and compact recall cards without adding
  media workflow complexity.
- Added scoped Domain 3 Hardware and Messer v1.70 source-validation tag support
  for Objective 3.3 generated output.
- Regenerated Objective 3.3 Basic and Cloze TSV output.
- Verified `validate.py`, `build.py`, `pytest`, Ruff check, and Ruff format
  check pass.
- Avoided Objective 3.4 storage-device content and Objective 5.2
  troubleshooting-drive content.
- Intentionally did not card exact DDR speeds, capacity limits, memory timings,
  voltages, or motherboard slot color conventions.
- At initial draft time, omitted-concepts review, independent content review,
  and any required manual Anki smoke testing remained pending.

## 2026-07-08 - Review-required fixes

- Deleted `3.3-C003` because DRAM refresh behavior is Messer-supported
  background but not an explicit official Objective 3.3 bullet.
- Rewrote `3.3-C004` to test DDR acronym recall instead of duplicating the
  DDR compatibility scenario in `3.3-B003`.
- Deleted `3.3-C006` because it duplicated the multi-channel purpose already
  tested by `3.3-B006`.
- Updated the checklist coverage map and card counts.

## 2026-07-08 - Manual Anki smoke test pass

- Recorded the post-fix manual Anki smoke test pass in `checklist.md`.
- Verified expected import counts in the smoke test: 7 Basic, 4 Cloze, 0 Image,
  11 total notes.
- Verified `Basic.tsv` used the stable Hint column and Hint fields imported
  correctly.
- Verified Basic and Cloze imports; Image import and media rendering were not
  applicable because Objective 3.3 has no Image cards.
- Verified TSV headers were not imported as notes, Card ID was the first field,
  re-import updated existing notes instead of duplicating, HTML rendered
  correctly, Cloze cards generated correctly, and tags imported as Anki
  metadata rather than learner-facing fields.
- Did not modify objectives outside 3.3 or create Objective 3.4 content.
