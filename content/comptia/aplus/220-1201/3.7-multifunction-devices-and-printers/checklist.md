# Objective 3.7 completion checklist

**Objective status: READY FOR MAINTAINER ACCEPTANCE.** Objective 3.7 has
source-backed content, generated TSV output, completed omitted-concepts and
content review, passing automated verification, and a passing manual Anki smoke
test. It still needs maintainer acceptance.

## Official objective context

Domain 3.0 Hardware, Objective 3.7: Given a scenario, deploy and configure
multifunction devices/printers and settings.

Official bullet scope:

- Properly unbox device and consider set-up location
- Use appropriate drivers for a given operating system
- Printer Control Language (PCL) vs. postscript
- Firmware
- Device connectivity: USB, Ethernet, wireless
- Public/shared devices: printer share, print server
- Configuration settings: duplex, orientation, tray settings, quality
- Security: user authentication, badging, audit logs, secured prints
- Network scan services: email, SMB, cloud services
- Automatic document feeder (ADF)/flatbed scanner

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.7-multifunction-devices-and-printers` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.7 is driven by the official `Given a scenario` wording. Cards focus
on practical deployment and configuration choices for multifunction devices,
printer drivers, page description languages, firmware, connectivity, sharing,
settings, security, scan services, and scanning hardware. The objective wording
does not require separate interview-style troubleshooting material.

## Objective-specific cautions

- Do not drift into Objective 3.8 printer maintenance tasks such as toner,
  fusers, rollers, print heads, ribbons, or thermal paper replacement.
- Do not drift into Objective 5.6 printer troubleshooting symptoms except where
  a configuration choice directly explains deployment behavior.
- Do not over-card vendor-specific driver package names, firmware menus,
  proprietary cloud setup steps, exact printer console paths, or features
  outside the official 3.7 scope.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Multifunction device role | CompTIA 3.7; Messer v1.70 p.41 | Present, p.41 | Device Role and Placement | 3.7-B001, 3.7-C001 | Basic, Cloze | N/A; role and acronym recall are distinct | Self-reviewed |
| Unboxing and setup location | CompTIA 3.7; Messer v1.70 p.41 | Present, p.41 | Device Role and Placement | 3.7-B002 | Basic | N/A | Self-reviewed |
| OS-specific printer drivers | CompTIA 3.7; Messer v1.70 p.41; private practice gap check | Present, p.41 | Drivers and Page Description Languages | 3.7-B003 | Basic | N/A | Self-reviewed |
| PCL versus PostScript driver matching | CompTIA 3.7; Messer v1.70 p.41; private practice gap check | Present, p.41 | Drivers and Page Description Languages | 3.7-B004, 3.7-C002 | Basic, Cloze | N/A; mismatch reasoning and acronym recall are distinct | Self-reviewed |
| Firmware role and update cautions | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Firmware | 3.7-B005 | Basic | N/A | Self-reviewed |
| USB direct connectivity | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Device Connectivity | 3.7-B006 | Basic | N/A | Self-reviewed |
| Ethernet wired network connectivity | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Device Connectivity | 3.7-B007 | Basic | N/A | Self-reviewed |
| Wireless connectivity choices | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Device Connectivity | 3.7-B008 | Basic | N/A | Self-reviewed |
| Printer share versus print server | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | Public and Shared Devices | 3.7-B009 | Basic | N/A | Self-reviewed |
| Duplex printing | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | Configuration Settings | 3.7-B010, 3.7-C003 | Basic, Cloze | N/A; scenario choice and term recall are distinct | Self-reviewed |
| Orientation setting | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Configuration Settings | 3.7-B011 | Basic | N/A | Self-reviewed |
| Tray settings | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | Configuration Settings | 3.7-B012 | Basic | N/A | Self-reviewed |
| Quality settings | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Configuration Settings | 3.7-B013 | Basic | N/A | Self-reviewed |
| User authentication and permissions | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Security | 3.7-B014 | Basic | N/A | Self-reviewed |
| Badging and secured prints | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | Security | 3.7-B015 | Basic | N/A | Self-reviewed |
| Audit logs | CompTIA 3.7; Messer v1.70 p.42 | Present, p.42 | Security | 3.7-B016 | Basic | N/A | Self-reviewed |
| Network scan services: email, SMB, cloud | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | Network Scan Services | 3.7-B017, 3.7-C004 | Basic, Cloze | N/A; scan destination choice and acronym recall are distinct | Self-reviewed |
| ADF versus flatbed scanning | CompTIA 3.7; Messer v1.70 p.42; private practice gap check | Present, p.42 | ADF and Flatbed Scanning | 3.7-B018, 3.7-C005 | Basic, Cloze | N/A; selection and acronym recall are distinct | Self-reviewed |
| Exact driver package names, firmware menus, cloud-service setup steps, printer console paths, IPP/AirPrint details, finishing/collation features, and maintenance procedures | Messer v1.70 pp.41-42; adjacent objectives | Present as examples/details or outside 3.7 scope | Scope Caveats | None | None | Study-guide-only or omitted; product-specific details, non-3.7 features, and maintenance/troubleshooting tasks belong in documentation or later objectives | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.7-B003 | Correct printer driver selection is central to deployment | Needs reviewer agreement |
| 3.7-B004 | PCL/PostScript mismatch is a common deployment trap | Needs reviewer agreement |
| 3.7-B005 | Firmware affects device startup, network behavior, and compatibility | Needs reviewer agreement |
| 3.7-B009 | Printer share versus print server is a core shared-device distinction | Needs reviewer agreement |
| 3.7-B010 | Duplex is an explicit configuration setting and common user request | Needs reviewer agreement |
| 3.7-B012 | Tray settings are an explicit setting and common deployment issue | Needs reviewer agreement |
| 3.7-B015 | Badging/secured print is a practical shared-printer security control | Needs reviewer agreement |
| 3.7-B017 | Network scan destination selection is explicit objective scope | Needs reviewer agreement |
| 3.7-B018 | ADF versus flatbed is an explicit scanner-selection decision | Needs reviewer agreement |
| 3.7-C002 | PCL acronym recall supports driver-language matching | Needs reviewer agreement |
| 3.7-C005 | ADF acronym recall supports scanner feature selection | Needs reviewer agreement |

## Omitted-concepts review

Omitted-concepts review completed on 2026-07-11. The intentionally not-carded
details are exact driver package names, firmware menus, cloud-service setup
steps, printer console paths, IPP/AirPrint details, finishing/collation
features, and maintenance procedures. These remain study-guide-only or omitted
because they are product-specific, volatile, unsupported as official 3.7 scope,
or better covered in later printer objectives. No official-scope,
source-supported, stable, practice-test-relevant concept was left without
either a card or a specific study-guide-only reason.

## Independent content review

Initial independent content review completed on 2026-07-11. Result: NO-GO for
Anki smoke test until required fixes were completed. Required fixes were
completed on 2026-07-11: finishing/collation references were removed or
narrowed to official 3.7 settings, checklist/changelog review records were
updated, and generated TSV output was regenerated. Manual Anki smoke test
passed after required fixes.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.7 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.7 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 41-42 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Initial card and no-card decisions recorded.
- [x] Official objective domain, number, full phrase, and bullet scope recorded in this checklist.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified deployment and configuration decisions.
- [x] Cloze cards cover justified compact acronym and term recall.
- [x] No image cards created in this initial draft; device UI or connector visuals can be revisited after text review.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 18 Basic, 5 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing was reported passed on 2026-07-11. Objective 3.7 has
no Image cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Tester | User-reported |
| Expected note count | 23 total notes: 18 Basic, 5 Cloze, 0 Image |
| Actual note count | Reported passed with expected counts |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.7 has no Image cards |
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
| Self-review | 2026-07-11 | Initial Objective 3.7 draft and coverage decisions completed | Validation, build, omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Content review | 2026-07-11 | NO-GO for Anki smoke test; required scope-wording and review-record fixes identified | Remove or narrow finishing/collation references; update verification/review records | Fixes completed; needs recheck |
| Manual Anki smoke test | 2026-07-11 | Basic and Cloze imports reported passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None | Passed |
