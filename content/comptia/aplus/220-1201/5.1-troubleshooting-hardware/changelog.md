# Objective 5.1 changelog

## 2026-07-04 - Final cleanup acceptance

- Accepted Objective 5.1 after post-cleanup manual Anki smoke testing passed.
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

- Deleted `5.1-B025` as a duplicate of `5.1-B014`.
- Deleted `5.1-C003` as a duplicate of `5.1-B004`.
- Regenerated TSV output.
- Card-bloat cleanup completed.
- No interview-practice material was exported into TSV.
- No Objective 5.1 scope was expanded.
- No objectives outside 5.1, 5.2, and 5.3 were modified.
- Objective 5.4 was not created.

## 2026-06-30 - Remaining bundled Basic-card fixes

- Narrowed `5.1-B008` to checking whether the outlet or power strip provides
  power.
- Narrowed `5.1-B012` to checking whether cooling fans spin under load.
- Narrowed `5.1-B015` to recording the exact application error message.
- Added `5.1-B022` for checking that the power cable is seated.
- Added `5.1-B023` for checking the power supply rear switch when present.
- Added `5.1-B024` for checking blocked vents or dust restricting airflow.
- Added `5.1-B025` for using temperature readings to confirm overheating.
- Added `5.1-B026` for checking Event Viewer for application-crash evidence.
- Added `5.1-B027` for checking Reliability Monitor for application-failure
  history.
- Removed no cards.
- Reviewed hints after the split; retained only short non-revealing hints where
  they help reasoning before reveal.
- Updated `checklist.md` with narrowed IDs, new split IDs, updated counts, and
  non-export behavior for interview-practice files.
- Regenerated TSV output.
- Did not expand Objective 5.1 scope, modify unrelated objectives, create
  Objective 5.4, or add APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Two-layer troubleshooting refactor

- Created `interview/` with `interview-scenarios.md` and
  `interview-answer-bank.md` for longer spoken troubleshooting practice.
- Moved broad interview-style learning targets out of regular Anki answers and
  into the interview-practice files.
- Rewrote regular Basic cards to favor one specific retrieval target per card.
- Rewrote `5.1-B007`, `5.1-B014`, and `5.1-B017` for narrower power, heat, and
  escalation-evidence decisions.
- Added `5.1-B018` through `5.1-B021` for separate cable, input-source, log, and
  diagnostic-result documentation targets.
- Removed no cards.
- Reviewed hints during the split; retained only short non-revealing hints
  where they help pre-reveal reasoning.
- Updated `study-guide.md` to point longer interview practice to the
  `interview/` directory.
- Updated `checklist.md` to record the two-layer refactor, new counts, rewritten
  card IDs, and that prior manual Anki smoke testing was superseded by this
  content change.
- Regenerated TSV output.
- Did not expand Objective 5.1 scope.
- Did not create content outside the requested Objective 5.1, 5.2, and 5.3
  refactor scope; did not create Objectives 3.2 through 4.x, Objective 5.4
  content, or any APKG/PDF/website/native-occlusion output.

## 2026-06-30 - Optional Basic hints

- Added optional learner-facing `## Hint` sections to selected scenario-heavy
  Basic troubleshooting cards.
- Hints guide pre-reveal reasoning, such as checking safety, recent changes,
  simple external causes, and evidence quality, without duplicating answers.
- Left direct cards without hints where a hint would mostly reveal the answer.
- Did not modify Cloze cards.
- Regenerated TSV output with the updated OpenAPlus Basic Hint field.
- No Objective 3.2 through 4.x content was created.
- No Objective 5.2 or later objective content was created by this 5.1 hint
  update.

## 2026-06-30 - Initial Objective 5.1 draft

- Created Objective 5.1 directory using slug `5.1-troubleshooting-hardware`.
- Used CompTIA 220-1201 Objective 5.1 as the scope authority and Professor
  Messer 220-1201 v1.70 pages 48-50 as a private validation source.
- Drafted `study-guide.md`, `checklist.md`, and 21 cards: 17 Basic, 4 Cloze,
  and 0 Image.
- Prioritized help desk and interview-style troubleshooting decisions:
  information gathering, simple first checks, theory testing, escalation
  details, and documentation.
- Added the study-guide section `Interview-ready troubleshooting language`.
- Did not create Objective 3.2 through 4.x content and did not create Objective
  5.2 content.
- Did not use image cards because the selected learning targets are technician
  decision points rather than visual-recognition tasks.
- Regenerated Objective 5.1 TSV output.
- Added the minimal Objective 5.1 generated tag mapping so TSV output receives
  Domain 5 troubleshooting and Messer v1.70 source-validation tags without
  manual derived tags in card front matter.
- Verified `validate.py`, `build.py`, `pytest`, Ruff check, and Ruff format
  check pass.

## 2026-06-30 - Final acceptance

- Accepted Objective 5.1 after omitted-concepts review, independent content
  review, and manual Anki smoke testing passed.
- Omitted-concepts review result: GO; exact POST code tables, vendor-specific
  diagnostic menus, exact voltage values, deep replacement procedures,
  Objective 5.2 storage details, and Objective 5.3 display fault trees were
  correctly omitted, left study-guide-only, or deferred.
- Independent content review result: GO; source fidelity, copyright safety,
  objective coverage, card quality, HighYield decisions, Instructor Notes,
  generated output, and scope boundaries passed review.
- Verified `Basic.tsv` and `Cloze.tsv` imported successfully in the
  `OpenAPlus Import Test` deck/profile; `Image.tsv` was not applicable because
  Objective 5.1 has no Image cards.
- Verified expected and actual note counts were both 21, headers were not
  imported as notes, Card ID was the first field and update key, HTML rendered
  correctly, Cloze cards generated correctly, and re-importing updated existing
  notes instead of creating duplicates.
- Verified custom OpenAPlus Basic and Cloze note types worked, Instructor Notes
  displayed correctly after answer reveal, and tags imported as Anki metadata
  rather than learner-facing fields.
- Objectives 3.2 through 4.x were not created.
- Objective 5.2 content was not created.
