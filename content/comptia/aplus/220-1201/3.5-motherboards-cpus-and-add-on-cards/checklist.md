# Objective 3.5 completion checklist

**Objective status: READY FOR MAINTAINER ACCEPTANCE.** Objective 3.5 has
source-backed content, generated TSV output, completed omitted-concepts and
content review, passing automated verification, and a passing manual Anki smoke
test. It still needs maintainer acceptance.

## Official objective context

Domain 3.0 Hardware, Objective 3.5: Given a scenario, install and configure
motherboards, central processing units (CPUs), and add-on cards.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.5-motherboards-cpus-and-add-on-cards` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.5 is driven by the official `Given a scenario` wording. Cards focus
on practical installation and configuration choices for motherboard form
factors, connector types, compatibility, firmware settings, CPU architecture,
expansion cards, and cooling. The objective wording does not require separate
interview-style troubleshooting material.

## Objective-specific cautions

- Do not drift into Objective 3.6 power-supply selection except where Objective
  3.5 explicitly includes motherboard and PCIe power connectors.
- Do not drift into Objective 5.1 hardware troubleshooting symptoms or Objective
  5.6 printer troubleshooting.
- Do not over-card exact motherboard dimensions, socket model numbers, PCIe
  generation bandwidths, fan RPM values, or temperature thresholds.
- Treat vendor-specific firmware menu names as documentation lookup items, not
  universal flashcard facts.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ATX form factor use | CompTIA 3.5; Messer v1.70 p.34 | Present, p.34 | Motherboard Form Factors | 3.5-B001, 3.5-C001 | Basic, Cloze | N/A; scenario selection and acronym recall are distinct | Self-reviewed |
| microATX tradeoff | CompTIA 3.5; Messer v1.70 p.34 | Present, p.34 | Motherboard Form Factors | 3.5-B002 | Basic | N/A | Self-reviewed |
| ITX small-form-factor use | CompTIA 3.5; Messer v1.70 p.34 | Present, p.34 | Motherboard Form Factors | 3.5-B003 | Basic | N/A | Self-reviewed |
| PCI versus PCIe expansion slots | CompTIA 3.5; Messer v1.70 p.35 | Present, p.35 | Motherboard Connectors | 3.5-B004, 3.5-C002 | Basic, Cloze | N/A; comparison and acronym recall are distinct | Self-reviewed |
| Motherboard headers | CompTIA 3.5; Messer v1.70 p.35 | Present, p.35 | Motherboard Connectors | 3.5-B005 | Basic | N/A | Self-reviewed |
| Motherboard and PCIe power connectors | CompTIA 3.5; Messer v1.70 p.35 | Present, p.35 | Motherboard Connectors | 3.5-B006 | Basic | N/A | Self-reviewed |
| SATA and eSATA connector purposes | CompTIA 3.5; Messer v1.70 p.26 | Present, p.26 | Motherboard Connectors | 3.5-B007, 3.5-C003, 3.5-C004 | Basic, Cloze | N/A; connector choice and acronym recall are distinct | Self-reviewed |
| M.2 motherboard connector | CompTIA 3.5; Messer v1.70 p.32; private practice gap check | Present, p.32 | Motherboard Connectors | 3.5-B008 | Basic | N/A | Self-reviewed |
| CPU socket/vendor compatibility | CompTIA 3.5; Messer v1.70 p.35 | Present, p.35 | Motherboard Compatibility | 3.5-B009 | Basic | N/A | Self-reviewed |
| Multisocket motherboards | CompTIA 3.5; Messer v1.70 p.35 | Present, p.35 | Motherboard Compatibility | 3.5-B010 | Basic | N/A | Self-reviewed |
| BIOS/UEFI startup role | CompTIA 3.5; Messer v1.70 p.36 | Present, p.36 | BIOS and UEFI Settings | 3.5-C005, 3.5-C010 | Cloze | N/A | Self-reviewed |
| Boot options and boot order | CompTIA 3.5; Messer v1.70 p.36 | Present, p.36 | BIOS and UEFI Settings | 3.5-B011 | Basic | N/A | Self-reviewed |
| USB permissions | CompTIA 3.5; Messer v1.70 p.36 | Present, p.36 | BIOS and UEFI Settings | 3.5-B012 | Basic | N/A | Self-reviewed |
| Secure Boot | CompTIA 3.5; Messer v1.70 p.37; private practice gap check | Present, p.37 | BIOS and UEFI Settings | 3.5-B013 | Basic | N/A | Self-reviewed |
| Boot password versus BIOS/supervisor password | CompTIA 3.5; Messer v1.70 p.37; private practice gap check | Present, p.37 | BIOS and UEFI Settings | 3.5-B014 | Basic | N/A | Self-reviewed |
| Temperature monitoring and fan controls | CompTIA 3.5; Messer v1.70 pp.36-37 | Present, pp.36-37 | BIOS and UEFI Settings | 3.5-B015 | Basic | N/A | Self-reviewed |
| Virtualization support in firmware | CompTIA 3.5; Messer v1.70 p.37; private practice gap check | Present, p.37 | BIOS and UEFI Settings | 3.5-B016 | Basic | N/A | Self-reviewed |
| TPM local cryptographic support | CompTIA 3.5; Messer v1.70 pp.37-38; private practice gap check | Present, pp.37-38 | TPM, HSM, and Encryption Support | 3.5-B017, 3.5-C006 | Basic, Cloze | N/A; local-vs-central distinction and acronym recall are distinct | Self-reviewed |
| HSM centralized cryptographic support | CompTIA 3.5; Messer v1.70 p.38; private practice gap check | Present, p.38 | TPM, HSM, and Encryption Support | 3.5-B017, 3.5-C007 | Basic, Cloze | N/A; local-vs-central distinction and acronym recall are distinct | Self-reviewed |
| x86/x64 architecture | CompTIA 3.5; Messer v1.70 p.38 | Present, p.38 | CPU Architecture and Cores | 3.5-B018, 3.5-C009 | Basic, Cloze | N/A | Self-reviewed |
| ARM architecture | CompTIA 3.5; Messer v1.70 p.38; private practice gap check | Present, p.38 | CPU Architecture and Cores | 3.5-B018, 3.5-C008 | Basic, Cloze | N/A; architecture selection and acronym recall are distinct | Self-reviewed |
| Core configurations | CompTIA 3.5; Messer v1.70 p.38 | Present, p.38 | CPU Architecture and Cores | 3.5-B019 | Basic | N/A | Self-reviewed |
| Sound card, video card, capture card, and NIC purposes | CompTIA 3.5; Messer v1.70 pp.38-39; private practice gap check | Present, pp.38-39 | Expansion Cards | 3.5-B020, 3.5-B021, 3.5-B025, 3.5-C011 | Basic, Cloze | N/A | Self-reviewed |
| Expansion-card documentation and driver checks | Messer v1.70 p.39 | Present, p.39 | Expansion Cards | 3.5-B022 | Basic | N/A | Self-reviewed |
| Fans, heat sinks, thermal paste/pads, and liquid cooling | CompTIA 3.5; Messer v1.70 p.39; private practice gap check | Present, p.39 | Cooling | 3.5-B023, 3.5-B024 | Basic | N/A | Self-reviewed |
| Exact board dimensions, socket part numbers, PCIe generation speeds, fan RPM ratings, temperature thresholds, and vendor-specific firmware key sequences | Messer v1.70 pp.34-39 | Present as examples/details, pp.34-39 | Scope Caveats | None | None | Study-guide-only; product-specific details are better checked in system documentation | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.5-B001 | Form factor selection is a core build-planning decision | Content review agreed |
| 3.5-B004 | PCI versus PCIe distinguishes old and modern expansion interfaces | Content review agreed |
| 3.5-B005 | Headers are a common motherboard-connection recognition point | Content review agreed |
| 3.5-B009 | CPU socket compatibility is a hard install boundary | Content review agreed |
| 3.5-B013 | Secure Boot is a core UEFI security setting | Content review agreed |
| 3.5-B016 | Firmware virtualization support is a common VM enablement requirement | Content review agreed |
| 3.5-B017 | TPM versus HSM is a core encryption-support distinction | Content review agreed |
| 3.5-B018 | CPU architecture selection affects OS/device compatibility and power use | Content review agreed |
| 3.5-B020 | Expansion-card selection is an explicit objective item | Content review agreed |
| 3.5-B025 | Video card selection is an explicit objective item | Content review agreed |
| 3.5-B023 | Thermal interface material is a common cooling concept | Content review agreed |
| 3.5-C006 | TPM acronym recall supports firmware/security configuration | Content review agreed |
| 3.5-C008 | ARM acronym recall supports architecture selection | Content review agreed |

## Omitted-concepts review

Omitted-concepts review completed on 2026-07-11. The intentionally not-carded
details are exact board dimensions, socket part numbers, PCIe generation
speeds, fan RPM ratings, temperature thresholds, and vendor-specific firmware
key sequences. These remain study-guide-only because they are product-specific
and should be checked in system documentation. No official-scope,
source-supported, stable, practice-test-relevant concept was left without
either a card or a specific study-guide-only reason.

## Independent content review

Initial content review completed on 2026-07-08. Result: NO-GO for Anki smoke
test until required fixes were completed. Required fixes were completed on
2026-07-08: SATA/eSATA and M.2 Messer page citations were corrected, header
wording was narrowed to approved-source support, direct video-card purpose
coverage was added, card counts were corrected, and TSV output was regenerated.
Clean content-review recheck completed on 2026-07-11. Result: GO for manual
Anki smoke test. The recheck confirmed the citation fixes, narrowed header
wording, direct video-card coverage, generated TSV counts, and generated tags.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.5 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.5 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 34-39 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Initial card and no-card decisions recorded.
- [x] Official objective domain, number, full phrase, and bullet scope recorded in this checklist.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified motherboard, CPU, firmware, expansion-card, and cooling decisions.
- [x] Cloze cards cover justified compact acronym and term recall.
- [x] No image cards created in this initial draft; motherboard component recognition may be revisited after text review.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 25 Basic, 11 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] `python scripts/validate.py` passes without unexplained warnings after required fixes.
- [x] `python scripts/build.py` passes and generated output is regenerated after required fixes.
- [x] `pytest` and Ruff checks pass after required fixes.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing was reported passed on 2026-07-11. Objective 3.5 has
no Image cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Tester | User-reported |
| Expected note count | 36 total notes: 25 Basic, 11 Cloze, 0 Image |
| Actual note count | Reported passed with expected counts |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.5 has no Image cards |
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
| Self-review | 2026-07-08 | Initial Objective 3.5 draft and coverage decisions completed | Validation, build, omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Content review | 2026-07-08 | NO-GO for Anki smoke test; required source/citation and coverage fixes identified | Correct SATA/eSATA and M.2 citations; narrow header wording; add direct video-card card; correct counts | Fixes completed; needs recheck |
| Omitted-concepts review | 2026-07-11 | Omitted exact dimensions, socket part numbers, PCIe generation speeds, fan RPM ratings, temperature thresholds, and vendor-specific firmware key sequences are acceptable as study-guide-only | None | Approved for content review |
| Content review recheck | 2026-07-11 | GO for manual Anki smoke test after required fixes | None | Approved for Anki smoke test |
| Manual Anki smoke test | 2026-07-11 | Basic and Cloze imports reported passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None | Passed |
