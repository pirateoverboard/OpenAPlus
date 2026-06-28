# Objective 1.1 completion checklist

**Objective status: NOT ACCEPTED.** Camera/webcam scope, wireless-card scope,
follow-up reviewer approval, and the required Anki smoke test remain unresolved.

## Coverage map

This map was created before card authoring and updated after self-review.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Manufacturer-specific repair complexity | Professor Messer 220-1201 v1.70 p.1 | Repair Strategy | 1.1-B004 | Basic | N/A | Self-reviewed |
| Battery replacement design | Professor Messer 220-1201 v1.70 p.1 | Batteries | 1.1-B004 | Basic | N/A | Self-reviewed |
| Li-ion and LiPo characteristics | Professor Messer 220-1201 v1.70 p.1 | Batteries | 1.1-C002 | Cloze | N/A | Self-reviewed |
| Keyboard replacement | Professor Messer 220-1201 v1.70 p.1 | Keyboard and Keys | 1.1-B005 | Basic | N/A | Self-reviewed |
| Keycap handling | Professor Messer 220-1201 v1.70 p.1 | Keyboard and Keys | 1.1-B006 | Basic | N/A | Self-reviewed |
| SO-DIMM selection, acronym, and recognition | Professor Messer 220-1201 v1.70 p.1 | Memory | 1.1-B001, 1.1-C001, 1.1-I001 | Basic, Cloze, Image | N/A; each card tests a different skill | Self-reviewed |
| Soldered memory | Professor Messer 220-1201 v1.70 p.1 | Memory | 1.1-B002 | Basic | N/A | Self-reviewed |
| HDD and SSD comparison | Professor Messer 220-1201 v1.70 p.1 | Storage | 1.1-B003 | Basic | N/A | Self-reviewed |
| M.2 storage installation | Professor Messer 220-1201 v1.70 p.1 | Storage | 1.1-C003 | Cloze | N/A | Self-reviewed |
| HDD-to-SSD migration | Professor Messer 220-1201 v1.70 p.1 | Storage Migration | 1.1-B007 | Basic | N/A | Self-reviewed |
| Image file versus drive-to-drive clone | Professor Messer 220-1201 v1.70 p.1 | Storage Migration | 1.1-B008 | Basic | N/A | Self-reviewed |
| Wi-Fi antenna placement | Professor Messer 220-1201 v1.70 pp.1–2 | Wireless Hardware | 1.1-B012, 1.1-I002 | Basic, Image | N/A; textual wire identification and visual placement recognition are distinct | Self-reviewed |
| Bluetooth personal-area connectivity | Professor Messer 220-1201 v1.70 p.2 | Wireless and Short-Range Features | 1.1-C004 | Cloze | N/A | Self-reviewed |
| NFC range and authentication use | Professor Messer 220-1201 v1.70 p.2 | Wireless and Short-Range Features | 1.1-B009, 1.1-C005 | Basic, Cloze | N/A; application and range recall are distinct | Self-reviewed |
| Fingerprint and face biometrics | Professor Messer 220-1201 v1.70 p.2 | Biometrics | 1.1-B010 | Basic | N/A | Self-reviewed |
| Built-in and external microphones | Professor Messer 220-1201 v1.70 p.2 | Microphone | 1.1-B011 | Basic | N/A | Self-reviewed |
| Exact repair times and screw counts | Professor Messer 220-1201 v1.70 p.1 | Repair Strategy | None | None | Model-specific illustrations; not stable learning targets | Self-reviewed |
| Battery shapes and physical styles | Professor Messer 220-1201 v1.70 p.1 | Batteries | None | None | Manufacturer-specific; compatibility principle is sufficient | Self-reviewed |
| NFC payment and workplace anecdotes | Professor Messer 220-1201 v1.70 p.2 | Wireless and Short-Range Features | None | None | Supporting examples; no distinct retrieval target | Self-reviewed |
| Microphone connector variants | Professor Messer 220-1201 v1.70 p.2 | Microphone | None | None | Supporting detail for the external-microphone decision | Self-reviewed |
| Camera/webcam placement in Objective 1.1 | CompTIA 220-1201 Exam Objectives v2.0, Objective 1.1 | None | None | Supplied scope omits it and private notes place camera/webcam in 1.2; clarification required before adding content | Needs clarification |
| Wireless card replacement details | CompTIA 220-1201 Exam Objectives v2.0, Objective 1.1 | Wireless Hardware | None | None | Private pages support antenna placement and Bluetooth roles but not a model-independent replacement procedure | Needs independent review |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.1-B001 | Foundational replaceable-memory selection | Self-reviewed; independent agreement pending |
| 1.1-B003 | Foundational HDD/SSD comparison used in later storage decisions | Self-reviewed; independent agreement pending |
| 1.1-B007 | Required HDD-to-SSD migration decision | Self-reviewed; independent agreement pending |
| 1.1-B012 | Required identification of antenna leads routed around the display | Self-reviewed; independent agreement pending |
| 1.1-C001 | SO-DIMM acronym requires rapid recall | Self-reviewed; independent agreement pending |
| 1.1-C002 | Common battery memory-effect trap | Self-reviewed; independent agreement pending |

## Research and extraction

- [ ] Objective 1.1 scope fully reconciled against CompTIA exam objectives;
  camera/webcam and wireless-card treatment remain unresolved as recorded above.
- [x] Professor Messer 220-1201 v1.70 pages 1–2 reviewed privately.
- [x] Concepts extracted in original wording.
- [x] Card and no-card decisions recorded before authoring.
- [x] Source ambiguities resolved or documented in `changelog.md`.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified application and comparison targets.
- [x] Cloze cards cover justified compact-recall targets.
- [x] Image cards use original diagrams only where visual recognition adds value.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No redundant learning targets remain.
- [x] Changelog records the completed authoring work.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Original diagrams self-reviewed for clarity and unique basenames.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is verified.
- [x] `pytest` and Ruff pass.
- [x] Required Anki smoke test status recorded as pending in `changelog.md`.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-28 | Content and build checks completed | Independent content review and Anki smoke test | Complete |
| Independent content review | 2026-06-28 | Changes required | Correct the listed source, card-quality, classification, image, and scope-status issues | Corrections applied; follow-up approval pending |
