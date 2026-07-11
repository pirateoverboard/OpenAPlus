# Objective 3.8 completion checklist

**Objective status: DRAFTED; SMOKE TEST PASSED.** Objective 3.8 has
source-backed draft content, generated TSV output, passing automated
verification, and a passing manual Anki smoke test. Omitted-concepts review,
independent content review, and maintainer acceptance are still pending.

## Official objective context

Domain 3.0 Hardware, Objective 3.8: Given a scenario, perform appropriate
printer maintenance.

Official bullet scope:

- Laser: maintenance to replace toner, apply maintenance kit, calibrate, and clean
- Inkjet: ink cartridge, printhead, roller, and feeder
- Inkjet maintenance: clean printheads, replace cartridges, calibrate, and clear jams
- Thermal: feed assembly and special thermal paper
- Thermal maintenance: replace paper, clean heating element, and remove debris
- Impact: multipart paper
- Impact maintenance: replace ribbon, printhead, and paper

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.8-printer-maintenance` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.8 is driven by the official `Given a scenario` wording. Cards focus
on practical maintenance choices for laser, inkjet, thermal, and impact
printers. The objective does not require separate interview-style
troubleshooting material; broad printer symptom triage belongs mainly to
Objective 5.6.

## Objective-specific cautions

- Do not drift into Objective 3.7 deployment settings such as printer shares,
  drivers, scan services, secured print, or ADF/flatbed configuration.
- Do not drift into Objective 5.6 broad printer troubleshooting beyond
  source-supported maintenance decisions.
- Do not over-card exact page-count thresholds, vendor maintenance-kit part
  numbers, proprietary cartridge codes, cleaning menu paths, or model-specific
  service procedures.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Laser toner replacement and OPC drum caution | CompTIA 3.8; Messer v1.70 p.43 | Present, p.43 | Laser Printer Maintenance | 3.8-B001, 3.8-C001 | Basic, Cloze | N/A; replacement decision and acronym recall are distinct | Self-reviewed |
| Laser maintenance kit contents and timing | CompTIA 3.8; Messer v1.70 p.43; private practice gap check | Present, p.43 | Laser Printer Maintenance | 3.8-B002 | Basic | N/A | Self-reviewed |
| Laser fuser safety | CompTIA 3.8; Messer v1.70 p.43; private practice gap check | Present, p.43 | Laser Printer Maintenance | 3.8-B003 | Basic | N/A | Self-reviewed |
| Laser calibration | CompTIA 3.8; Messer v1.70 p.43 | Present, p.43 | Laser Printer Maintenance | 3.8-B004 | Basic | N/A | Self-reviewed |
| Laser cleaning methods | CompTIA 3.8; Messer v1.70 p.43; private practice gap check | Present, p.43 | Laser Printer Maintenance | 3.8-B005 | Basic | N/A | Self-reviewed |
| Inkjet cartridge and CMYK ink | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Inkjet Printer Maintenance | 3.8-B006, 3.8-C002 | Basic, Cloze | N/A; cartridge concept and acronym recall are distinct | Self-reviewed |
| Inkjet printhead integration | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Inkjet Printer Maintenance | 3.8-B007 | Basic | N/A | Self-reviewed |
| Inkjet printhead cleaning | CompTIA 3.8; Messer v1.70 p.44; private practice gap check | Present, p.44 | Inkjet Printer Maintenance | 3.8-B008 | Basic | N/A | Self-reviewed |
| Inkjet calibration | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Inkjet Printer Maintenance | 3.8-B009 | Basic | N/A | Self-reviewed |
| Inkjet jam clearing | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Inkjet Printer Maintenance | 3.8-B010 | Basic | N/A | Self-reviewed |
| Inkjet rollers and feeder | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Inkjet Printer Maintenance | 3.8-B011 | Basic | N/A | Self-reviewed |
| Thermal printer paper and heating element | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Thermal Printer Maintenance | 3.8-B012, 3.8-C003 | Basic, Cloze | N/A; paper purpose and term recall are distinct | Self-reviewed |
| Thermal feed assembly | CompTIA 3.8; Messer v1.70 p.44 | Present, p.44 | Thermal Printer Maintenance | 3.8-B013 | Basic | N/A | Self-reviewed |
| Thermal paper replacement | CompTIA 3.8; Messer v1.70 p.45; private practice gap check | Present, p.45 | Thermal Printer Maintenance | 3.8-B014 | Basic | N/A | Self-reviewed |
| Thermal heating-element cleaning | CompTIA 3.8; Messer v1.70 p.45 | Present, p.45 | Thermal Printer Maintenance | 3.8-B015 | Basic | N/A | Self-reviewed |
| Thermal debris removal and vacuum caution | CompTIA 3.8; Messer v1.70 p.45; private practice gap check | Present, p.45 | Thermal Printer Maintenance | 3.8-B016 | Basic | N/A | Self-reviewed |
| Impact printer printhead, ribbon, and multipart paper | CompTIA 3.8; Messer v1.70 p.45; private practice gap check | Present, p.45 | Impact Printer Maintenance | 3.8-B017, 3.8-B018, 3.8-C004, 3.8-C005 | Basic, Cloze | N/A; maintenance decisions and compact term recall are distinct | Self-reviewed |
| Impact paper replacement and tractor feed | CompTIA 3.8; Messer v1.70 p.45 | Present, p.45 | Impact Printer Maintenance | 3.8-B019 | Basic | N/A | Self-reviewed |
| Exact maintenance-kit part numbers, page-count thresholds, proprietary cartridge codes, printer service menus, detailed teardown procedures, and broad printer symptom triage | Messer v1.70 pp.43-45; adjacent Objective 5.6 | Present as examples/details or outside 3.8 scope | Scope Caveats | None | None | Study-guide-only or omitted; product-specific details and broad troubleshooting belong in documentation or Objective 5.6 | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.8-B002 | Laser maintenance-kit timing and contents are central to printer maintenance | Needs reviewer agreement |
| 3.8-B003 | Fuser heat is a safety-critical maintenance point | Needs reviewer agreement |
| 3.8-B005 | Safe toner cleaning is a common printer maintenance trap | Needs reviewer agreement |
| 3.8-B008 | Inkjet printhead cleaning is a core inkjet maintenance task | Needs reviewer agreement |
| 3.8-B010 | Clearing inkjet jams is explicit objective scope | Needs reviewer agreement |
| 3.8-B012 | Thermal paper distinction is foundational for thermal printers | Needs reviewer agreement |
| 3.8-B015 | Heating-element cleaning is explicit thermal maintenance scope | Needs reviewer agreement |
| 3.8-B017 | Ribbon replacement is a core impact-printer maintenance task | Needs reviewer agreement |
| 3.8-B019 | Tractor-feed alignment is core impact-printer paper maintenance | Needs reviewer agreement |
| 3.8-C002 | CMYK recall supports inkjet cartridge maintenance | Needs reviewer agreement |
| 3.8-C004 | Multipart paper recall supports impact-printer maintenance | Needs reviewer agreement |

## Omitted-concepts review

Omitted-concepts review is pending. The intentionally not-carded details are
exact maintenance-kit part numbers, page-count thresholds, proprietary
cartridge codes, printer service menus, detailed teardown procedures, and broad
printer symptom triage.

## Independent content review

Independent content review found one required fix: `3.8-B018` needed to test
the official impact printhead replacement maintenance action instead of only
explaining why the printhead is a wear item. The card was rewritten to cover
replacement caution, release mechanism use, heat safety, and replacing the
ribbon with the printhead for best output.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.8 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.8 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 43-45 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Initial card and no-card decisions recorded.
- [x] Official objective domain, number, full phrase, and bullet scope recorded in this checklist.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified maintenance decisions.
- [x] Cloze cards cover justified compact acronym and term recall.
- [x] No image cards created in this initial draft; printer component visuals can be revisited after text review.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 19 Basic, 5 Cloze, 0 Image.

## Review and build

- [ ] Omitted-concepts review completed.
- [x] Independent content review completed; required `3.8-B018` fix applied.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing was reported passed on 2026-07-11. Objective 3.8 has
no Image cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Tester | User-reported |
| Expected note count | 24 total notes: 19 Basic, 5 Cloze, 0 Image |
| Actual note count | Reported passed with expected counts |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.8 has no Image cards |
| Media rendering | Not applicable |
| Basic Hint column | Passed |
| Headers | Passed; TSV headers were not imported as notes |
| Card ID behavior | Passed; Card ID was first field and drove update behavior |
| HTML rendering | Passed |
| Cloze rendering | Passed |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import behavior | Passed; existing notes updated instead of duplicating |
| Final result | Passed on 2026-07-11 |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-11 | Initial Objective 3.8 draft and coverage decisions completed | Validation, build, omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Codex independent review | 2026-07-11 | One required content fix found for impact printhead replacement coverage | Rewrite `3.8-B018` as an action-oriented replacement maintenance card; completed | Changes completed |
| Manual Anki smoke test | 2026-07-11 | Basic and Cloze imports reported passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None | Passed |
