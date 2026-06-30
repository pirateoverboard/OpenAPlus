# Objective 5.1 completion checklist

**Objective status: ACCEPTED.** Objective 5.1 has source-backed content,
generated output, omitted-concepts review, independent content review, and a
passing manual Anki smoke test.

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
| Inaccurate date/time or reset firmware settings | Messer v1.70 p.50; CompTIA 5.1 | Present, p.50 | Time, battery, and noise symptoms | 5.1-B004, 5.1-C003 | Basic, Cloze | N/A; scenario and compact battery function recall are distinct | Self-reviewed |
| Blue screen after driver or hardware change | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B005, 5.1-C002 | Basic, Cloze | N/A; recovery decision and acronym recall are distinct | Self-reviewed |
| Proprietary or application crash messages | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B006, 5.1-B015 | Basic | N/A | Self-reviewed |
| Blank monitor and no-video first checks | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B007 | Basic | N/A | Self-reviewed |
| No power at source or power supply | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B008 | Basic | N/A | Self-reviewed |
| Fans spin but no POST | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B009 | Basic | N/A | Self-reviewed |
| Sluggish performance triage | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Performance and overheating | 5.1-B010, 5.1-B011 | Basic | N/A | Self-reviewed |
| Overheating evidence and cooling checks | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Performance and overheating | 5.1-B012 | Basic | N/A | Self-reviewed |
| Smoke or burning smell | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Display and power checks | 5.1-B013 | Basic | N/A | Self-reviewed |
| Random shutdowns under load | Messer v1.70 p.49; CompTIA 5.1 | Present, p.49 | Crash screens and shutdowns | 5.1-B014 | Basic | N/A | Self-reviewed |
| Unusual noises | Messer v1.70 p.50; CompTIA 5.1 | Present, p.50 | Time, battery, and noise symptoms | 5.1-B016, 5.1-C004 | Basic, Cloze | N/A; scenario and compact symptom association are distinct | Self-reviewed |
| Escalation and documentation details | Messer v1.70 p.49; CompTIA 5.1 | Supported by crash-screen and ticket-detail guidance, p.49 | Interview-ready troubleshooting language | 5.1-B006, 5.1-B017 | Basic | N/A | Self-reviewed |
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
- [x] Basic cards emphasize troubleshooting decisions and interview-style scenarios.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards were considered and intentionally omitted because visual recognition did not add enough value for the selected learning targets.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 17 Basic, 4 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams independently reviewed for clarity and licensing, or not applicable.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [x] Objective accepted by maintainer.

## Manual Anki smoke test

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
| Maintainer manual Anki smoke test | 2026-06-30 | Basic and Cloze imports passed; Image import not applicable; custom note types, Instructor Notes, tags-as-metadata, and re-import update behavior passed | None | Approved; Objective 5.1 accepted |
