# Objective 3.6 completion checklist

**Objective status: READY FOR MAINTAINER ACCEPTANCE.** Objective 3.6 has
source-backed content, generated TSV output, completed omitted-concepts and
content review, passing automated verification, and a passing manual Anki smoke
test. It still needs maintainer acceptance.

## Official objective context

Domain 3.0 Hardware, Objective 3.6: Given a scenario, install the appropriate
power supply.

Official bullet scope:

- Input 110-120 VAC vs. 220-240 VAC
- Output 3.3V vs. 5V vs. 12V
- 20+4 pin motherboard connector
- Redundant power supply
- Modular power supply
- Wattage rating
- Energy efficiency

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.6-power-supplies` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.6 is driven by the official `Given a scenario` wording. Cards focus
on practical power-supply selection and installation decisions: correct input
voltage, DC output use, 20+4-pin motherboard power, redundancy, modular
cabling, wattage sizing, and efficiency. The objective wording does not require
separate interview-style troubleshooting material.

## Objective-specific cautions

- Do not drift into Objective 3.5 motherboard, CPU, add-on-card, or cooling
  installation except where power-supply selection depends on connector and
  component load.
- Do not drift into Objective 5.1 hardware troubleshooting symptoms beyond
  installation and selection decisions.
- Do not over-card exact efficiency certification levels, proprietary form
  factors, vendor-specific modular cable pinouts, or a universal wattage number
  for all systems.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Electrical safety while working around power supplies | CompTIA 3.6; Messer v1.70 p.40 | Present, p.40 | Safety and Conversion | 3.6-B001 | Basic | N/A | Self-reviewed |
| AC-to-DC conversion role | CompTIA 3.6; Messer v1.70 p.40 | Present, p.40 | Safety and Conversion | 3.6-B002 | Basic | N/A | Self-reviewed |
| Input voltage selection, 110-120 VAC vs. 220-240 VAC | CompTIA 3.6; Messer v1.70 p.40; private practice gap check | Present, p.40 | Safety and Conversion | 3.6-B003, 3.6-C001 | Basic, Cloze | N/A; selection and abbreviation recall are distinct | Self-reviewed |
| Auto-voltage versus manual input switching | CompTIA 3.6; Messer v1.70 p.40; private practice gap check | Present, p.40 | Safety and Conversion | 3.6-B004 | Basic | N/A | Self-reviewed |
| Output 3.3 V, 5 V, and 12 V rails | CompTIA 3.6; Messer v1.70 p.40; private practice gap check | Present, p.40 | Output Voltages | 3.6-B005, 3.6-B006, 3.6-C003 | Basic, Cloze | N/A | Self-reviewed |
| 20+4-pin motherboard connector | CompTIA 3.6; Messer v1.70 p.40; private practice gap check | Present, p.40 | Motherboard Power Connector | 3.6-B007, 3.6-C004 | Basic, Cloze | N/A | Self-reviewed |
| Redundant power supply purpose | CompTIA 3.6; Messer v1.70 p.40; private practice gap check | Present, p.40 | Redundant Power Supplies | 3.6-B008 | Basic | N/A | Self-reviewed |
| Modular versus fixed power-supply cabling | CompTIA 3.6; Messer v1.70 p.41; private practice gap check | Present, p.41 | Modular and Fixed Cabling | 3.6-B009 | Basic | N/A | Self-reviewed |
| Wattage rating and sizing | CompTIA 3.6; Messer v1.70 pp.40-41; private practice gap check | Present, pp.40-41 | Wattage Rating | 3.6-B010, 3.6-B011, 3.6-C005 | Basic, Cloze | N/A; sizing decisions and formula recall are distinct | Self-reviewed |
| Energy efficiency | CompTIA 3.6; Messer v1.70 p.41 | Present, p.41 | Energy Efficiency | 3.6-B012 | Basic | N/A | Self-reviewed |
| Exact efficiency certification tier names, proprietary PSU dimensions, vendor-specific modular cable pinouts, exact rail amperage tables, and universal wattage recommendations | Messer v1.70 pp.40-41 | Present as details/examples, pp.40-41 | Scope Caveats | None | None | Study-guide-only; exact values and proprietary details should be verified in product documentation | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.6-B003 | Input voltage mismatch can damage equipment or prevent operation | Needs reviewer agreement |
| 3.6-B004 | Auto-voltage versus manual switching is a core install decision | Needs reviewer agreement |
| 3.6-B005 | Output rails are explicit objective scope and common power-selection knowledge | Needs reviewer agreement |
| 3.6-B007 | 20+4-pin motherboard power is an explicit connector requirement | Needs reviewer agreement |
| 3.6-B008 | Redundancy is the key server availability distinction | Needs reviewer agreement |
| 3.6-B009 | Modular cabling is an explicit objective item and affects installation | Needs reviewer agreement |
| 3.6-B010 | Wattage sizing is central to choosing an appropriate PSU | Needs reviewer agreement |
| 3.6-B012 | Efficiency affects heat, cost, and PSU selection | Needs reviewer agreement |
| 3.6-C003 | 3.3 V, 5 V, and 12 V output recall is explicit objective scope | Needs reviewer agreement |

## Omitted-concepts review

Omitted-concepts review completed on 2026-07-11. The intentionally not-carded
details are exact efficiency certification tier names, proprietary PSU
dimensions, vendor-specific modular cable pinouts, exact rail amperage tables,
and universal wattage recommendations. These remain study-guide-only or omitted
because they are product-specific, volatile, unsupported as universal facts, or
better verified in product documentation. No official-scope, source-supported,
stable, practice-test-relevant concept was left without either a card or a
specific study-guide-only reason.

## Independent content review

Initial independent content review completed on 2026-07-11. Result: NO-GO for
Anki smoke test until required fixes were completed. Required fixes were
completed on 2026-07-11: duplicate AC-to-DC Cloze coverage was removed, the
study-guide 5 V wording was narrowed to approved-source support, and generated
TSV output was regenerated. Manual Anki smoke test passed after required fixes.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.6 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.6 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 40-41 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Initial card and no-card decisions recorded.
- [x] Official objective domain, number, full phrase, and bullet scope recorded in this checklist.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified power-supply selection and installation decisions.
- [x] Cloze cards cover justified compact abbreviation, connector, rail, and formula recall.
- [x] No image cards created in this initial draft; connector recognition can be revisited after text review.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 12 Basic, 4 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing was reported passed on 2026-07-11. Objective 3.6 has
no Image cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Tester | User-reported |
| Expected note count | 16 total notes: 12 Basic, 4 Cloze, 0 Image |
| Actual note count | Reported passed with expected counts |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.6 has no Image cards |
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
| Self-review | 2026-07-11 | Initial Objective 3.6 draft and coverage decisions completed | Validation, build, omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Content review | 2026-07-11 | NO-GO for Anki smoke test; required duplicate-card and source-wording fixes identified | Delete duplicate AC-to-DC Cloze card; narrow unsupported 5 V wording; update verification record | Fixes completed; needs recheck |
| Manual Anki smoke test | 2026-07-11 | Basic and Cloze imports reported passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None | Passed |
