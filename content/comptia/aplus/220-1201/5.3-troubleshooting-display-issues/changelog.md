# Objective 5.3 changelog

## 2026-07-04 - Final cleanup acceptance

- Accepted Objective 5.3 after post-cleanup manual Anki smoke testing passed.
- Verified Basic, Cloze, and Image imports in the `OpenAPlus Import Test`
  deck/profile.
- Verified Basic.tsv used the stable Hint column and Hint fields imported
  correctly.
- Verified headers were not imported as notes.
- Verified Card ID was the first field and drove duplicate/update behavior.
- Verified HTML rendered correctly and Cloze cards generated correctly.
- Verified SVG image media rendered correctly for Objective 5.3 image cards.
- Verified custom OpenAPlus Basic, Cloze, and Image note types worked.
- Verified Instructor Notes displayed correctly after answer reveal.
- Verified tags imported as Anki metadata, not learner-facing fields.
- Verified re-importing updated existing notes instead of duplicating them.
- Verified interview directory text was not exported to TSV.
- No Objective 5.4 content was created.

## 2026-07-04 - Card-bloat cleanup

- Deleted `5.3-C001`, `5.3-C002`, and `5.3-C003` as duplicate/list-style cards
  covered by Basic cards.
- Rewrote `5.3-B016` into a specific pre-OS artifact interpretation card.
- Revised the `5.3-B021` hint so it no longer gives away `filter`.
- Regenerated TSV output.
- Card-bloat cleanup completed.
- No interview-practice material was exported into TSV.
- No Objective 5.3 scope was expanded.
- No objectives outside 5.1, 5.2, and 5.3 were modified.
- Objective 5.4 was not created.

## 2026-06-30 - Remaining bundled Basic-card fixes

- Narrowed `5.3-B002` to testing the monitor with another known-good computer.
- Narrowed `5.3-B003` to using low-resolution or recovery display mode.
- Added `5.3-B031` for interpreting a known-good monitor and cable test on the
  user's computer.
- Added `5.3-B032` for interpreting a monitor that works on another computer.
- Added `5.3-B033` for checking operating-system display settings.
- Added `5.3-B034` for correcting the video driver after a driver update.
- Removed no cards and did not change Cloze or Image cards.
- Reviewed hints after the split; retained only short non-revealing hints where
  they help reasoning before reveal.
- Updated `checklist.md` with narrowed IDs, new split IDs, updated counts, and
  non-export behavior for interview-practice files.
- Regenerated TSV output and left existing staged image media behavior
  unchanged.
- Did not expand Objective 5.3 scope, modify unrelated objectives, create
  Objective 5.4, or add APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Two-layer troubleshooting refactor

- Created `interview/` with `interview-scenarios.md` and
  `interview-answer-bank.md` for longer spoken troubleshooting practice.
- Moved broad display interview and escalation talk tracks out of regular Anki
  Basic answers and into the interview-practice files.
- Rewrote regular Basic cards to favor one specific display symptom, check,
  known-good test, or documentation decision per card.
- Rewrote `5.3-B001`, `5.3-B004`, `5.3-B009`, `5.3-B010`, `5.3-B011`,
  `5.3-B016`, `5.3-B017`, and `5.3-B018` for narrower retrieval targets.
- Added `5.3-B019` through `5.3-B030` for separate cable seating, input source,
  projector airflow/filter/cooldown, OS color mode, display audio, dim-display,
  known-good artifact isolation, and documentation targets.
- Removed no cards.
- Reviewed hints during the split; retained only short non-revealing hints
  where they help pre-reveal reasoning.
- Updated `study-guide.md` to point longer interview practice to the
  `interview/` directory.
- Updated `checklist.md` to record the two-layer refactor, new counts, rewritten
  card IDs, and interview-material non-export behavior.
- Regenerated TSV output and staged media output remains generated for the two
  original SVG Image cards.
- Did not expand Objective 5.3 scope.
- Did not create Objectives 3.2 through 4.x, modify Objectives 1.1 through 3.1,
  modify Objectives 5.1 or 5.2 beyond this requested two-layer refactor, create
  Objective 5.4 content, or add APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Initial draft

- Confirmed Objective 5.3 title as **Troubleshooting Display Issues** from the
  available 220-1201 objective reference and Professor Messer 220-1201 v1.70
  notes.
- Reviewed Professor Messer 220-1201 v1.70 pages 52-53 as a private validation
  source; no private PDF, OCR export, screenshots, tables, or diagrams were
  copied into the repository.
- Created the Objective 5.3 study guide, checklist, changelog, 18 Basic cards,
  4 Cloze cards, and 2 Image cards.
- Created two original SVG image-card pairs for visual display symptom
  recognition: artifact pattern and partial dim/backlight symptom.
- Added Objective 5.3 derived tag mapping so generated TSV output includes
  `A+::220-1201::Domain5-Troubleshooting` and `Source::Messer-v170`.
- Added a pipeline test covering Objective 5.3 generated domain and
  source-validation tags.
- Generated Objective 5.3 Basic.tsv, Cloze.tsv, Image.tsv, and staged SVG media
  output with deterministic filename-only media references.
- Added interview-ready troubleshooting language focused on checking simple
  causes first, isolating display/cable/port/computer paths, and documenting
  escalation details.
- Ran validation, build, tests, Ruff lint, and Ruff format check successfully:
  291 cards validated, 68 tests passed, and Ruff reported no issues.
- Intentionally did not create Objectives 3.2 through 4.x, modify Objectives
  1.1 through 3.1, modify Objectives 5.1 or 5.2, or start Objective 5.4.

## Source ambiguity and no-card decisions

- Display audio codec details were not carded because the reviewed sources
  support audio input/output troubleshooting, not codec-level memorization.
- Exact projector bulb model or life-hour values were not carded because those
  details are vendor/model-specific and volatile.
- Exact refresh-rate/resolution tables were not carded because Objective 5.3
  tests troubleshooting the mismatch, not memorizing display-mode tables.
- GPU driver internals and vendor utilities were not carded because the reviewed
  sources support general driver/configuration troubleshooting only.
- Board-level display or graphics repair was omitted because it is not supported
  by the reviewed Objective 5.3 material and is beyond entry-level support.
