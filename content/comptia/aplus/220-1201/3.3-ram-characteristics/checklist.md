# Objective 3.3 completion checklist

**Objective status: DRAFT.** Objective 3.3 has initial source-backed draft
content, generated TSV output, passing automated verification, and a passing
manual Anki smoke test, but still needs omitted-concepts review, independent
content review, and maintainer acceptance.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.3-ram-characteristics` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

Objective 3.3 is treated as standard objective content. Cards focus on RAM
characteristics: DIMM/SODIMM form factors, DDR compatibility, ECC versus
non-ECC RAM, and channel configurations. The objective is not authored in
Domain 5 troubleshooting/interview style.

## Objective-specific cautions

- Do not drift into Objective 3.4 storage devices; RAM is working memory, not
  SSD or hard-drive storage.
- Do not over-card exact DDR speeds, capacities, timings, voltages, or slot
  color conventions because these are platform-specific.
- Do not imply that ECC works in every system; platform support must be checked.
- Keep channel-configuration cards focused on the concept and matching
  requirement rather than motherboard-specific slot layouts.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RAM as working memory, not long-term storage | CompTIA 3.3; Messer v1.70 p.30 | Present, p.30 | RAM versus storage | 3.3-B001 | Basic | N/A | Self-reviewed |
| DIMM form factor | CompTIA 3.3; Messer v1.70 p.30 | Present, p.30 | RAM form factors | 3.3-B002, 3.3-C001 | Basic, Cloze | N/A; form-factor selection and acronym recall are distinct | Self-reviewed |
| SODIMM form factor | CompTIA 3.3; Messer v1.70 p.30 | Present, p.30 | RAM form factors | 3.3-B002, 3.3-C002 | Basic, Cloze | N/A; form-factor selection and acronym recall are distinct | Self-reviewed |
| DRAM refresh behavior | Messer v1.70 p.30 | Present, p.30 | RAM versus storage | None | None | Study-guide-only; useful background but not explicit official Objective 3.3 bullet scope | Review-fixed |
| SDRAM clock synchronization | Messer v1.70 p.30 | Present, p.30 | RAM versus storage | None | None | Study-guide-only; useful background but not explicit official Objective 3.3 bullet scope | Self-reviewed |
| DDR generations and compatibility | CompTIA 3.3; Messer v1.70 pp.30-31 | Present, pp.30-31 | DDR iterations | 3.3-B003, 3.3-C004 | Basic, Cloze | N/A; replacement decision and acronym recall are distinct | Review-fixed |
| ECC versus non-ECC RAM | CompTIA 3.3; Messer v1.70 p.31 | Present, p.31 | ECC and non-ECC RAM | 3.3-B004, 3.3-C005 | Basic, Cloze | N/A; system-use decision and acronym recall are distinct | Self-reviewed |
| Platform support for ECC | CompTIA 3.3; Messer v1.70 p.31 | Present, p.31 | ECC and non-ECC RAM | 3.3-B005 | Basic | N/A | Self-reviewed |
| Memory bandwidth and MT/s | Messer v1.70 p.31 | Present, p.31 | Channel configurations | None | None | Study-guide-only; exact throughput figures are platform-specific and lower-value for this objective | Self-reviewed |
| Dual-channel, triple-channel, and quad-channel configurations | CompTIA 3.3; Messer v1.70 p.31 | Present, p.31 | Channel configurations | 3.3-B006 | Basic | N/A; duplicate Cloze card deleted after review | Review-fixed |
| Matched modules for channel mode | CompTIA 3.3; Messer v1.70 p.31 | Present, p.31 | Channel configurations | 3.3-B007 | Basic | N/A | Self-reviewed |
| Exact DDR transfer rates, capacities, timings, voltages, and slot colors | Messer v1.70 pp.30-31 | Present as examples/details, pp.30-31 | Intentionally limited details | None | None | Study-guide-only; varies by platform and should be checked in system documentation | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.3-B002 | DIMM versus SODIMM is a foundational RAM replacement distinction | Self-review; needs independent agreement |
| 3.3-B003 | DDR generation compatibility is a common RAM upgrade trap | Self-review; needs independent agreement |
| 3.3-B004 | ECC versus non-ECC is central to comparing RAM characteristics | Self-review; needs independent agreement |
| 3.3-B006 | Multi-channel memory is a core performance/configuration concept | Self-review; needs independent agreement |
| 3.3-B007 | Matching modules and slots is a practical RAM configuration decision | Self-review; needs independent agreement |
| 3.3-C001 | DIMM acronym recall supports form-factor recognition | Self-review; needs independent agreement |
| 3.3-C002 | SODIMM acronym recall supports form-factor recognition | Self-review; needs independent agreement |
| 3.3-C005 | ECC acronym recall supports the ECC versus non-ECC objective item | Self-review; needs independent agreement |

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 3.3 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 3.3 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 30-31 reviewed privately for validation and page citations.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card and no-card decisions recorded before authoring.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified RAM selection, compatibility, ECC, and channel-configuration decisions.
- [x] Cloze cards cover justified compact acronym and definition recall.
- [x] No image cards created in this initial draft because the text cards cover the exam decision points without requiring committed media.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Review-required fixes completed: removed out-of-scope DRAM Cloze card, rewrote DDR Cloze to acronym recall, and removed duplicate channel-configuration Cloze card.
- [x] Current draft card counts: 7 Basic, 4 Cloze, 0 Image.

## Review and build

- [ ] Omitted-concepts review completed.
- [ ] Independent content review completed.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke testing passed on 2026-07-08. Objective 3.3 has no Image
cards, so Image.tsv/media smoke testing was not applicable.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 11 total notes: 7 Basic, 4 Cloze, 0 Image |
| Actual note count | 11 total notes: 7 Basic, 4 Cloze, 0 Image |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 3.3 has no Image cards |
| Media rendering | Not applicable |
| Basic Hint column | Passed; stable Hint field imported correctly |
| Headers | Passed; TSV headers were not imported as notes |
| Card ID behavior | Passed; Card ID was first field and drove update behavior |
| HTML rendering | Passed |
| Cloze rendering | Passed |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Re-import behavior | Passed; existing notes updated instead of duplicating |
| Final result | Passed on 2026-07-08 after review-required fixes |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-08 | Initial Objective 3.3 draft and coverage decisions completed | Omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Manual Anki smoke test | 2026-07-08 | Basic and Cloze imports passed with expected counts; hints, tags, HTML, Cloze rendering, and duplicate/update behavior verified | None from smoke test after review-required fixes | Passed |
