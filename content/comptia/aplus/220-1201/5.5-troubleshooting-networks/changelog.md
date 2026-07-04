# Objective 5.5 changelog

## 2026-07-04 - Initial draft

- Created Objective 5.5 source content using slug
  `5.5-troubleshooting-networks`.
- Confirmed Objective 5.5 title as **Troubleshooting Networks** from the
  available 220-1201 objective scope and Professor Messer 220-1201 v1.70 notes.
- Used CompTIA 220-1201 Objective 5.5 as the scope authority and Professor
  Messer 220-1201 v1.70 pages 55-56 as a private validation source.
- Drafted `study-guide.md`, `checklist.md`, `interview/interview-scenarios.md`,
  38 Basic cards, 4 Cloze cards, and 0 Image cards.
- Prioritized help desk and interview troubleshooting decisions: physical link
  checks, ping path interpretation, APIPA symptom interpretation, wireless
  interference and placement clues, performance evidence, jitter and VoIP
  symptoms, port flapping isolation, authentication session checks, ISP
  escalation, and documentation.
- Considered Image cards and intentionally omitted them because the selected
  learning targets are test-result interpretations and technician decisions
  rather than visual identification.
- Added a minimal Objective 5.5 domain/source-validation tag mapping so
  generated TSV output receives Domain 5 troubleshooting and Messer v1.70
  source-validation tags without manual derived tags in card front matter.
- Did not create or modify Objectives 3.2 through 4.x.
- Did not modify Objectives 1.1 through 3.1 or Objectives 5.1 through 5.4.
- Did not create Objective 5.6 or any other objective.
- Did not add APKG generation, PDF generation, website rendering, or native
  image occlusion.

## 2026-07-04 - Build verification

- Completed omitted-concepts self-review and recorded intentionally not-carded
  concepts in `checklist.md`.
- Generated TSV output for Objective 5.5.
- Verified final generated draft counts: 38 Basic, 4 Cloze, 0 Image, 42 total.
- Verified `Basic.tsv` uses the stable Hint column:
  `Card ID, Front, Hint, Back, Instructor Notes, Difficulty, Card Type, Objective, Source, Tags`.
- Verified Objective 5.5 interview-practice text was not exported to regular
  TSV output.
- Verified no Objective 5.5 Image cards or media output were generated.
- Verified Objective 5.5 generated tags include the 5.5 objective tag,
  normalized objective-name tag, Domain 5 troubleshooting tag, card-type tag,
  HighYield where applicable, source-validation tag, and author topic tags.
- `.venv/bin/python scripts/validate.py` passed with 395 cards checked.
- `.venv/bin/python scripts/build.py` passed.
- `.venv/bin/python -m pytest` passed with 70 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- Objective 5.6 was not created.

## 2026-07-04 - Independent review fixes

- Omitted-concepts review passed.
- Fixed independent review blockers before manual Anki smoke testing.
- Deleted 5.5-B028 as a duplicate of 5.5-B009; 5.5-B009 remains as the more
  concrete wireless-interference card.
- Rewrote 5.5-B006 to avoid over-specific upstream-cause wording and use the
  safer "beyond the local gateway or on the upstream path" target.
- Softened the answer-revealing hint in 5.5-B017.
- Softened the answer-revealing hint in 5.5-B030.
- Added no cards and deleted no unrelated cards.
- Kept interview-practice text separate from TSV output.
- Regenerated TSV output after cleanup.
- Final expected card counts after cleanup: 37 Basic, 4 Cloze, 0 Image, 41 total.
- Objective 5.6 was not created.

## 2026-07-04 - Final acceptance

- Final acceptance decision: Objective 5.5 accepted after review fixes and
  manual Anki smoke testing.
- Manual Anki smoke test passed in the OpenAPlus Import Test deck/profile.
- Final card counts: 37 Basic, 4 Cloze, 0 Image, 41 total.
- Basic import passed.
- Cloze import passed.
- Image import was not applicable because Objective 5.5 has no Image cards.
- Verified `Basic.tsv` used the stable Hint column and Hint fields imported
  correctly.
- Verified headers were not imported as notes.
- Verified Card ID was the first field and supported duplicate/update behavior.
- Verified re-import updated existing notes instead of duplicating them.
- Verified HTML rendered correctly.
- Verified Cloze cards generated correctly.
- Verified custom OpenAPlus Basic and Cloze note types worked.
- Verified Instructor Notes displayed correctly after answer reveal.
- Verified tags imported as Anki metadata, not learner-facing fields.
- Verified interview-practice text was not exported to TSV.
- Review fixes remained complete: deleted 5.5-B028 as duplicate of 5.5-B009,
  rewrote 5.5-B006 to avoid over-specific upstream-cause wording, softened the
  5.5-B017 hint, and softened the 5.5-B030 hint.
- Confirmed generated output was regenerated.
- No Objective 5.6 content was created.
