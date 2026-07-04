# Objective 5.6 changelog

## 2026-07-04 - Initial draft

- Created Objective 5.6 source content using slug
  `5.6-troubleshooting-printers`.
- Confirmed Objective 5.6 title as **Troubleshooting Printers** from the
  available 220-1201 objective scope and Professor Messer 220-1201 v1.70 notes.
- Used CompTIA 220-1201 Objective 5.6 as the scope authority and Professor
  Messer 220-1201 v1.70 pages 56-57 as a private validation source.
- Drafted `study-guide.md`, `checklist.md`, `interview/interview-scenarios.md`,
  32 Basic cards, 3 Cloze cards, and 3 Image cards.
- Prioritized help desk and interview troubleshooting decisions: test-page
  isolation, driver and page-description-language clues, inkjet and laser output
  symptoms, paper path safety, queue/spooler triage, finishing-unit issues,
  tray configuration, printer connectivity, print server scope, and
  documentation.
- Created original SVG diagrams for printer output symptom recognition. No
  copied source diagrams, screenshots, vendor photos, or source layouts were
  used.
- Added a minimal Objective 5.6 domain/source-validation tag mapping so
  generated TSV output receives Domain 5 troubleshooting and Messer v1.70
  source-validation tags without manual derived tags in card front matter.
- Did not create or modify Objectives 3.2 through 4.x.
- Did not modify Objectives 1.1 through 3.1 or Objectives 5.1 through 5.5.
- Did not create any objective after 5.6.
- Did not add APKG generation, PDF generation, website rendering, or native
  image occlusion.

## 2026-07-04 - Build verification

- Generated TSV and media output for Objective 5.6.
- Verified final generated draft counts: 32 Basic, 3 Cloze, 3 Image, 38 total.
- Verified `Basic.tsv` uses the stable Hint column:
  `Card ID, Front, Hint, Back, Instructor Notes, Difficulty, Card Type, Objective, Source, Tags`.
- Verified Objective 5.6 interview-practice text was not exported to regular
  TSV output.
- Verified Objective 5.6 Image TSV references Anki-safe filename-only media
  names.
- Verified generated media output exists under
  `output/media/220-1201/5.6-troubleshooting-printers/`.
- Verified Objective 5.6 generated tags include the 5.6 objective tag,
  normalized objective-name tag, Domain 5 troubleshooting tag, card-type tag,
  HighYield where applicable, source-validation tag, and author topic tags.
- `.venv/bin/python scripts/validate.py` passed with 432 cards checked.
- `.venv/bin/python scripts/build.py` passed.
- `.venv/bin/python -m pytest` passed with 71 tests.
- `.venv/bin/ruff check .` passed.
- `.venv/bin/ruff format --check .` passed.
- No objective after 5.6 was created.

## 2026-07-04 - Independent review fixes

- Omitted-concepts review passed.
- Fixed independent review blockers before manual Anki smoke testing.
- Deleted 5.6-C002 as a duplicate of 5.6-B020; 5.6-B020 remains as the
  troubleshooting interpretation card for finishing timing.
- Fixed answer leakage in `assets/diagrams/220-1201/5.6/garbled-output-question.svg`
  by replacing printer-language-looking strings with neutral gibberish.
- Confirmed Image cards remain appropriate for Objective 5.6.
- Changed 5.6-B015 difficulty from medium to easy because it directly tests the
  print-service log evidence source.
- Kept interview-practice text separate from TSV output.
- Deleted no unrelated cards.
- Modified no objectives outside Objective 5.6 content.
- Created no later objective.
- Regenerated TSV and media output after cleanup.
- Final generated counts after cleanup verified: 32 Basic, 2 Cloze, 3 Image, 37 total.

## 2026-07-04 - Final acceptance

- Accepted Objective 5.6 after independent review fixes and manual Anki smoke
  testing.
- Manual Anki smoke test passed in test deck/profile
  `OpenAPlus Import Test`.
- Final accepted card counts: 32 Basic, 2 Cloze, 3 Image, 37 total.
- Verified Basic, Cloze, and Image imports.
- Verified `Basic.tsv` used the stable Hint column and Hint fields imported
  correctly.
- Verified TSV headers were not imported as notes.
- Verified Card ID was the first field and used for duplicate/update behavior.
- Verified HTML rendered correctly and Cloze cards generated correctly.
- Verified Objective 5.6 image cards rendered correctly and 5.6 media files
  were copied into Anki `collection.media`.
- Verified custom OpenAPlus Basic, Cloze, and Image note types worked.
- Verified Instructor Notes displayed correctly after answer reveal.
- Verified tags imported as Anki metadata, not learner-facing fields.
- Verified re-import updated existing notes instead of duplicating them.
- Verified interview-practice directory text was not exported to regular TSV.
- Confirmed 5.6-C002 remains deleted as a duplicate of 5.6-B020.
- Confirmed `garbled-output-question.svg` no longer reveals PDL or driver clues
  on the question side.
- Confirmed TSV and media output were regenerated after review fixes.
- Confirmed no later objective content was created.
