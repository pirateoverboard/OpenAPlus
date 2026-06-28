# Objective 1.3 completion checklist

**Objective status: DRAFT.** Objective 1.3 has source-backed draft content and
generated TSV output. It still requires independent content review and a manual
Anki smoke test before acceptance.

## Coverage map

This map was created before card authoring and updated after the initial build.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Cellular voice/data controls and airplane mode | Professor Messer 220-1201 v1.70 p.4 | Cellular networks | 1.3-B001 | Basic | N/A | Self-reviewed |
| Cellular generations overview | Professor Messer 220-1201 v1.70 p.4 | Cellular generations | 1.3-C001, 1.3-C002, 1.3-C003 | Cloze | N/A; compact generation recall only | Self-reviewed |
| Wi-Fi local network access | Professor Messer 220-1201 v1.70 p.4 | Wi-Fi and Wi-Fi calling | 1.3-B002 | Basic | N/A | Self-reviewed |
| Wi-Fi calling | Professor Messer 220-1201 v1.70 p.4 | Wi-Fi and Wi-Fi calling | 1.3-B003 | Basic | N/A | Self-reviewed |
| Hotspot | Professor Messer 220-1201 v1.70 p.4 | Hotspot | None | None | Covered in study guide only because Objective 1.2 already has active-recall hotspot/tethering coverage | Self-reviewed |
| SIM and eSIM | Professor Messer 220-1201 v1.70 p.4 | SIM and eSIM | 1.3-B004, 1.3-B005, 1.3-C004 | Basic, Cloze | N/A; physical/eSIM scenarios and compact SIM acronym recall are distinct | Self-reviewed |
| Bluetooth pairing process | Professor Messer 220-1201 v1.70 p.4 | Bluetooth pairing | 1.3-B006 | Basic | N/A | Self-reviewed |
| GPS and location services | Professor Messer 220-1201 v1.70 p.4 | GPS and location services | 1.3-B007 | Basic | N/A | Self-reviewed |
| MDM purpose and policy enforcement | Professor Messer 220-1201 v1.70 p.5 | Mobile Device Management | 1.3-B008, 1.3-C006 | Basic, Cloze | N/A; scenario and acronym recall are distinct | Self-reviewed |
| BYOD ownership and security concerns | Professor Messer 220-1201 v1.70 p.5 | BYOD, COPE, and CYOD | 1.3-B009, 1.3-C007 | Basic, Cloze | N/A; ownership/security scenario and acronym recall are distinct | Self-reviewed |
| COPE and CYOD ownership models | Professor Messer 220-1201 v1.70 p.5 | BYOD, COPE, and CYOD | 1.3-B010, 1.3-C008, 1.3-C009 | Basic, Cloze | N/A; comparison and compact acronym recall are distinct | Self-reviewed |
| Synchronization costs and network choice | Professor Messer 220-1201 v1.70 p.5 | Synchronization | 1.3-B011 | Basic | N/A | Self-reviewed |
| Business application synchronization | Professor Messer 220-1201 v1.70 p.5 | Synchronization | 1.3-B012 | Basic | N/A | Self-reviewed |
| Exact cellular speed numbers | Professor Messer 220-1201 v1.70 p.4 | Cellular generations | None | None | Source-backed but intentionally not carded; exact rates are less useful and more brittle than operational generation concepts | Self-reviewed |
| Detailed Bluetooth vendor key sequences | Professor Messer 220-1201 v1.70 p.4 | Bluetooth pairing | None | None | Vendor-specific; study guide notes to check manufacturer instructions | Self-reviewed |
| Image recognition targets | Professor Messer 220-1201 v1.70 pp.4–5 | None | None | None | No image card created because Objective 1.3 concepts are process/decision targets rather than visual identification targets | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.3-B001 | Common troubleshooting distinction between cellular voice, data, and airplane mode | Self-reviewed |
| 1.3-B002 | Foundational mobile network selection between Wi-Fi and cellular data | Self-reviewed |
| 1.3-B006 | Required Bluetooth pairing decision process | Self-reviewed |
| 1.3-B008 | Foundational enterprise mobile management scenario | Self-reviewed |
| 1.3-B009 | Common ownership/security trap for BYOD | Self-reviewed |
| 1.3-B011 | Common data-cap and transfer-cost decision | Self-reviewed |
| 1.3-C004 | SIM acronym and function require quick recall | Self-reviewed |
| 1.3-C006 | MDM acronym and role are foundational for management questions | Self-reviewed |

## Research and extraction

- [x] Professor Messer 220-1201 v1.70 pages 4–5 reviewed privately.
- [x] Concepts extracted in original wording.
- [x] Card and no-card decisions recorded before authoring.
- [x] No unresolved source ambiguity identified for this draft.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified scenarios, comparisons, and best-choice targets.
- [x] Cloze cards cover justified compact-recall targets.
- [x] No image cards created because no visual recognition target was justified.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No redundant learning targets intentionally retained; draft `1.3-C005`
  was removed because it duplicated the eSIM scenario target in `1.3-B005`.
- [x] Changelog records the completed draft work.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is verified.
- [x] `pytest` and Ruff pass.
- [ ] Independent content review completed.
- [ ] Manual Anki smoke test passed.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-28 | Draft content and build checks completed | Independent content review and manual Anki smoke test | Pending |
