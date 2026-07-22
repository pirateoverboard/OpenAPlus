# Objective 2.9 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.9 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.9: Compare and contrast common data
destruction and disposal methods.
```

Official bullet scope reviewed:

1. Physical destruction of hard drives: drilling, shredding, degaussing, and
   incineration.
2. Recycling or repurposing best practices: erasing/wiping, low-level
   formatting, and standard formatting.
3. Outsourcing concepts: third-party vendors and certification of
   destruction/recycling.
4. Regulatory and environmental requirements.

Source-scope decisions:

- The official objective defines the destruction-and-disposal scope and the
  `Compare and contrast` learner task. Professor Messer p. 45 validates the
  method distinctions, outcomes, limitations, and page reference.
- The cards compare methods by recoverability, future drive usability, media
  type, scope, and documentation rather than asking learners to reproduce the
  official bullet list.
- The private Core 2 practice-exam gap check reinforced physical destruction
  when reuse is not required and regular formatting when the drive must
  remain usable. No published wording, scenario, answer choice, explanation,
  or citation was taken from it.
- The official objective says `standard formatting`, while Professor Messer
  p. 45 distinguishes quick and regular variants with different overwrite
  behavior. The study guide and cards preserve that distinction and do not
  claim that every standard format sanitizes data.
- No new secondary source was used, and no unresolved ambiguity blocks the
  supported card set.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Physical destruction versus logical sanitization | CompTIA 2.9; Messer p. 45 | Separate Physical Destruction from Logical Sanitization | 2.9-B001 | Basic | N/A | Self-reviewed |
| Drilling | CompTIA 2.9; Messer p. 45 | Compare Physical Destruction Methods | 2.9-B002 | Basic | N/A | Self-reviewed |
| Shredding | CompTIA 2.9; Messer p. 45 | Compare Physical Destruction Methods | 2.9-B003 | Basic | N/A | Self-reviewed |
| Degaussing magnetic hard drives | CompTIA 2.9; Messer p. 45 | Compare Physical Destruction Methods | 2.9-B004 | Basic | N/A | Self-reviewed |
| Degaussing limitation for SSD and flash | CompTIA 2.9; Messer p. 45 | Compare Physical Destruction Methods | 2.9-B005 | Basic | N/A | Self-reviewed |
| Incineration | CompTIA 2.9; Messer p. 45 | Compare Physical Destruction Methods | 2.9-B006 | Basic | N/A | Self-reviewed |
| File-level overwriting | Messer p. 45; supports CompTIA 2.9 erasing/wiping | Erase or Wipe Media That Will Be Reused | 2.9-B007 | Basic | N/A | Self-reviewed |
| Whole-drive wiping | CompTIA 2.9; Messer p. 45 | Erase or Wipe Media That Will Be Reused | 2.9-B008 | Basic | N/A | Self-reviewed |
| Recycling or repurposing after sanitization | CompTIA 2.9; Messer p. 45 | Erase or Wipe Media That Will Be Reused | 2.9-B001, 2.9-B008, 2.9-B011 | Basic | N/A; cards test method family, wipe scope, and reusable-drive formatting | Self-reviewed |
| Low-level formatting | CompTIA 2.9; Messer p. 45 | Distinguish Formatting Options | 2.9-B009 | Basic | N/A | Self-reviewed |
| Quick standard formatting | CompTIA 2.9; Messer p. 45 | Distinguish Formatting Options | 2.9-B010 | Basic | N/A | Self-reviewed |
| Regular standard formatting | CompTIA 2.9; Messer p. 45 | Distinguish Formatting Options | 2.9-B011 | Basic | N/A | Self-reviewed |
| Third-party destruction/recycling vendor | CompTIA 2.9; Messer p. 45 | Outsource with Verifiable Documentation | 2.9-B012 | Basic | N/A | Self-reviewed |
| Certificate of destruction/recycling | CompTIA 2.9; Messer p. 45 | Outsource with Verifiable Documentation | 2.9-B012 | Basic | N/A; one card tests the required evidence in the third-party context | Self-reviewed |
| Regulatory requirements | CompTIA 2.9; Messer p. 45 | Follow Regulatory and Environmental Requirements | 2.9-B013 | Basic | N/A | Self-reviewed |
| Environmental requirements | CompTIA 2.9; Messer p. 45 | Follow Regulatory and Environmental Requirements | 2.9-B013 | Basic | N/A; one pre-disposal compliance decision covers the paired official requirement | Self-reviewed |
| Named wiping utilities and vendor-specific interfaces | Messer p. 45; supports CompTIA 2.9 | Erase or Wipe Media That Will Be Reused | None | None | Product names and interfaces are not required by the official objective and would add volatile implementation detail | Self-reviewed |
| Exact regulatory retention periods or jurisdiction-specific disposal rules | CompTIA 2.9; Messer p. 45 | Follow Regulatory and Environmental Requirements | None | None | Requirements vary; the stable target is to identify and follow the applicable rules | Self-reviewed |
| Windows-version-specific formatting defaults | Messer p. 45 | None | None | None | Implementation-specific, not required by the official objective, and may become outdated | Self-reviewed |
| Used-drive recovery statistics and source examples | Messer p. 45 | None | None | None | Anecdotal supporting material outside the official method-comparison target | Self-reviewed |

## Objective-specific cautions

- Do not treat deletion, quick formatting, whole-drive wiping, and physical
  destruction as interchangeable.
- Do not recommend degaussing for SSD or flash storage.
- Do not use physical destruction when a scenario explicitly requires the drive
  to remain usable.
- Do not imply that every operation called a standard format overwrites data;
  the quick-versus-regular choice controls the source-backed outcome.
- Do not prescribe one universal disposal process when regulatory,
  environmental, and organizational requirements may differ.
- Do not add product-specific wiping commands or tools that the official
  objective does not require.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.9-B001, 2.9-B003–B005, 2.9-B008, 2.9-B010–B013 | Central reuse-versus-destruction, media limitation, overwrite, outsourcing-evidence, and compliance distinctions reinforced by official scope and the private gap check | Independent review approved |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.9 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed page 45 was used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] The standard-formatting terminology caution is documented without
      guessing.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize method comparisons, consequences, and short
      selection scenarios in line with the official `Compare and contrast`
      wording.
- [x] Cloze cards were considered; no acronym or compact fact benefits from a
      separate Cloze without duplicating a Basic-card target.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve the
      method-selection and outcome distinctions in this objective.
- [x] Interview material was considered and is not justified by this comparison
      objective.
- [x] Instructor Notes add a boundary, consequence, or nearby-method contrast.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review confirms accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 13
      data rows; no Cloze, Command, Image, or media output is expected.
- [x] The 101-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for the generated Basic file.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 13 Basic cards, including nine HighYield cards.
- Generated TSV output: `Basic.tsv` contains 13 verified data rows; no Cloze,
  Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic
  import; headers were not imported as notes, HTML rendered correctly,
  Instructor Notes displayed after reveal, tags imported as Anki metadata,
  Card ID supported update behavior, re-import created no duplicates, and the
  observed count matched 13 Basic notes. The Anki version and disposable
  profile name were not provided.
- Media verification: Not applicable; Objective 2.9 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.9 and Messer p. 45; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; found overbroad SSD-method guidance, an unsupported `full format` alias, unsupported compliance extrapolations, and one difficulty mismatch | Narrow source claims, use `regular format`, restrict compliance explanation, and change B013 to Easy | Changes required |
| Author fix pass | 2026-07-22 | Narrowed SSD guidance to source-supported media compatibility, removed the unsupported alias and compliance extrapolations, changed B013 to Easy, and documented recommended omissions | Blocker-fix verification and manual Anki smoke test remain | Needs blocker-fix verification |
| Blocker-fix verification | 2026-07-22 | GO; all four blockers resolved with no new source, redundancy, scope, metadata, or generated-output issues | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic import, rendering, metadata tags, 13-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
