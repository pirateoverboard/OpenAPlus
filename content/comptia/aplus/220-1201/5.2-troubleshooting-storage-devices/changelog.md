# Objective 5.2 changelog

## 2026-07-04 - Final cleanup acceptance

- Accepted Objective 5.2 after post-cleanup manual Anki smoke testing passed.
- Verified Basic and Cloze imports in the `OpenAPlus Import Test` deck/profile.
- Verified Basic.tsv used the stable Hint column and Hint fields imported
  correctly.
- Verified headers were not imported as notes.
- Verified Card ID was the first field and drove duplicate/update behavior.
- Verified HTML rendered correctly and Cloze cards generated correctly.
- Verified custom OpenAPlus Basic and Cloze note types worked.
- Verified Instructor Notes displayed correctly after answer reveal.
- Verified tags imported as Anki metadata, not learner-facing fields.
- Verified re-importing updated existing notes instead of duplicating them.
- Verified interview directory text was not exported to TSV.
- No Objective 5.4 content was created.

## 2026-07-04 - Card-bloat cleanup

- Deleted `5.2-B014` as a duplicate of `5.2-B013`.
- Deleted `5.2-C003` as a duplicate of `5.2-B011`.
- Regenerated TSV output.
- Card-bloat cleanup completed.
- No interview-practice material was exported into TSV.
- No Objective 5.2 scope was expanded.
- No objectives outside 5.1, 5.2, and 5.3 were modified.
- Objective 5.4 was not created.

## 2026-06-30 - Remaining bundled Basic-card fixes

- Narrowed `5.2-B017` to checking whether the external drive is receiving
  power.
- Added `5.2-B023` for trying a known-good external-drive data cable.
- Added `5.2-B024` for trying another compatible computer port.
- Added `5.2-B025` for interpreting a dock or adapter path failure.
- Removed no cards.
- Reviewed hints after the split; retained only short non-revealing hints where
  they help reasoning before reveal.
- Updated `checklist.md` with the narrowed ID, new split IDs, updated counts,
  and non-export behavior for interview-practice files.
- Regenerated TSV output.
- Did not expand Objective 5.2 scope, modify unrelated objectives, create
  Objective 5.4, or add APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Two-layer troubleshooting refactor

- Created `interview/` with `interview-scenarios.md` and
  `interview-answer-bank.md` for longer spoken troubleshooting practice.
- Moved broad storage interview and escalation talk tracks out of regular Anki
  Basic answers and into the interview-practice files.
- Rewrote regular Basic cards to favor one specific storage symptom, evidence
  item, or documentation decision per card.
- Rewrote `5.2-B004`, `5.2-B012`, and `5.2-B019` for narrower drive-detection,
  RAID-console-status, and backup/data-risk documentation targets.
- Added `5.2-B020` through `5.2-B022` for exact boot-error, failed-disk
  identifier, and drive-detection documentation targets.
- Removed no cards.
- Reviewed hints during the split; retained only short non-revealing hints
  where they help pre-reveal reasoning.
- Updated `study-guide.md` to point longer interview practice to the
  `interview/` directory.
- Updated `checklist.md` to record the two-layer refactor, new counts, rewritten
  card IDs, and that prior manual Anki smoke testing was superseded by this
  content change.
- Regenerated TSV output.
- Did not expand Objective 5.2 scope.
- Did not create content outside the requested Objective 5.1, 5.2, and 5.3
  refactor scope; did not create Objectives 3.2 through 4.x, Objective 5.4
  content, or any APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Final acceptance

- Accepted Objective 5.2 after omitted-concepts review, independent content
  review, and manual Anki smoke testing passed.
- Omitted-concepts review result: GO; exact S.M.A.R.T. attribute IDs,
  vendor-specific disk utilities, deep data-recovery procedures, RAID rebuild
  commands, exact product IOPS values, low disk space, and BitLocker/encryption
  recovery-key workflow were correctly omitted, left study-guide-only, or
  deferred pending source support.
- Independent content review result: GO; source fidelity, copyright safety,
  objective coverage, card quality, HighYield decisions, Instructor Notes,
  generated output, and scope boundaries passed review.
- Verified `Basic.tsv` imported successfully in the `OpenAPlus Import Test`
  deck/profile using the updated OpenAPlus Basic note type with the stable Hint
  field.
- Verified `Cloze.tsv` imported successfully; `Image.tsv` was not applicable
  because Objective 5.2 has no Image cards.
- Verified expected and actual note counts were both 23, headers were not
  imported as notes, Card ID was the first field and update key, HTML rendered
  correctly, Cloze cards generated correctly, and re-importing updated existing
  notes instead of creating duplicates.
- Verified populated and empty Hint fields imported cleanly.
- Verified custom OpenAPlus Basic and Cloze note types worked, Instructor Notes
  displayed correctly after answer reveal, and tags imported as Anki metadata
  rather than learner-facing fields.
- Objectives 3.2 through 4.x were not created.
- Objective 5.3 content was not created.

## 2026-06-30 - Optional Basic hints

- Added optional learner-facing `## Hint` sections to selected scenario-heavy
  Basic troubleshooting cards.
- Hints guide pre-reveal reasoning, such as protecting data, checking detection,
  ruling out simple physical causes, and documenting escalation context, without
  duplicating answers.
- Left direct cards without hints where a hint would mostly reveal the answer.
- Did not modify Cloze cards.
- Regenerated TSV output with the updated OpenAPlus Basic Hint field.
- Did not modify Objectives 1.1 through 3.1.
- Did not modify Objective 5.1 except for the requested hint/checklist/changelog
  update.
- Did not create Objectives 3.2 through 4.x.
- Did not create Objective 5.3 or any other objective.

## 2026-06-30 - Initial draft

- Created Objective 5.2 source content for `5.2-troubleshooting-storage-devices`.
- Confirmed title as **Troubleshooting Storage Devices** from the available 220-1201 objective reference and Professor Messer 220-1201 v1.70 notes.
- Reviewed Professor Messer 220-1201 v1.70 pages 50-51 privately as validation/reference material.
- Added a study guide focused on storage failure symptoms, boot failure symptoms, data protection, RAID alerts, S.M.A.R.T., read/write performance, missing drives, and interview-ready troubleshooting language.
- Added 19 Basic cards and 4 Cloze cards.
- Considered Image cards and intentionally omitted them because the selected learning targets are decision-making and symptom triage, not visual identification.
- Recorded intentionally not-carded concepts: exact S.M.A.R.T. attribute IDs, vendor-specific disk utilities, deep data-recovery procedures, RAID rebuild commands, exact product IOPS values, low disk space, and BitLocker/encryption recovery-key workflow.
- Recorded source ambiguity for low disk space and BitLocker/encryption recovery-key workflow because they were not present in the reviewed Objective 5.2 reference pages.
- Added only the minimal 5.2 domain/source-validation tag mapping required for generated TSV tags.
- Did not modify Objectives 1.1 through 3.1.
- Did not modify Objective 5.1.
- Did not create Objectives 3.2 through 4.x.
- Did not create Objective 5.3 or any other objective.
- Did not add APKG generation, PDF generation, website rendering, or native image occlusion.
