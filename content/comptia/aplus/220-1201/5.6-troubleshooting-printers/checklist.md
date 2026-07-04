# Objective 5.6 completion checklist

**Objective status: ACCEPTED.** Objective 5.6 has source-backed content,
original SVG image cards, generated TSV/media output, interview-practice
material, completed review fixes, and a passing manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.6-troubleshooting-printers` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.6 is treated as troubleshooting printer symptoms. Because the user
requested interview preparation, active-recall cards emphasize evidence-driven
printer isolation: application versus printer, driver versus printer engine,
consumables and imaging components, paper path, queue/spooler, finishing
hardware, tray configuration, network connectivity, print server scope, and
documentation.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Printer test page and diagnostic utilities | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Printer Test and Diagnostic Pages | 5.6-B001, 5.6-B002 | Basic | N/A; application isolation and printer utility selection are separate targets | Self-reviewed |
| Lines down printed page | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Bad Output | 5.6-B003, 5.6-B004, 5.6-I001 | Basic, Image | N/A; inkjet check, laser check, and visual recognition are separate targets | Self-reviewed |
| Faded prints or blank pages | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Bad Output | 5.6-B005 | Basic | N/A | Self-reviewed |
| Double/echo images, ghosting, and speckling | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Bad Output | 5.6-B006, 5.6-I002 | Basic, Image | N/A; text scenario and visual recognition are separate targets | Self-reviewed |
| Garbled print and page description language | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Bad Output | 5.6-B007, 5.6-B008, 5.6-C001, 5.6-I003 | Basic, Cloze, Image | N/A; driver suspicion, application isolation, compact PDL examples, and visual recognition are separate targets | Self-reviewed |
| Paper jam safety | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Paper Path and Mechanical Symptoms | 5.6-B009, 5.6-B010 | Basic | N/A; safe removal and stop/escalate decision are separate targets | Self-reviewed |
| Paper not feeding or multiple-page misfeeds | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Paper Path and Mechanical Symptoms | 5.6-B011, 5.6-B012, 5.6-C003 | Basic, Cloze | N/A; tray check, pickup roller interpretation, and compact maintenance-kit recall are separate targets | Self-reviewed |
| Creased paper | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Paper Path and Mechanical Symptoms | 5.6-B013 | Basic | N/A | Self-reviewed |
| Multiple pending jobs and spooler issues | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Queue and Spooler Problems | 5.6-B014, 5.6-B015, 5.6-B016 | Basic | N/A; queue observation, logs, and problem-job isolation are separate targets | Self-reviewed |
| Grinding noises | Messer v1.70 p.56; CompTIA 5.6 | Present, p.56 | Paper Path and Mechanical Symptoms | 5.6-B017, 5.6-B018, 5.6-B019 | Basic | N/A; likely mechanical category, documentation/manual process, and maintenance/replacement escalation are separate targets | Self-reviewed |
| Finishing issues | Messer v1.70 p.57; CompTIA 5.6 | Present, p.57 | Finishing, Orientation, and Tray Configuration | 5.6-B020, 5.6-B021, 5.6-B022 | Basic | N/A; finishing timing, staple-jam safety, and hole-punch driver check are separate targets | Self-reviewed |
| Incorrect page orientation | Messer v1.70 p.57; CompTIA 5.6 | Present, p.57 | Finishing, Orientation, and Tray Configuration | 5.6-B023, 5.6-B024 | Basic | N/A; print-setting check and printer-default check are separate targets | Self-reviewed |
| Tray not recognized and paper-size mismatch | Messer v1.70 p.57; CompTIA 5.6 | Present, p.57 | Finishing, Orientation, and Tray Configuration | 5.6-B025, 5.6-B026 | Basic | N/A; driver tray definition and page-size mismatch are separate targets | Self-reviewed |
| Printer connectivity issues | Messer v1.70 p.57; CompTIA 5.6 | Present, p.57 | Connectivity and Print Server Scope | 5.6-B027, 5.6-B028, 5.6-B029, 5.6-B030 | Basic | N/A; connection type, IP configuration, print server, and test result interpretation are separate targets | Self-reviewed |
| Escalation and documentation | Messer v1.70 p.56-57; CompTIA 5.6 | Supported across Objective 5.6 symptom set | Interview-ready Troubleshooting Language; interview-practice file | 5.6-B031, 5.6-B032 | Basic | N/A; bad-output escalation and queue/connectivity escalation are separate documentation targets | Self-reviewed |
| Broad printer troubleshooting explanations | Messer v1.70 p.56-57; CompTIA 5.6 | Supported across Objective 5.6 symptom set | Interview-ready Troubleshooting Language; interview-practice file | None | None | Broad spoken answers belong in `interview/`, not TSV cards | Self-reviewed |
| Exact vendor utility names and web UI paths | Messer v1.70 p.56 | General diagnostic utility concept only | Printer Test and Diagnostic Pages | None | None | Intentionally omitted; vendor-specific and volatile | Self-reviewed |
| Model-specific paper jam removal steps | Messer v1.70 p.56-57 | General manufacturer-process caution only | Paper Path and Mechanical Symptoms; Finishing, Orientation, and Tray Configuration | None | None | Intentionally omitted; source supports using the approved process, not memorizing model procedures | Self-reviewed |
| Exact Windows Event Viewer navigation | Messer v1.70 p.56 | Windows logging location present | Queue and Spooler Problems | None | None | Study-guide only; volatile UI path detail is not needed for A+ recall | Self-reviewed |
| Deep laser printer repair procedures | Messer v1.70 p.56 | Symptom/component clues present | Bad Output; Paper Path and Mechanical Symptoms | None | None | Intentionally omitted; entry-level support should identify, document, and escalate hardware repair beyond scope | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.6-B001 | Test pages are a foundational printer isolation step | Self-review; needs independent agreement |
| 5.6-B003 | Inkjet lines and print-head cleaning are common output troubleshooting clues | Self-review; needs independent agreement |
| 5.6-B004 | Laser lines and drum checks are common output troubleshooting clues | Self-review; needs independent agreement |
| 5.6-B005 | Faded/blank output and consumable checks are frequent help desk issues | Self-review; needs independent agreement |
| 5.6-B007 | Garbled output and driver/PDL mismatch are common printer troubleshooting targets | Self-review; needs independent agreement |
| 5.6-B009 | Paper jam safety prevents additional damage | Self-review; needs independent agreement |
| 5.6-B014 | Queue triage is a common help desk printer task | Self-review; needs independent agreement |
| 5.6-B017 | Grinding noises require mechanical caution | Self-review; needs independent agreement |
| 5.6-B023 | Orientation errors are common user-facing printer tickets | Self-review; needs independent agreement |
| 5.6-B025 | Tray definition mismatch is a common office printer issue | Self-review; needs independent agreement |
| 5.6-B027 | Printer connectivity starts with connection type | Self-review; needs independent agreement |
| 5.6-I001 | Visual recognition of vertical page defects improves troubleshooting | Self-review; needs independent agreement |
| 5.6-I002 | Visual recognition of ghosting improves troubleshooting | Self-review; needs independent agreement |
| 5.6-I003 | Visual recognition of garbled output improves driver/PDL triage | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.6 title and troubleshooting-printers scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 56-57 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, photos, screenshots, or layout.
- [x] Card, study-guide-only, interview-only, and omitted decisions recorded.
- [x] Source ambiguity recorded instead of guessed into cards.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize specific troubleshooting decisions rather than broad interview answers.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards use original SVG diagrams for visual printer-output symptoms.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] Duplicate Cloze cleanup completed; 5.6-C002 was deleted as a duplicate of 5.6-B020.
- [x] Current draft card counts after review cleanup: 32 Basic, 2 Cloze, 3 Image.
- [x] Optional learner-facing hints added to selected troubleshooting Basic cards; hints guide reasoning without revealing answers.
- [x] Interview-practice directory created with longer spoken-answer scenarios.
- [x] Broad interview-style prompts kept out of regular Anki.
- [x] No Objective 5.6 scope was expanded.
- [x] No objectives outside Objective 5.6 were modified for content.
- [x] No objective after 5.6 was created.
- [x] No unrelated cards were deleted during review cleanup.
- [x] Image cards remain appropriate after review cleanup.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent review blockers fixed.
- [x] Duplicate card cleanup completed.
- [x] Question-side SVG answer-leak review passed.
- [x] Original diagrams reviewed for clarity, licensing, answer leakage, and unique names.
- [x] `.venv/bin/python scripts/validate.py` passes.
- [x] `.venv/bin/python scripts/build.py` passes and TSV/media output is regenerated.
- [x] `.venv/bin/python -m pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Basic, Cloze, and Image imports passed.
- [x] Basic.tsv stable Hint column and Hint field import passed.
- [x] Media copy/import test passed.
- [x] Re-import/update behavior passed using Card ID as the first field.
- [x] Tags imported as Anki metadata, not learner-facing fields.
- [x] Interview directory text was not exported to TSV.
- [x] Objective accepted by maintainer.

## Build verification

- 2026-07-04: `.venv/bin/python scripts/validate.py` passed with 432 cards checked.
- 2026-07-04: `.venv/bin/python scripts/build.py` passed and regenerated TSV/media output.
- 2026-07-04: Generated Objective 5.6 TSV counts verified: 32 Basic, 3 Cloze, 3 Image.
- 2026-07-04: `Basic.tsv` uses the stable Hint column:
  `Card ID, Front, Hint, Back, Instructor Notes, Difficulty, Card Type, Objective, Source, Tags`.
- 2026-07-04: Objective 5.6 generated tags include the 5.6 objective tag,
  normalized objective-name tag, Domain 5 troubleshooting tag, card-type tag,
  HighYield where applicable, source-validation tag, and author topic tags.
- 2026-07-04: Image TSV references Anki-safe filename-only media names.
- 2026-07-04: Generated media output exists under
  `output/media/220-1201/5.6-troubleshooting-printers/`.
- 2026-07-04: Interview-practice text was not exported to regular TSV output.
- 2026-07-04: `.venv/bin/python -m pytest` passed with 71 tests.
- 2026-07-04: `.venv/bin/ruff check .` passed.
- 2026-07-04: `.venv/bin/ruff format --check .` passed.
- 2026-07-04: No objective after 5.6 was created.
- 2026-07-04: Omitted-concepts review passed.
- 2026-07-04: Independent review blockers fixed before manual Anki smoke test.
- 2026-07-04: Deleted 5.6-C002 as a duplicate of 5.6-B020.
- 2026-07-04: Fixed answer leakage in `garbled-output-question.svg`.
- 2026-07-04: Confirmed Image cards remain appropriate.
- 2026-07-04: Interview-practice text remains separate from TSV output.
- 2026-07-04: No unrelated cards were deleted.
- 2026-07-04: No objectives outside Objective 5.6 were modified for content.
- 2026-07-04: No later objective was created.
- 2026-07-04: TSV and media regenerated after review fixes.
- 2026-07-04: Final generated counts after cleanup verified: 32 Basic, 2 Cloze, 3 Image, 37 total.
- 2026-07-04: Manual Anki smoke test passed in test deck/profile
  `OpenAPlus Import Test`.
- 2026-07-04: Basic import passed, Cloze import passed, and Image import
  passed for 32 Basic, 2 Cloze, 3 Image, 37 total notes.
- 2026-07-04: `Basic.tsv` used the stable Hint column and Hint fields imported
  correctly.
- 2026-07-04: TSV headers were not imported as notes; Card ID was the first
  field and drove duplicate/update behavior.
- 2026-07-04: HTML rendered correctly, Cloze cards generated correctly, and
  Image cards rendered correctly.
- 2026-07-04: Objective 5.6 media files were copied into Anki
  `collection.media`.
- 2026-07-04: Custom OpenAPlus Basic, Cloze, and Image note types worked.
- 2026-07-04: Instructor Notes displayed correctly after answer reveal.
- 2026-07-04: Tags imported as Anki metadata, not learner-facing fields.
- 2026-07-04: Re-import updated existing notes instead of duplicating them.
- 2026-07-04: Interview directory text was not exported to TSV.
- 2026-07-04: Objective 5.6 accepted after cleanup and manual smoke testing.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-04 | Initial Objective 5.6 draft and coverage decisions completed | Automated verification, omitted-concepts review, independent content review, and manual Anki smoke-test decision | Needs independent review |
| Independent review | 2026-07-04 | Omitted-concepts and content review blockers resolved; question-side SVG answer-leak review passed | Deleted 5.6-C002, fixed garbled-output question SVG answer leakage, regenerated TSV/media output | Approved for smoke test |
| Manual Anki smoke test | 2026-07-04 | Basic, Cloze, and Image imports passed with expected counts; media, hints, tags, HTML, note types, and duplicate/update behavior verified | None | Accepted |
