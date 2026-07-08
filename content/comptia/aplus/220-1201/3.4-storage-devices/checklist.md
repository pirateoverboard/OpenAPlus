# Objective 3.4 completion checklist

**Objective status: READY FOR MAINTAINER ACCEPTANCE.** Objective 3.4 has
source-backed draft content, generated TSV output, completed omitted-concepts
and content review, passing automated verification, and a passing manual Anki
smoke test. It still needs maintainer acceptance.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.4-storage-devices` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.4 is treated as standard objective content. Cards focus on storage
device comparison, storage-interface compatibility, removable media, and RAID
configuration tradeoffs. The objective is not authored in Domain 5
troubleshooting/interview style.

## Objective-specific cautions

- Do not drift into Objective 5.2 troubleshooting symptoms and recovery steps;
  this objective compares storage devices and configurations.
- Do not over-card exact throughput, latency, or capacity figures because those
  are platform-specific and change across standards and products.
- Do not imply that M.2 always means NVMe; M.2 is a physical interface and must
  be checked against system documentation.
- Do not present RAID as backup; RAID improves availability for some drive
  failures, while backups protect recoverability.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Storage as non-volatile retention compared with RAM | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Hard drives; Solid-state drives | 3.4-B001 | Basic | N/A | Self-reviewed |
| HDD magnetic storage and moving parts | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Hard drives | 3.4-B001 | Basic | N/A | Self-reviewed |
| HDD spindle speed as a comparison characteristic | CompTIA 3.4; Messer v1.70 p.33 | Present, p.33 | Hard drives | 3.4-C001 | Cloze | N/A | Self-reviewed |
| HDD 2.5-inch and 3.5-inch form factors | CompTIA 3.4; Messer v1.70 p.32; private practice gap check | Present, p.32 | Hard drives | 3.4-B002 | Basic | N/A | Self-reviewed |
| SSD non-volatile flash and no moving parts | CompTIA 3.4; Messer v1.70 p.32; private practice gap check | Present, p.32 | Solid-state drives | 3.4-B001, 3.4-C002 | Basic, Cloze | N/A; comparison and acronym recall are distinct | Self-reviewed |
| SATA SSD interface | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Interfaces and form factors | 3.4-B003, 3.4-C004 | Basic, Cloze | N/A; interface selection and acronym recall are distinct | Self-reviewed |
| NVMe SSD interface/protocol | CompTIA 3.4; Messer v1.70 p.32; private practice gap check | Present, p.32 | Interfaces and form factors | 3.4-B003, 3.4-C003 | Basic, Cloze | N/A; interface selection and acronym recall are distinct | Self-reviewed |
| PCIe storage interface | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Interfaces and form factors | 3.4-B004 | Basic | N/A | Self-reviewed |
| M.2 form factor and key/support compatibility | CompTIA 3.4; Messer v1.70 p.32; private practice gap check | Present, p.32 | Interfaces and form factors | 3.4-B005 | Basic | N/A | Self-reviewed |
| SAS storage interface | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Interfaces and form factors | 3.4-B006, 3.4-C005 | Basic, Cloze | N/A; use case and acronym recall are distinct | Self-reviewed |
| mSATA form factor | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Interfaces and form factors | 3.4-B007, 3.4-C006 | Basic, Cloze | N/A; form-factor recognition and acronym recall are distinct | Self-reviewed |
| Flash drives and memory cards as removable flash storage | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Removable and optical storage | 3.4-B008 | Basic | N/A | Self-reviewed |
| Optical drives | CompTIA 3.4; Messer v1.70 p.32 | Present, p.32 | Removable and optical storage | 3.4-B009 | Basic | N/A | Self-reviewed |
| RAID is not backup | CompTIA 3.4; Messer v1.70 p.33; private practice gap check | Present, p.33 | RAID configurations | 3.4-B010, 3.4-C007 | Basic, Cloze | N/A; conceptual trap and acronym recall are distinct | Self-reviewed |
| RAID 0 striping | CompTIA 3.4; Messer v1.70 p.33; private practice gap check | Present, p.33 | RAID configurations | 3.4-B011 | Basic | N/A | Self-reviewed |
| RAID 1 mirroring | CompTIA 3.4; Messer v1.70 p.33; private practice gap check | Present, p.33 | RAID configurations | 3.4-B012 | Basic | N/A | Self-reviewed |
| RAID 5 striping with parity | CompTIA 3.4; Messer v1.70 pp.33-34; private practice gap check | Present, pp.33-34 | RAID configurations | 3.4-B013 | Basic | N/A | Self-reviewed |
| RAID 6 dual parity | CompTIA 3.4; Messer v1.70 p.34; private practice gap check | Present, p.34 | RAID configurations | 3.4-B014 | Basic | N/A | Self-reviewed |
| RAID 10 stripe of mirrors | CompTIA 3.4; Messer v1.70 p.34; private practice gap check | Present, p.34 | RAID configurations | 3.4-B015 | Basic | N/A | Self-reviewed |
| Exact HDD latency table, SSD benchmark numbers, optical capacities, and full M.2 keying matrix | Messer v1.70 pp.32-33 | Present as examples/details, pp.32-33 | Intentionally limited details | None | None | Study-guide-only; platform- or product-specific detail is better checked in documentation | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.4-B001 | HDD versus SSD is a foundational storage-device comparison | Content review agreed |
| 3.4-B003 | SATA versus NVMe is a common SSD selection and compatibility distinction | Content review agreed |
| 3.4-B005 | M.2 versus NVMe is a common exam trap and practical upgrade issue | Content review agreed |
| 3.4-B010 | RAID is not backup is a core availability-versus-recoverability distinction | Content review agreed |
| 3.4-B011 | RAID 0 has high performance but no redundancy | Content review agreed |
| 3.4-B012 | RAID 1 mirroring is a core redundancy concept | Content review agreed |
| 3.4-B013 | RAID 5 parity is a common redundancy/capacity tradeoff | Content review agreed |
| 3.4-B014 | RAID 6 adds two-drive failure tolerance | Content review agreed |
| 3.4-B015 | RAID 10 combines striping and mirroring | Content review agreed |
| 3.4-C003 | NVMe acronym recall supports interface selection | Content review agreed |
| 3.4-C007 | RAID acronym recall supports the drive-configuration objective item | Content review agreed |

## Omitted-concepts review

Omitted-concepts review completed on 2026-07-08. The only intentionally
not-carded concept group is exact HDD latency tables, SSD benchmark numbers,
optical capacities, flash-memory electrical details, and full M.2 keying
matrices. These remain study-guide-only because they are platform- or
product-specific details better checked in system documentation. No
official-scope, source-supported, stable, practice-test-relevant concept was
left without either a card or a specific study-guide-only reason.

## Independent content review

Content review completed on 2026-07-08 using the standard-objective review
criteria. Result: GO for manual Anki smoke test after one required fix. The fix
was to align the SATA and mSATA acronym Cloze cards and study-guide wording
with the official CompTIA glossary expansions; those changes were completed and
the TSV output was regenerated. No remaining blockers were identified before
the manual Anki smoke-test gate.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.4 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.4 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 32-34 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Card and no-card decisions recorded before authoring.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified device comparison, interface selection, removable storage, and RAID decisions.
- [x] Cloze cards cover justified compact acronym and measurement recall.
- [x] No image cards created in this initial draft because the text cards cover the exam decision points without requiring committed media.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 15 Basic, 7 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing was reported passed on 2026-07-08. Objective 3.4 has
no Image cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Tester | User-reported |
| Expected note count | 22 total notes: 15 Basic, 7 Cloze, 0 Image |
| Actual note count | Reported passed with expected counts |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.4 has no Image cards |
| Media rendering | Not applicable |
| Basic Hint column | Passed |
| Headers | Passed; TSV headers were not imported as notes |
| Card ID behavior | Passed; Card ID was first field and drove update behavior |
| HTML rendering | Passed |
| Cloze rendering | Passed |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import behavior | Passed; existing notes updated instead of duplicating |
| Final result | Passed on 2026-07-08 |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-08 | Initial Objective 3.4 draft and coverage decisions completed | Omitted-concepts review, independent review, verification, and any required Anki smoke test | Completed |
| Omitted-concepts review | 2026-07-08 | Omitted exact performance tables, capacities, electrical details, and full M.2 keying matrices are acceptable as study-guide-only | None | Approved for content review |
| Content review | 2026-07-08 | GO for manual Anki smoke test after acronym wording fix | Align SATA and mSATA acronym wording to official glossary; completed | Approved for Anki smoke test |
| Manual Anki smoke test | 2026-07-08 | Basic and Cloze imports reported passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None | Passed |
