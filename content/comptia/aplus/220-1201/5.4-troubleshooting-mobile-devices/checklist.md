# Objective 5.4 completion checklist

**Objective status: ACCEPTED.** Objective 5.4 has source-backed content,
generated output, completed review fixes, and a passed manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.4-troubleshooting-mobile-devices` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.4 is treated as troubleshooting mobile device symptoms. Because the
user requested interview preparation, active-recall cards emphasize safety,
data protection, first checks, symptom interpretation, least-invasive tests,
documentation, and escalation. General networking, display, storage, and
hardware topics are included only when Objective 5.4 applies them to mobile
devices.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Poor battery health and aging battery | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Battery and Charging Symptoms | 5.4-B001 | Basic | N/A | Self-reviewed |
| Poor reception and unnecessary radios draining battery | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Battery and Charging Symptoms | 5.4-B002 | Basic | N/A | Self-reviewed |
| App battery usage | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Battery and Charging Symptoms | 5.4-B003 | Basic | N/A | Self-reviewed |
| Swollen battery safety | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Battery and Charging Symptoms | 5.4-B004 | Basic | N/A | Self-reviewed |
| Broken screen and backup priority | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Physical Damage and Liquid Exposure | 5.4-B005, 5.4-B006 | Basic | N/A; backup and sharp-glass safety are separate decisions | Self-reviewed |
| Improper charging path | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Battery and Charging Symptoms | 5.4-B007, 5.4-B008, 5.4-B009 | Basic | N/A; port inspection, cable swap, and adapter verification are separate retrieval targets | Self-reviewed |
| Mobile poor or no connectivity | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Connectivity and Overheating | 5.4-B010, 5.4-B011 | Basic | N/A; cellular location and Wi-Fi range/interference are separate targets | Self-reviewed |
| Liquid damage and Liquid Contact Indicator | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Physical Damage and Liquid Exposure | 5.4-B012, 5.4-B013, 5.4-B014, 5.4-B033, 5.4-C001 | Basic, Cloze | N/A; safety decisions, escalation documentation, and acronym recall are distinct | Self-reviewed |
| Overheating | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Connectivity and Overheating | 5.4-B015, 5.4-B016 | Basic | N/A; app usage and environmental heat are separate checks | Self-reviewed |
| Digitizer or unresponsive touch input | Messer v1.70 p.53; CompTIA 5.4 | Present, p.53 | Touch, Stylus, and Input Problems | 5.4-B017, 5.4-C002 | Basic, Cloze | N/A; restart decision and term recall are distinct | Self-reviewed |
| Physically damaged ports | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Physical Damage and Liquid Exposure | 5.4-B018, 5.4-B034 | Basic | N/A; escalation and documentation are separate decisions | Self-reviewed |
| Malware symptoms and scanning | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Apps, Malware, and Performance | 5.4-B019, 5.4-B020 | Basic | N/A; symptom recognition and battery/heat clue are separate targets | Self-reviewed |
| Cursor drift and calibration | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Touch, Stylus, and Input Problems | 5.4-B021, 5.4-C003 | Basic, Cloze | N/A; action decision and term recall are distinct | Self-reviewed |
| Unable to install applications | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Apps, Malware, and Performance | 5.4-B022, 5.4-B023, 5.4-B024, 5.4-B025 | Basic | N/A; storage, network, compatibility, and store/account checks are separate retrieval targets | Self-reviewed |
| Stylus does not work | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Touch, Stylus, and Input Problems | 5.4-B026, 5.4-B027, 5.4-B028 | Basic | N/A; power, pairing, and physical tip checks are separate retrieval targets; duplicate Bluetooth Cloze was removed | Self-reviewed |
| Degraded performance | Messer v1.70 p.54; CompTIA 5.4 | Present, p.54 | Apps, Malware, and Performance | 5.4-B029, 5.4-B030, 5.4-B031, 5.4-B032 | Basic | N/A; update/restart, storage, background apps, and hardware compatibility are separate targets | Self-reviewed |
| Interview-style mobile troubleshooting explanations | Messer v1.70 p.53-54; CompTIA 5.4 | Supported across Objective 5.4 symptom set | Interview-ready Troubleshooting Language; interview-practice file | None | None | Broad spoken answers belong in `interview/`, not TSV cards | Self-reviewed |
| Exact phone reset key combinations by model | Messer v1.70 p.53 | Model-specific variation noted | Touch, Stylus, and Input Problems | None | None | Intentionally omitted; volatile and vendor/model-specific | Self-reviewed |
| Exact mobile OS menu paths | Messer v1.70 p.53-54 | Examples only | Battery and Charging Symptoms; Apps, Malware, and Performance | None | None | Study-guide only; UI paths change and are not needed for atomic troubleshooting cards | Self-reviewed |
| Board-level port repair procedures | Messer v1.70 p.54 | Repair depth not procedural | Physical Damage and Liquid Exposure | None | None | Intentionally omitted; entry-level support should document and escalate | Self-reviewed |
| Specific third-party security app names | Messer v1.70 p.54 | General scanner/security app only | Apps, Malware, and Performance | None | None | Intentionally omitted; vendor-specific and volatile | Self-reviewed |
| Exact battery chemistry or capacity specifications | Messer v1.70 p.53 | Not required for the symptom decisions | Battery and Charging Symptoms | None | None | Intentionally omitted; not needed for help desk triage | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.4-B001 | Battery health replacement is a common mobile support decision | Self-review; needs independent agreement |
| 5.4-B003 | App battery usage is a common first check for sudden drain | Self-review; needs independent agreement |
| 5.4-B004 | Swollen battery is a safety-critical decision | Self-review; needs independent agreement |
| 5.4-B005 | Broken-screen backup protects user data before repair | Self-review; needs independent agreement |
| 5.4-B007 | Charging-port inspection is a common mobile first check | Self-review; needs independent agreement |
| 5.4-B008 | Known-good cable testing prevents unnecessary device replacement | Self-review; needs independent agreement |
| 5.4-B012 | Liquid exposure requires safe power handling | Self-review; needs independent agreement |
| 5.4-B015 | Overheating and app usage are common help desk clues | Self-review; needs independent agreement |
| 5.4-B017 | Restarting an unresponsive mobile interface is a common first isolation step | Self-review; needs independent agreement |
| 5.4-B019 | Mobile malware symptoms are interview-relevant and practical | Self-review; needs independent agreement |
| 5.4-B022 | App-install failures frequently come from low storage | Self-review; needs independent agreement |
| 5.4-B026 | Stylus battery checks are a simple least-invasive first action | Self-review; needs independent agreement |
| 5.4-B030 | Low storage causing mobile performance problems is common support triage | Self-review; needs independent agreement |
| 5.4-B033 | Liquid-damage escalation documentation protects handoff quality | Self-review; needs independent agreement |
| 5.4-C001 | Liquid Contact Indicator acronym supports mobile damage triage | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.4 title and troubleshooting-mobile-devices scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 53-54 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, study-guide-only, interview-only, and omitted decisions recorded.
- [x] Source ambiguity recorded instead of guessed into cards.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize specific troubleshooting decisions rather than broad interview answers.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards were considered and intentionally omitted because visual recognition did not add enough value for the selected learning targets.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts after review fixes: 34 Basic, 3 Cloze, 0 Image.
- [x] Optional learner-facing hints added to selected troubleshooting Basic cards; hints guide reasoning without revealing answers.
- [x] Interview-practice directory created with longer spoken-answer scenarios.
- [x] Broad interview-style prompts kept out of regular Anki.
- [x] Duplicate card cleanup completed.
- [x] Hint review passed.
- [x] Platform-safe store cache/account wording completed.
- [x] No Objective 5.4 scope was expanded.
- [x] No objectives outside Objective 5.4 were modified for content.
- [x] Objective 5.5 was not created.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams reviewed for clarity, licensing, and unique names, or not applicable.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Objective accepted.

## Build verification

Verification run on 2026-07-04:

- `.venv/bin/python scripts/validate.py` passed with 354 cards checked.
- `.venv/bin/python scripts/build.py` passed and generated Objective 5.4
  Basic.tsv and Cloze.tsv output.
- `.venv/bin/python -m pytest` passed with 69 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Basic.tsv uses the stable Hint column.
- Basic.tsv contains 34 data rows.
- Cloze.tsv contains 3 data rows after review fixes.
- Image.tsv is not applicable because no Objective 5.4 image cards were
  created.
- Generated 5.4 TSV rows include `A+::220-1201::5.4`,
  `A+::220-1201::Domain5-Troubleshooting`,
  `A+::220-1201::TroubleshootingMobileDevices`, card-type tags, HighYield
  where applicable, custom metadata tags, and `Source::Messer-v170`.
- TSV output does not include the interview-practice Markdown prompt text.
- No Objective 5.4 media output was generated because image cards were omitted.
- Objectives 1.1 through 3.1 were not modified for Objective 5.4 content.
- Objectives 3.2 through 4.x were not created.
- Objectives 5.1 through 5.3 were not modified for Objective 5.4 content.
- Objective 5.5 was not created.
- No private source PDF was committed.

## Independent review fixes

Review fixes applied on 2026-07-04:

- Omitted-concepts review completed.
- Independent content review completed.
- Deleted 5.4-C004 as a duplicate of 5.4-B027.
- Softened the answer-revealing hint in 5.4-B019.
- Tightened store cache/account sign-in wording in 5.4-B025 and the study
  guide.
- Tightened store cache/account sign-in wording in the interview material.
- Confirmed no broad "app-store cache" wording remains.
- No cards added.
- No unrelated cards deleted.
- Interview-practice text remains separate from TSV output.
- Objective 5.5 was not created.

## Manual Anki smoke test

Manual Anki smoke test recorded on 2026-07-04 after independent review fixes.

Objective 5.4 has no image cards, so Image.tsv and media smoke testing were not
applicable.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 34 Basic, 3 Cloze, 0 Image, 37 total |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; no image cards |
| Basic Hint column | Passed; Basic.tsv used the stable Hint column |
| Hint field import | Passed |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was first field and drove updates |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom note types | Passed; OpenAPlus Basic and Cloze note types worked |
| Instructor Notes display | Passed; displayed correctly after answer reveal |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Interview directory text exported | Passed; interview directory text was not exported to TSV |
| Final result | Pass |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-04 | Initial Objective 5.4 draft and coverage decisions completed | Automated verification, omitted-concepts review, independent content review, and manual Anki smoke-test decision | Needs independent review |
| Omitted-concepts review | 2026-07-04 | GO; intentionally not-carded concepts were correctly omitted or left study-guide-only | None | Approved for independent content review |
| Independent content review | 2026-07-04 | Required fixes completed: duplicate Cloze removed, hint softened, store cache/account wording tightened | Manual Anki smoke test before acceptance | Ready for manual Anki smoke test |
| Maintainer manual Anki smoke test | 2026-07-04 | Basic and Cloze imports passed; Image import not applicable; Hint field, custom note types, Instructor Notes, tags-as-metadata, interview non-export, and re-import update behavior passed | None | Accepted |
