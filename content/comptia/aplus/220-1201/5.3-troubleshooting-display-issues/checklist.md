# Objective 5.3 completion checklist

**Objective status: ACCEPTED AFTER CLEANUP.** Objective 5.3 has source-backed
draft content, generated output, card-bloat cleanup, and a passed post-cleanup
manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.3-troubleshooting-display-issues` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.3 is treated as troubleshooting display issues. Because the user
requested interview preparation, active-recall cards emphasize visible symptom
recognition, first checks, known-good swaps, display settings, cable/port
isolation, escalation, and professional user communication. Objective 3.1
display-type facts are not repeated unless they are needed for troubleshooting.
Objective 5.1 general no-video content is not repeated except where Objective
5.3 requires display-specific reasoning.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Incorrect input source and basic power/signal checks | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | No image or incorrect input | 5.3-B001, 5.3-B019, 5.3-B020 | Basic | N/A; refactored into separate power, cable, and input retrieval targets | Self-reviewed |
| Known-good display swap to isolate the path | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | No image or incorrect input | 5.3-B002, 5.3-B031, 5.3-B032 | Basic | N/A; monitor-on-known-good-computer, known-good-monitor-on-user-computer, and result interpretation are separate targets | Self-reviewed |
| No video after operating system loads | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | No image or incorrect input | 5.3-B003, 5.3-B033, 5.3-B034 | Basic | N/A; recovery display mode, OS settings, and driver-change action are separate targets | Self-reviewed |
| Projector bulb, heat, airflow, filter, and cooldown behavior | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Projector and audio symptoms | 5.3-B004, 5.3-B021, 5.3-B022 | Basic | N/A; list-style Cloze card removed during card-bloat cleanup | Self-reviewed |
| Fuzzy image and native resolution mismatch | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B005 | Basic | N/A; duplicate Cloze card removed during card-bloat cleanup | Self-reviewed |
| Burn-in and image sticking | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Permanent display defects | 5.3-B006 | Basic | N/A | Self-reviewed |
| Dead pixels | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Permanent display defects | 5.3-B007 | Basic | N/A; duplicate Cloze card removed during card-bloat cleanup | Self-reviewed |
| Flashing screen and loose/bad video cable | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B008 | Basic | N/A | Self-reviewed |
| Incorrect color display, display presets, driver, OS color mode | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Incorrect color and dim image | 5.3-B009, 5.3-B023 | Basic | N/A; refactored into display-control and OS color-mode targets | Self-reviewed |
| Monitor/display audio over video or separate input | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Projector and audio symptoms | 5.3-B010, 5.3-B024, 5.3-B025, 5.3-C004 | Basic, Cloze | N/A; refactored into OS output, local mute, separate-input, and compact transport recall targets | Self-reviewed |
| Dim image settings and backlight failure path | Messer v1.70 p.52; CompTIA 5.3 | Present, p.52 | Incorrect color and dim image | 5.3-B011, 5.3-B026, 5.3-B027, 5.3-I002 | Basic, Image | N/A; text decisions and visual recognition are distinct | Self-reviewed |
| Cable pins causing color or image-quality problems | Messer v1.70 p.53; CompTIA 5.3 | Present, p.53 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B012 | Basic | N/A | Self-reviewed |
| Refresh rate and resolution settings for distorted image | Messer v1.70 p.53; CompTIA 5.3 | Present, p.53 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B013 | Basic | N/A | Self-reviewed |
| Hardware acceleration as a driver troubleshooting isolation step | Messer v1.70 p.53; CompTIA 5.3 | Present, p.53 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B014 | Basic | N/A | Self-reviewed |
| Display scaling and sizing issues | Messer v1.70 p.53; CompTIA 5.3 | Present, p.53 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B015 | Basic | N/A | Self-reviewed |
| Lines, blocks, flashing colors, and artifact pattern recognition | Messer v1.70 p.53; CompTIA 5.3 | Present, p.53 | Fuzzy, distorted, flashing, or incorrectly sized image | 5.3-B016, 5.3-B028, 5.3-B029, 5.3-I001 | Basic, Image | N/A; pre-OS interpretation, known-good tests, and visual recognition are distinct | Self-reviewed |
| Distinguishing cable, display, adapter, and driver paths | Messer v1.70 p.52-53; CompTIA 5.3 | Supported by cable, monitor, adapter, and driver checks | Interview-ready troubleshooting language; interview-practice files | 5.3-B017, 5.3-B028, 5.3-B029 | Basic | N/A; broad spoken troubleshooting answer moved to `interview/` | Self-reviewed |
| Escalation and documentation for display issues | Messer v1.70 p.52-53; CompTIA 5.3 | Supported by symptom and isolation details | Interview-ready troubleshooting language; interview-practice files | 5.3-B018, 5.3-B030 | Basic | N/A; broad spoken escalation answer moved to `interview/` | Self-reviewed |
| Display audio exact codec formats | Source ambiguous for Objective 5.3 | Not present in reviewed Messer 5.3 pages | None | None | None | Intentionally omitted; unsupported and not needed for entry-level triage | Self-reviewed |
| Exact projector lamp model or hours | Messer v1.70 p.52 | General bulb/heat/cooling only | Projector and audio symptoms | None | None | Intentionally omitted; vendor/model-specific and volatile | Self-reviewed |
| Exact refresh-rate and resolution tables | Messer v1.70 p.52-53 | General matching to display specifications only | Fuzzy, distorted, flashing, or incorrectly sized image | None | None | Study-guide only; memorizing tables would duplicate Objective 3.1 and add low-value detail | Self-reviewed |
| GPU driver internals or vendor utilities | Messer v1.70 p.52-53 | General driver/configuration troubleshooting only | None | None | None | Intentionally omitted; vendor-specific and beyond objective depth | Self-reviewed |
| Board-level display or GPU repair | Source ambiguous for Objective 5.3 | Not present in reviewed Messer 5.3 pages | None | None | None | Intentionally omitted; entry-level support should isolate and escalate, not perform board repair | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.3-B001 | Simple power/input/cable triage is a common help desk and exam first step | Self-review; needs independent agreement |
| 5.3-B003 | Video before OS but not after OS is a common decision split | Self-review; needs independent agreement |
| 5.3-B004 | Projector heat/bulb/airflow checks are required troubleshooting decisions | Self-review; needs independent agreement |
| 5.3-B005 | Native-resolution mismatch is a common display-quality issue | Self-review; needs independent agreement |
| 5.3-B008 | Flashing-screen cable checks are a frequent first action | Self-review; needs independent agreement |
| 5.3-B011 | Dim image versus backlight failure is a common support trap | Self-review; needs independent agreement |
| 5.3-B013 | Refresh/resolution checks avoid unnecessary hardware replacement | Self-review; needs independent agreement |
| 5.3-B016 | Pre-OS artifact symptoms help separate hardware-path troubleshooting from app-only causes | Self-review; needs independent agreement |
| 5.3-B018 | Escalation documentation is interview-useful support practice | Self-review; needs independent agreement |
| 5.3-B027 | Persistent faint laptop image after settings are checked is a common backlight escalation clue | Self-review; needs independent agreement |
| 5.3-I001 | Visual artifact recognition is a common display troubleshooting clue | Self-review; needs independent agreement |
| 5.3-I002 | Visual dim-section recognition helps separate settings from backlight faults | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.3 title and troubleshooting-display-issues scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 52-53 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, study-guide-only, and omitted decisions recorded.
- [x] Source ambiguity recorded instead of guessed into cards.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize specific troubleshooting decisions rather than broad interview answers.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards use original SVG diagrams where visual symptom recognition adds value.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts after card-bloat cleanup: 34 Basic, 1 Cloze, 2 Image.
- [x] Optional learner-facing hints added to 17 selected troubleshooting Basic cards; hints guide reasoning without revealing answers.
- [x] Interview-practice directory created with longer spoken-answer scenarios and answer-bank material.
- [x] Broad interview-style cards moved or rewritten into smaller Anki retrieval targets.
- [x] Hint review completed during the refactor; hints remain optional and non-revealing.
- [x] No objective scope was expanded.
- [x] No unrelated objectives were modified.
- [x] Cards added: 5.3-B019 through 5.3-B030.
- [x] Cards rewritten for specificity: 5.3-B001, 5.3-B004, 5.3-B009, 5.3-B010, 5.3-B011, 5.3-B016, 5.3-B017, 5.3-B018.
- [x] Cards removed during card-bloat cleanup: 5.3-C001, 5.3-C002, and 5.3-C003.
- [x] Interview material is not exported to Anki TSV by the existing pipeline.
- [x] Remaining bundled Basic cards fixed: 5.3-B002 and 5.3-B003 were narrowed.
- [x] Split cards added: 5.3-B031 through 5.3-B034.
- [x] Hints reviewed after the bundled-card fix.
- [x] No Objective 5.3 scope was expanded.
- [x] No unrelated objectives were modified.
- [x] Objective 5.4 was not created.

## Card-bloat cleanup verification

Verification run on 2026-07-04 after the approved card-bloat cleanup:

- Deleted 5.3-C001, 5.3-C002, and 5.3-C003 as duplicate/list-style cards
  covered by Basic cards.
- Rewrote 5.3-B016 into a specific pre-OS artifact interpretation card.
- Revised the 5.3-B021 hint so it no longer gives away `filter`.
- Card-bloat cleanup completed.
- Interview-practice material remains outside TSV export.
- No Objective 5.3 scope was expanded.
- No objectives outside 5.1, 5.2, and 5.3 were modified.
- Objective 5.4 was not created.
- TSV output was regenerated.
- Basic.tsv keeps the stable Hint column.
- Manual Anki smoke test passed after cleanup.
- Basic, Cloze, and Image imports passed.
- Hint field import passed.
- Re-import/update behavior passed.
- Tags imported as Anki metadata, not learner-facing fields.
- Image cards and SVG media rendered correctly.
- Interview directory text was not exported to TSV.
- Objective accepted after cleanup.

## Review and build

- [ ] Omitted-concepts review completed.
- [ ] Independent content review completed.
- [x] Original diagrams reviewed for clarity, licensing, and unique names by self-review.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed after cleanup.
- [x] Objective accepted after cleanup.

## Post-cleanup manual Anki smoke test

Manual Anki smoke test recorded on 2026-07-04 after card-bloat cleanup.

Objective 5.3 includes image cards, so Image.tsv and staged SVG media were
included in the smoke test.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Passed |
| Basic Hint column | Passed; Basic.tsv used the stable Hint column |
| Hint field import | Passed |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was first field and drove updates |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Image cards and media rendering | Passed; SVG image media rendered correctly |
| Custom note types | Passed; OpenAPlus Basic, Cloze, and Image note types worked |
| Instructor Notes display | Passed; displayed correctly after answer reveal |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Interview directory text exported | Passed; interview directory text was not exported to TSV |
| Final result | Pass |

## Image-card review

Objective 5.3 uses two original SVG image cards:

- `5.3-I001` shows a generic artifact pattern with no question-side visible
  text or metadata that reveals the answer.
- `5.3-I002` shows a generic dim display section with no question-side visible
  text or metadata that reveals the answer.

No copied screenshots, photos, product layouts, source diagrams, vendor logos,
or private-source artwork were used.

Generated media was staged under
`output/media/220-1201/5.3-troubleshooting-display-issues/` with deterministic
filename-only TSV references.

## Build verification

Verification run on 2026-06-30:

- `.venv/bin/python scripts/validate.py` passed with 310 cards checked.
- `.venv/bin/python scripts/build.py` passed and generated Basic, Cloze, Image,
  and staged media output for Objective 5.3.
- `.venv/bin/python -m pytest` passed with 68 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Basic.tsv uses the stable Hint column.
- Image.tsv references staged filenames only.
- Question-side SVGs were checked for visible text and accessibility metadata
  that would reveal the answer; none was found.
- Scoped diff checks found no changes to Objectives 1.1 through 3.1.
- Objective 5.1 and 5.2 changes were limited to the requested two-layer
  troubleshooting refactor.
- Objectives 3.2 through 4.x and Objective 5.4 were not created.

## Bundled-card fix verification

Verification run on 2026-06-30 after splitting the remaining bundled Basic
cards:

- 5.3-B002 narrowed to testing the monitor with another known-good computer.
- 5.3-B003 narrowed to using low-resolution or recovery display mode.
- 5.3-B031 added for interpreting a known-good monitor and cable test on the user's computer.
- 5.3-B032 added for interpreting a monitor that works on another computer.
- 5.3-B033 added for checking operating-system display settings.
- 5.3-B034 added for video driver correction after a driver update.
- Image cards were not changed.
- Interview-practice material remains outside TSV export.
- Objective 5.4 was not created.
- `.venv/bin/python scripts/validate.py` passed with 323 cards checked.
- `.venv/bin/python scripts/build.py` passed and regenerated TSV and staged media output.
- `.venv/bin/python -m pytest` passed with 68 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Basic.tsv contains 34 data rows and the stable Hint column.
- Image.tsv still contains 2 data rows with the existing Image schema.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-30 | Initial Objective 5.3 draft and coverage decisions completed | Omitted-concepts review, independent content review, automated checks, and manual Anki smoke-test decision | Needs independent review |
| Maintainer manual Anki smoke test | 2026-07-04 | Post-cleanup Basic, Cloze, and Image imports passed; SVG media, Hint field, custom note types, Instructor Notes, tags-as-metadata, interview non-export, and re-import update behavior passed | None | Accepted after cleanup |
