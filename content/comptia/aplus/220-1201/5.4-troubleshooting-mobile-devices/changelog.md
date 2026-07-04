# Objective 5.4 changelog

## 2026-07-04 - Final acceptance

- Accepted Objective 5.4 after independent review fixes and manual Anki smoke
  testing passed.
- Final card counts: 34 Basic, 3 Cloze, 0 Image, 37 total.
- Verified Basic and Cloze imports in the `OpenAPlus Import Test` deck/profile.
- Verified Image import was not applicable because Objective 5.4 has no image
  cards.
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
- Verified duplicate card cleanup: `5.4-C004` was deleted as a duplicate of
  `5.4-B027`.
- Verified `5.4-B019` hint no longer reveals the answer category.
- Verified store cache/account sign-in wording was tightened in the card, study
  guide, and interview material.
- Confirmed no broad `app-store cache` wording remains.
- No Objective 5.5 content was created.

## 2026-07-04 - Independent review fixes

- Omitted-concepts review completed.
- Independent content review completed.
- Deleted `5.4-C004` as a duplicate of `5.4-B027`.
- Softened the answer-revealing hint in `5.4-B019`.
- Tightened store cache/account sign-in wording in `5.4-B025` and
  `study-guide.md`.
- Tightened store cache/account sign-in wording in the interview material.
- Confirmed no broad `app-store cache` wording remains.
- Added no cards.
- Deleted no unrelated cards.
- Interview-practice text remains separate from TSV output.
- Objective 5.5 was not created.

## 2026-07-04 - Initial draft

- Created Objective 5.4 source content using slug
  `5.4-troubleshooting-mobile-devices`.
- Confirmed Objective 5.4 title as **Troubleshooting Mobile Devices** from the
  available 220-1201 objective scope and Professor Messer 220-1201 v1.70 notes.
- Used CompTIA 220-1201 Objective 5.4 as the scope authority and Professor
  Messer 220-1201 v1.70 pages 53-54 as a private validation source.
- Drafted `study-guide.md`, `checklist.md`, `interview/interview-scenarios.md`,
  34 Basic cards, 4 Cloze cards, and 0 Image cards.
- Prioritized mobile help desk and interview troubleshooting decisions:
  safety, data protection, first checks, symptom interpretation, known-good
  charging-path tests, app-install causes, stylus isolation, malware clues,
  performance triage, documentation, and escalation.
- Considered Image cards and intentionally omitted them because the selected
  learning targets are technician decisions and safety judgments rather than
  visual identification.
- Added a minimal Objective 5.4 domain/source-validation tag mapping so
  generated TSV output receives Domain 5 troubleshooting and Messer v1.70
  source-validation tags without manual derived tags in card front matter.
- Did not create or modify Objectives 3.2 through 4.x.
- Did not modify Objectives 1.1 through 3.1 or Objectives 5.1 through 5.3.
- Did not create Objective 5.5 or any other objective.
- Did not add APKG generation, PDF generation, website rendering, or native
  image occlusion.
- Generated Objective 5.4 Basic.tsv and Cloze.tsv output.
- Verified Basic.tsv uses the stable Hint column.
- Verified interview-practice material is not exported to TSV.
- No unresolved source ambiguity was guessed into cards.
- Ran validation, build, tests, Ruff lint, and Ruff format check successfully:
  354 cards validated, 69 tests passed, and Ruff reported no issues.
