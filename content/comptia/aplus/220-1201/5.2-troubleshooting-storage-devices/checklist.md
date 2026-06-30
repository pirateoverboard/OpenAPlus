# Objective 5.2 completion checklist

**Objective status: ACCEPTED.** Objective 5.2 has source-backed content,
generated output, omitted-concepts review, independent content review, stable
Basic Hint-field output, and a passing manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.2-troubleshooting-storage-devices` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.2 is treated as troubleshooting storage devices and storage-related
boot symptoms. Because the user requested interview preparation, active-recall
cards emphasize data protection, first checks, symptom interpretation,
evidence-based escalation, and what not to assume. General hardware symptoms
from Objective 5.1 are not repeated unless they apply directly to storage.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Read/write failure and unreadable source disk | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Storage failure symptoms | 5.2-B001 | Basic | N/A | Self-reviewed |
| Slow storage performance and constant activity | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Storage failure symptoms | 5.2-B002 | Basic | N/A | Self-reviewed |
| Loud clicking, grinding, or scraping noises | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Storage failure symptoms | 5.2-B003 | Basic | N/A | Self-reviewed |
| Mechanical hard drive failure risk | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Storage failure symptoms | 5.2-C001 | Cloze | N/A; compact recall supports scenario reasoning | Self-reviewed |
| Backup before risky disk work | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Data loss and corruption | 5.2-B001, 5.2-B003, 5.2-B010, 5.2-C002 | Basic, Cloze | N/A; decision cards and recall target are distinct | Self-reviewed |
| Boot device not found or drive not recognized | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B004 | Basic | N/A | Self-reviewed |
| Operating system not found while drive is present | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B005 | Basic | N/A | Self-reviewed |
| Boot failure physical checks | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B006 | Basic | N/A | Self-reviewed |
| Boot sequence and removable media | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B007 | Basic | N/A | Self-reviewed |
| Disabled storage interface or new installation configuration | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B008 | Basic | N/A | Self-reviewed |
| Testing a drive in another computer or known-good path | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Boot failure symptoms | 5.2-B009 | Basic | N/A | Self-reviewed |
| SSD read-only or sudden access failure | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | Data loss and corruption | 5.2-B010 | Basic | N/A | Self-reviewed |
| RAID failure alerts and console-first response | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | RAID symptoms and recovery | 5.2-B011, 5.2-C003 | Basic, Cloze | N/A; scenario and compact warning are distinct | Self-reviewed |
| RAID escalation details | Messer v1.70 p.50; CompTIA 5.2 | Present, p.50 | RAID symptoms and recovery | 5.2-B012 | Basic | N/A | Self-reviewed |
| S.M.A.R.T. purpose and trend monitoring | Messer v1.70 p.51; CompTIA 5.2 | Present, p.51 | S.M.A.R.T. and read/write performance | 5.2-B013, 5.2-B014, 5.2-C004 | Basic, Cloze | N/A; action decisions and acronym recall are distinct | Self-reviewed |
| Extended read/write times and IOPS | Messer v1.70 p.51; CompTIA 5.2 | Present, p.51 | S.M.A.R.T. and read/write performance | 5.2-B015 | Basic | N/A | Self-reviewed |
| Missing internal drive after OS boots | Messer v1.70 p.51; CompTIA 5.2 | Present, p.51 | Missing drives in the operating system | 5.2-B016 | Basic | N/A | Self-reviewed |
| Missing external drive | Messer v1.70 p.51; CompTIA 5.2 | Present, p.51 | Missing drives in the operating system | 5.2-B017 | Basic | N/A | Self-reviewed |
| Missing network share | Messer v1.70 p.51; CompTIA 5.2 | Present, p.51 | Missing drives in the operating system | 5.2-B018 | Basic | N/A | Self-reviewed |
| Escalation and documentation for storage issues | Messer v1.70 p.50-51; CompTIA 5.2 | Supported by symptom, diagnostic, and RAID details | Interview-ready troubleshooting language | 5.2-B012, 5.2-B019 | Basic | N/A | Self-reviewed |
| Exact S.M.A.R.T. attribute IDs and thresholds | Messer v1.70 p.51 | General metric trend only | S.M.A.R.T. and read/write performance | None | None | Intentionally omitted; source supports trends and warnings, not memorizing attribute tables | Self-reviewed |
| Vendor-specific disk utilities | Messer v1.70 p.50-51 | General diagnostics and utilities only | None | None | None | Intentionally omitted; tool names vary by vendor and support policy | Self-reviewed |
| Deep data-recovery clean-room procedures | Messer v1.70 p.50 | Recovery described as difficult and expensive | Data loss and corruption | None | None | Study-guide only; entry-level support should escalate rather than perform deep recovery | Self-reviewed |
| RAID rebuild command syntax and vendor procedures | Messer v1.70 p.50 | RAID differences and console review emphasized | RAID symptoms and recovery | None | None | Intentionally omitted; vendor/array-specific and unsafe to generalize | Self-reviewed |
| Exact IOPS values for specific products | Messer v1.70 p.51 | Broad comparison only | S.M.A.R.T. and read/write performance | None | None | Intentionally omitted; volatile and not needed for troubleshooting decisions | Self-reviewed |
| Low disk space as a storage symptom | Source ambiguous for Objective 5.2 | Not present in reviewed Messer 5.2 pages | None | None | None | Not carded; ambiguous source support in reviewed objective material | Self-reviewed |
| BitLocker or encryption recovery-key workflow | Source ambiguous for Objective 5.2 | Not present in reviewed Messer 5.2 pages | None | None | None | Not carded; avoid adding unsupported security workflow to this storage objective | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.2-B001 | Backup-before-repair is a required troubleshooting decision | Self-review; needs independent agreement |
| 5.2-B003 | Clicking or grinding drive noise is a common support escalation clue | Self-review; needs independent agreement |
| 5.2-B004 | Drive-detection boot triage is foundational storage troubleshooting | Self-review; needs independent agreement |
| 5.2-B006 | Cable and power checks are common least-disruptive first actions | Self-review; needs independent agreement |
| 5.2-B007 | Boot order and removable media are common exam and help desk traps | Self-review; needs independent agreement |
| 5.2-B010 | SSD failure behavior prevents false mechanical-drive assumptions | Self-review; needs independent agreement |
| 5.2-B011 | RAID console-first response avoids destructive guesswork | Self-review; needs independent agreement |
| 5.2-B013 | S.M.A.R.T. warning response prevents avoidable data loss | Self-review; needs independent agreement |
| 5.2-B016 | Missing internal drive triage is a common desktop support issue | Self-review; needs independent agreement |
| 5.2-B019 | Storage escalation documentation is interview-useful support practice | Self-review; needs independent agreement |
| 5.2-C002 | Data backup priority is a compact fact used across storage decisions | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.2 title and troubleshooting-storage-devices scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 50-51 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, study-guide-only, and omitted decisions recorded.
- [x] Source ambiguity recorded instead of guessed into cards.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize troubleshooting decisions and interview-style scenarios.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards were considered and intentionally omitted because visual recognition did not add enough value for the selected learning targets.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 19 Basic, 4 Cloze, 0 Image.
- [x] Optional learner-facing hints added to selected troubleshooting Basic cards; hints guide reasoning without revealing answers.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams independently reviewed for clarity and licensing, or not applicable.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [x] Objective accepted by maintainer.

## Hint update

On 2026-06-30, optional `## Hint` sections were added to selected
scenario-heavy Basic cards. Hints were intentionally not added to every card:
direct distinction cards were left without hints when a hint would mostly repeat
the answer. Cloze cards were not changed.

The OpenAPlus Basic TSV schema now includes a Hint field between Front and Back.
Manual Anki smoke testing verified the updated OpenAPlus Basic note type with
the Hint field.

## Manual Anki smoke test

No image cards were created, so image-media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 23 |
| Actual note count | 23 |
| Basic.tsv import | Passed with updated OpenAPlus Basic note type including Hint field |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable |
| Media rendering | Not applicable |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was the first field and drove updates |
| Hint field import | Passed; populated and empty Hint fields imported cleanly |
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
| Self-review | 2026-06-30 | Initial Objective 5.2 draft and coverage decisions completed | Omitted-concepts review, independent content review, automated checks, and manual Anki smoke-test decision | Needs independent review |
| Omitted-concepts review | 2026-06-30 | GO; intentionally not-carded concepts were correctly omitted, left study-guide-only, or deferred pending source support | None | Approved for independent content review |
| Independent content review | 2026-06-30 | GO; source fidelity, copyright safety, objective coverage, card quality, generated output, and scope boundaries passed review | Manual Anki smoke test before acceptance | Ready for manual Anki smoke test |
| Maintainer manual Anki smoke test | 2026-06-30 | Basic and Cloze imports passed; Image import not applicable; Hint field, custom note types, Instructor Notes, tags-as-metadata, and re-import update behavior passed | None | Approved; Objective 5.2 accepted |
