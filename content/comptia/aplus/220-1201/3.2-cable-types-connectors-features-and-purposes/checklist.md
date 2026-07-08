# Objective 3.2 completion checklist

**Objective status: DRAFT.** Objective 3.2 has source-backed draft content,
generated output after build, and a passing manual Anki smoke test after the
Basic/Cloze redundancy cleanup, but still needs final independent-review and
acceptance records before acceptance.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.2-cable-types-connectors-features-and-purposes` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.2 is treated as standard objective content. Cards focus on choosing
or identifying basic cable families, connector types, features, and purposes.
The objective is not authored in Domain 5 troubleshooting/interview style.

## Objective-specific cautions

- Do not drift into Objective 3.4 storage-device characteristics beyond SATA
  and eSATA cabling.
- Do not over-card exact cable speed, distance, revision, or pin-color tables
  unless they are stable and clearly useful for A+ recall.
- Do not create cards for every possible adapter combination; focus on the
  adapter-versus-converter distinction and common examples.
- Keep connector visuals original, generic, or license-reviewed Wikimedia
  Commons photos with attribution metadata. Do not copy vendor diagrams,
  screenshots, proprietary source layouts, or private-source examples.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cable categories and Ethernet suitability | CompTIA 3.2; Messer v1.70 p.23 | Present, p.23 | Network cables | 3.2-C001 | Cloze | N/A | Self-reviewed |
| T568A/T568B termination standards | CompTIA 3.2; Messer v1.70 p.24 | Present, p.24 | Network cables | 3.2-C002 | Cloze | N/A; exact color order left study-guide-only | Self-reviewed |
| UTP vs STP | CompTIA 3.2; Messer v1.70 p.23 | Present, p.23 | Network cables | 3.2-B001, 3.2-C003 | Basic, Cloze | N/A; comparison and acronym recall are distinct | Self-reviewed |
| Direct-burial STP | CompTIA 3.2; Messer v1.70 p.23 | Present, p.23 | Network cables | 3.2-B002 | Basic | N/A | Self-reviewed |
| Plenum-rated cable | CompTIA 3.2; Messer v1.70 p.23 | Present, p.23 | Network cables | 3.2-B003 | Basic | Redundant Cloze card deleted after Anki smoke-test redundancy review; Basic scenario covers the installation decision | Self-reviewed |
| Coaxial cable and F-type connector | CompTIA 3.2; Messer v1.70 pp.23, 28 | Present, pp.23, 28 | Network cables; Connector recognition | 3.2-B004 | Basic | N/A | Self-reviewed |
| Single-mode vs multimode fiber | CompTIA 3.2; Messer v1.70 p.24 | Present, p.24 | Network cables | 3.2-B005 | Basic | Redundant Cloze card deleted after Anki smoke-test redundancy review; Basic card covers the distance-selection decision | Self-reviewed |
| USB 2.0 and USB 3.0 peripheral use | CompTIA 3.2; Messer v1.70 p.25 | Present, p.25 | Peripheral cables | 3.2-C006 | Cloze | N/A | Self-reviewed |
| USB connector recognition | CompTIA 3.2; Messer v1.70 pp.25, 28; Wikimedia Commons source metadata in `docs/image-sources/3.2-cable-types-connectors-features-and-purposes.md` | Present, pp.25, 28 | Peripheral cables; Connector recognition | 3.2-I003, 3.2-I004, 3.2-I005, 3.2-I006, 3.2-I007 | Image | N/A; visual connector recognition is useful for this objective | Self-reviewed after Wikimedia repair |
| USB-C as connector, not protocol | CompTIA 3.2; Messer v1.70 pp.25-26, 28 | Present, pp.25-26, 28 | Peripheral cables; Video cables | 3.2-B006 | Basic | Redundant Cloze card deleted after Anki smoke-test redundancy review; Basic card covers the common connector-versus-protocol trap | Self-reviewed |
| Thunderbolt over USB-C | CompTIA 3.2; Messer v1.70 p.25 | Present, p.25 | Peripheral cables | 3.2-B007 | Basic | N/A | Self-reviewed |
| Serial and DB9 console use | CompTIA 3.2; Messer v1.70 pp.25, 28 | Present, pp.25, 28 | Peripheral cables; Connector recognition | 3.2-B008 | Basic | Redundant Cloze card deleted after Anki smoke-test redundancy review; Basic card covers practical console-use recognition | Self-reviewed |
| HDMI and DisplayPort digital video | CompTIA 3.2; Messer v1.70 p.26 | Present, p.26 | Video cables | 3.2-B009, 3.2-C009 | Basic, Cloze | N/A | Self-reviewed |
| DVI and VGA video distinctions | CompTIA 3.2; Messer v1.70 p.26 | Present, p.26 | Video cables | 3.2-B010, 3.2-C010 | Basic, Cloze | N/A | Self-reviewed |
| SATA and eSATA cabling | CompTIA 3.2; Messer v1.70 p.27 | Present, p.27 | Hard drive cables | 3.2-B011 | Basic | Redundant Cloze card deleted after Anki smoke-test redundancy review; Basic card covers the internal-versus-external purpose distinction | Self-reviewed |
| Adapter vs converter | CompTIA 3.2; Messer v1.70 p.27 | Present, p.27 | Adapters and converters | 3.2-B012 | Basic | N/A | Self-reviewed |
| RJ45 vs RJ11 | CompTIA 3.2; Messer v1.70 p.28 | Present, p.28 | Connector recognition | 3.2-B013, 3.2-I001 | Basic, Image | N/A; purpose comparison and visual recognition are distinct | Self-reviewed |
| Punchdown block | CompTIA 3.2; Messer v1.70 p.28 | Present, p.28 | Connector recognition | 3.2-B014 | Basic | N/A | Self-reviewed |
| ST, SC, and LC fiber connectors | CompTIA 3.2; Messer v1.70 p.29 | Present, p.29 | Connector recognition | 3.2-C012, 3.2-I002 | Cloze, Image | N/A; name recall and visual lock-style recognition are distinct | Self-reviewed |
| Lightning and Molex connector recognition | CompTIA 3.2; Messer v1.70 p.28 | Present, p.28 | Connector recognition | None | None | Study-guide-only; active cards would duplicate connector-list memorization without a stronger applied decision | Self-reviewed |
| Exact T568A/T568B color order | Messer v1.70 p.24 | Present, p.24 | Intentionally limited detail | None | None | Study-guide-only; detailed pin-color memorization is lower value than recognizing the standards and consistent termination requirement | Self-reviewed |
| USB and Thunderbolt revision speed tables | Messer v1.70 p.25 | Present, p.25 | Intentionally limited detail | None | None | Study-guide-only; volatile/revision-heavy detail better checked against device specifications | Self-reviewed |
| Full video bandwidth and distance tables | Messer v1.70 p.26 | Present, p.26 | Intentionally limited detail | None | None | Study-guide-only; exact mode support depends on cable, device, and revision | Self-reviewed |
| Every possible adapter pairing | Messer v1.70 p.27 | Examples present, p.27 | Intentionally limited detail | None | None | Study-guide-only; adapter-versus-converter principle is carded instead | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.2-B001 | UTP versus STP is a foundational cable-selection distinction | Self-review; needs independent agreement |
| 3.2-B003 | Plenum-rated cable is a common installation/environment exam distinction | Self-review; needs independent agreement |
| 3.2-B005 | Single-mode versus multimode is a core fiber selection concept | Self-review; needs independent agreement |
| 3.2-B006 | USB-C connector-versus-protocol confusion is a common exam trap | Self-review; needs independent agreement |
| 3.2-B007 | Thunderbolt over USB-C is a common connector-versus-signal distinction | Self-review; needs independent agreement |
| 3.2-B012 | Adapter versus converter is practical and commonly tested | Self-review; needs independent agreement |
| 3.2-B013 | RJ45 versus RJ11 is foundational connector recognition | Self-review; needs independent agreement |
| 3.2-I001 | Visual recognition of RJ45 versus RJ11 reinforces a common connector distinction | Self-review; needs independent agreement |
| 3.2-I002 | Visual recognition of fiber connector lock styles supports the connector-type objective | Self-review; needs independent agreement |
| 3.2-I007 | USB-C recognition is foundational and reinforces the connector-versus-protocol exam trap | Self-review; needs independent agreement |

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.2 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.2 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 22-29 reviewed privately for validation and page citations.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, image, study-guide-only, and omitted decisions recorded.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified cable-selection, connector-purpose, and adapter/converter decisions.
- [x] Cloze cards cover compact standards, acronym, and connector recall.
- [x] Non-USB Image cards use original simplified SVGs for useful connector recognition.
- [x] USB Image cards use reviewed Wikimedia Commons photo-derived wrappers with source, author, license, and attribution metadata recorded.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] Manual Anki smoke test failure reviewed: Basic and Cloze cards had overlapping learning targets.
- [x] Basic/Cloze redundancy review completed across all Objective 3.2 Basic and Cloze cards.
- [x] Redundant Cloze cards deleted rather than preserved for card count.
- [x] Image cards kept only where they test visual recognition or useful diagram recognition.
- [x] No intentionally redundant Basic/Cloze learning targets retained.
- [x] Current draft card counts after redundancy cleanup: 14 Basic, 7 Cloze, 7 Image.

## Review and build

- [ ] Omitted-concepts review completed.
- [ ] Independent content review completed.
- [x] Original non-USB diagrams reviewed for clarity, licensing, and answer-leak risk.
- [x] USB connector image-card review completed; bad USB SVGs replaced with license-reviewed Wikimedia Commons photo-derived media.
- [x] Wikimedia Commons license review completed and recorded in `docs/image-sources/3.2-cable-types-connectors-features-and-purposes.md`.
- [x] Question-side USB media checked for visible answer leakage.
- [x] No objectives outside 3.2 modified; Objective 3.3 not created.
- [x] No private source PDFs, screenshots, OCR exports, or unlicensed images committed.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV/media output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Required before acceptance because Objective 3.2 contains Image cards.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 28 after redundancy cleanup |
| Actual note count | 28 total notes: 14 Basic, 7 Cloze, 7 Image |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Passed |
| Media rendering | Passed after copying staged media into Anki `collection.media` |
| Basic Hint column | Passed; stable Hint field imported correctly |
| Headers | Passed; TSV headers were not imported as notes |
| Card ID behavior | Passed; Card ID was first field and drove update behavior |
| HTML rendering | Passed |
| Cloze rendering | Passed |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import behavior | Passed; existing notes updated instead of duplicating |
| Final result | Passed on 2026-07-08 after Basic/Cloze redundancy cleanup |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-06 | Initial Objective 3.2 draft and coverage decisions completed | Independent review and Anki smoke test | Needs independent review |
| Manual Anki smoke test | 2026-07-08 | Basic, Cloze, and Image imports passed with expected counts; media, hints, tags, HTML, note types, and duplicate/update behavior verified | None from smoke test after redundancy cleanup | Passed |
