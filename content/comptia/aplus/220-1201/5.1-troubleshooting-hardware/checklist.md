# Objective 5.1 completion checklist

**Objective status: ACCEPTED AFTER CLEANUP.** Objective 5.1 previously passed
review and manual Anki smoke testing, was refactored into regular Anki cards
plus interview-practice material, and then passed post-cleanup manual Anki smoke
testing.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.1-troubleshooting-hardware` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.1 is treated as troubleshooting common hardware symptoms. Because
the user requested interview preparation, active-recall cards emphasize the
technician's next decision: what to ask, what to check first, what evidence
narrows the issue, when to stop for safety, and what to document before
escalation. Concepts from storage, display, mobile, network, and printer
troubleshooting are not expanded unless they appear in the Objective 5.1
hardware-symptom context.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POST purpose and failure indicators | Messer v1.70 p.48; CompTIA 5.1 | Present, p.48 | POST and boot symptoms | 5.1-B001, 5.1-C001 | Basic, Cloze | N/A; documentation decision and acronym recall are distinct | Self-reviewed |
| POST beep/code manufacturer variation | Messer v1.70 p.48; CompTIA 5.1 | Present, p.48 | POST and boot symptoms | 5.1-B001 | Basic | N/A | Self-reviewed |
| Blank screen on boot before OS load | Messer v1.70 p.48; CompTIA 5.1 | Present, p.48 | POST and boot symptoms | 5.1-B002 | Basic | N/A | Self-reviewed |
| Wrong boot device or removable media | Messer v1.70 p.48; CompTIA 5.1 | Present, p.48 | POST and boot symptoms | 5.1-B003 | Basic | N/A | Self-reviewed |
| Inaccurate date/time or reset firmware settings | Messer v1.70 p.50; CompTIA 5.1 | Present, p.50 | Time, battery, and noise symptoms | 5.1-B004 | Basic | N/A; duplicate Cloze card removed during card-bloat cleanup | Self-reviewed |
| Blue screen after driver or hardware change | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B005, 5.1-C002 | Basic, Cloze | N/A; recovery decision and acronym recall are distinct | Self-reviewed |
| Proprietary or application crash messages | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B006, 5.1-B015, 5.1-B026, 5.1-B027 | Basic | N/A; app error text, Event Viewer, and Reliability Monitor are separate evidence targets | Self-reviewed |
| Blank monitor and no-video first checks | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B007, 5.1-B018, 5.1-B019 | Basic | N/A; refactored into separate power, cable, and input retrieval targets | Self-reviewed |
| No power at source or power supply | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B008, 5.1-B022, 5.1-B023 | Basic | N/A; outlet/power strip, cable seating, and PSU switch checks are separate retrieval targets | Self-reviewed |
| Fans spin but no POST | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B009 | Basic | N/A | Self-reviewed |
| Sluggish performance triage | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Performance and overheating | 5.1-B010, 5.1-B011 | Basic | N/A | Self-reviewed |
| Overheating evidence and cooling checks | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Performance and overheating | 5.1-B012, 5.1-B024 | Basic | N/A; fan operation and airflow blockage are separate retrieval targets; duplicate temperature card removed | Self-reviewed |
| Smoke or burning smell | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B013 | Basic | N/A | Self-reviewed |
| Random shutdowns under load | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B014, 5.1-B020 | Basic | N/A; refactored into separate temperature and log-evidence targets | Self-reviewed |
| Unusual noises | Messer v1.70 p.50; CompTIA 5.1 | Present, p.50 | Time, battery, and noise symptoms | 5.1-B016, 5.1-C004 | Basic, Cloze | N/A; scenario and compact symptom association are distinct | Self-reviewed |
| Escalation and documentation details | Messer v1.70 p.49; CompTIA 5.1 | Supported by crash-screen and ticket-detail guidance, p.49 | Interview-ready troubleshooting language; interview-practice files | 5.1-B006, 5.1-B017, 5.1-B021 | Basic | N/A; broad spoken escalation practice moved to `interview/` | Self-reviewed |
| Exact POST beep codes and POST code tables | Messer v1.70 p.48 | Explicitly manufacturer-specific | POST and boot symptoms | None | None | Intentionally omitted; memorize-the-table cards would be misleading and vendor-specific | Self-reviewed |
| Vendor-specific diagnostic menus and utilities | Messer v1.70 p.49 | General diagnostics only | Crash screens and shutdowns | None | None | Study-guide only; exact tools vary by manufacturer and support policy | Self-reviewed |
| Exact voltage values and power-supply rail readings | Messer v1.70 p.49 | General power output check only | Display and power checks | None | None | Intentionally omitted; not necessary for entry-level Objective 5.1 decision cards | Self-reviewed |
| Deep component replacement procedures | CompTIA 5.1 | Not required as procedural depth | None | None | None | Intentionally omitted; objective targets symptom troubleshooting, not repair manuals | Self-reviewed |
| Storage-specific boot repair and SMART interpretation | Messer v1.70 p.50 | Objective 5.2 begins after 5.1 | None | None | None | Intentionally deferred to Objective 5.2; not created here | Self-reviewed |
| Display-specific fault trees | Messer v1.70 p.51 | Objective 5.3 content | None | None | None | Intentionally deferred to Objective 5.3; not created here | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.1-B001 | POST beep/code handling is a common troubleshooting and interview decision | Self-review; needs independent agreement |
| 5.1-B003 | Wrong boot device checks are simple, common, and least-disruptive first actions | Self-review; needs independent agreement |
| 5.1-B005 | Driver-change BSOD recovery is a common support scenario | Self-review; needs independent agreement |
| 5.1-B007 | Monitor power, signal, and input checks prevent unnecessary hardware replacement | Self-review; needs independent agreement |
| 5.1-B008 | No-power isolation is foundational hardware troubleshooting | Self-review; needs independent agreement |
| 5.1-B009 | Spinning fans can mislead technicians about power health | Self-review; needs independent agreement |
| 5.1-B010 | Task Manager triage is a common first step for sluggish systems | Self-review; needs independent agreement |
| 5.1-B012 | Overheating checks are common and prevent unnecessary part replacement | Self-review; needs independent agreement |
| 5.1-B013 | Burning smell requires immediate safety action | Self-review; needs independent agreement |
| 5.1-B017 | Clear escalation documentation is a practical help desk interview skill | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.1 title and troubleshooting-hardware scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 48-50 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, study-guide-only, and omitted decisions recorded.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize specific troubleshooting decisions rather than broad interview answers.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards were considered and intentionally omitted because visual recognition did not add enough value for the selected learning targets.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts after card-bloat cleanup: 26 Basic, 3 Cloze, 0 Image.
- [x] Optional learner-facing hints added to selected troubleshooting Basic cards; hints guide reasoning without revealing answers.
- [x] Interview-practice directory created with longer spoken-answer scenarios and answer-bank material.
- [x] Broad interview-style cards moved or rewritten into smaller Anki retrieval targets.
- [x] Hint review completed during the refactor; hints remain optional and non-revealing.
- [x] No objective scope was expanded.
- [x] No unrelated objectives were modified.
- [x] Cards added: 5.1-B018 through 5.1-B021.
- [x] Cards rewritten for specificity: 5.1-B007, 5.1-B014, 5.1-B017.
- [x] Cards removed during card-bloat cleanup: 5.1-B025 and 5.1-C003.
- [x] Interview material is not exported to Anki TSV by the existing pipeline.
- [x] Remaining bundled Basic cards fixed: 5.1-B008, 5.1-B012, and 5.1-B015 were narrowed.
- [x] Split cards added: 5.1-B022 through 5.1-B027.
- [x] Hints reviewed after the bundled-card fix.
- [x] No Objective 5.1 scope was expanded.
- [x] No unrelated objectives were modified.
- [x] Objective 5.4 was not created.

## Card-bloat cleanup verification

Verification run on 2026-07-04 after the approved card-bloat cleanup:

- Deleted 5.1-B025 as a duplicate of 5.1-B014.
- Deleted 5.1-C003 as a duplicate of 5.1-B004.
- Card-bloat cleanup completed.
- Interview-practice material remains outside TSV export.
- No Objective 5.1 scope was expanded.
- No objectives outside 5.1, 5.2, and 5.3 were modified.
- Objective 5.4 was not created.
- TSV output was regenerated.
- Basic.tsv keeps the stable Hint column.
- Manual Anki smoke test passed after cleanup.
- Basic and Cloze imports passed.
- Hint field import passed.
- Re-import/update behavior passed.
- Tags imported as Anki metadata, not learner-facing fields.
- Interview directory text was not exported to TSV.
- Objective accepted after cleanup.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams independently reviewed for clarity and licensing, or not applicable.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed for the post-cleanup refactored output.
- [x] Objective accepted after cleanup.

## Two-layer refactor verification

Verification run on 2026-06-30 after the two-layer refactor:

- `.venv/bin/python scripts/validate.py` passed with 310 cards checked.
- `.venv/bin/python scripts/build.py` passed and regenerated TSV output.
- `.venv/bin/python -m pytest` passed with 68 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Basic.tsv uses the stable Hint column.
- TSV output does not include the interview-practice Markdown prompt text.
- Objectives 3.2 through 4.x and Objective 5.4 were not created.

## Bundled-card fix verification

Verification run on 2026-06-30 after splitting the remaining bundled Basic
cards:

- 5.1-B008 narrowed to outlet/power-strip verification.
- 5.1-B012 narrowed to fan operation under load.
- 5.1-B015 narrowed to recording the exact application error message.
- 5.1-B022 added for seated power cable checks.
- 5.1-B023 added for the power supply rear switch check when present.
- 5.1-B024 added for blocked vents or dust restricting airflow.
- 5.1-B025 added for temperature readings under load.
- 5.1-B026 added for Event Viewer application-crash evidence.
- 5.1-B027 added for Reliability Monitor application-failure history.
- Interview-practice material remains outside TSV export.
- Objective 5.4 was not created.
- `.venv/bin/python scripts/validate.py` passed with 323 cards checked.
- `.venv/bin/python scripts/build.py` passed and regenerated TSV output.
- `.venv/bin/python -m pytest` passed with 68 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Basic.tsv contains 27 data rows and the stable Hint column.

## Hint update

On 2026-06-30, optional `## Hint` sections were added to selected
scenario-heavy Basic cards. Hints were intentionally not added to every card:
direct symptom-pattern cards were left without hints when a hint would mostly
repeat the answer. Cloze cards were not changed.

The OpenAPlus Basic TSV schema now includes a Hint field between Front and Back.
The prior manual Anki smoke test predates this optional field; future imports
should use the updated OpenAPlus Basic note type field order shown in the TSV
headers.

## Post-cleanup manual Anki smoke test

Manual Anki smoke test recorded on 2026-07-04 after card-bloat cleanup.

No image cards were created for Objective 5.1, so image-media smoke testing was
not applicable.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable |
| Basic Hint column | Passed; Basic.tsv used the stable Hint column |
| Hint field import | Passed |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was first field and drove updates |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom note types | Passed; OpenAPlus Basic and Cloze note types worked |
| Instructor Notes display | Passed; displayed correctly after answer reveal |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Interview directory text exported | Passed; interview directory text was not exported to TSV |
| Final result | Pass |

## Manual Anki smoke test

This smoke test records the pre-refactor accepted output and is superseded by
the 2026-06-30 two-layer refactor. The refactored TSV output requires a new
manual Anki smoke test before re-acceptance.

No image cards were created, so image-media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 21 |
| Actual note count | 21 |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable |
| Media rendering | Not applicable |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was the first field and drove updates |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom note types | Passed; OpenAPlus Basic and Cloze note types worked |
| Instructor Notes display | Passed; displayed correctly after answer reveal |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Final result | Pass |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-30 | Initial Objective 5.1 draft and coverage decisions completed | Omitted-concepts review, independent content review, automated checks, and manual Anki smoke-test decision | Needs independent review |
| Omitted-concepts review | 2026-06-30 | GO; intentionally not-carded concepts were correctly omitted, left study-guide-only, or deferred to later objectives | None | Approved for independent content review |
| Independent content review | 2026-06-30 | GO; source fidelity, coverage, card quality, generated output, and scope boundaries passed review | Manual Anki smoke test before acceptance | Ready for manual Anki smoke test |
| Maintainer manual Anki smoke test | 2026-06-30 | Basic and Cloze imports passed; Image import not applicable; custom note types, Instructor Notes, tags-as-metadata, and re-import update behavior passed | None | Superseded by later two-layer refactor |
| Self-review | 2026-06-30 | Two-layer refactor created interview-practice material and rewrote broad Basic cards into specific retrieval targets | Regenerate TSV and rerun automated verification | Needs independent review and manual Anki smoke test |
| Maintainer manual Anki smoke test | 2026-07-04 | Post-cleanup Basic and Cloze imports passed; Hint field, custom note types, Instructor Notes, tags-as-metadata, interview non-export, and re-import update behavior passed | None | Accepted after cleanup |
