# OpenAPlus Review Prompt Pack

This file contains reusable Codex prompts for reviewing OpenAPlus objective drafts before acceptance.

Use these after an objective draft is generated and before the manual Anki smoke test.

---

# 1. Omitted Concepts Check Prompt

Use this prompt first when an objective draft includes a list of concepts intentionally not carded.

```text
Run an omitted-concepts review for OpenAPlus Objective <OBJECTIVE_NUMBER> — <OBJECTIVE_NAME>.

Do not modify files.

Review only:

content/comptia/aplus/220-1201/<OBJECTIVE_SLUG>/
assets/diagrams/220-1201/<OBJECTIVE_NUMBER>/ if present
output/tsv/220-1201/<OBJECTIVE_SLUG>/
output/media/220-1201/<OBJECTIVE_SLUG>/ if present

Do not review or modify other objectives.
Do not create new objective content.

Goal:
Evaluate whether each concept listed as intentionally not carded was correctly omitted from flashcards.

For each omitted concept, determine whether it should remain:
- study-guide-only content
- omitted entirely
- converted into a Basic card
- converted into a Cloze card
- converted into an Image card
- deferred because of missing/ambiguous source support

Review these areas:

1. Objective scope
- Is the omitted concept actually in CompTIA A+ 220-1201 Objective <OBJECTIVE_NUMBER> scope?
- Is it an explicit objective item, an example, or supporting explanation?
- Would excluding it create a coverage gap?
- Was the official CompTIA objectives PDF used as the primary scope source?
- Does checklist.md record the official CompTIA domain, objective number, full
  objective phrase, and bullet scope?
- Were card/no-card decisions evaluated against the official objective wording,
  not an internal standard/troubleshooting mode?
- Does the official objective wording affect the active-recall value? For
  example, `Given a scenario` favors applied decisions when useful, `Compare
  and contrast` favors distinctions and tradeoffs, `Explain` favors purpose and
  consequence, and `Identify` favors recognition.

2. Source support
- Is the omitted concept supported by approved source material?
- Was the Professor Messer PDF used only as a secondary validation/page-reference source?
- Were Professor Messer practice exam PDFs, if used, used only as private
  secondary gap-check sources?
- If a matching practice exam was available, was a practice-exam gap check
  completed before acceptance?
- Were any Messer videos, vendor docs, or other secondary sources used without explicit approval?
- Does the approved source support enough detail to write a reliable card?
- Are there any unsupported assumptions?

3. Stability
- Is the concept stable enough for OpenAPlus?
- Would it become outdated quickly because of vendor, model, version, pricing, or product-specific changes?

4. Active recall value
- Is the concept worth memorizing or applying in flashcard form?
- Is it better handled in the study guide only?
- Is it too obvious, too broad, too narrow, or too trivia-like?
- If practice-exam gap checking showed the concept is likely to matter, is
  there a specific checklist reason for leaving it study-guide-only?

5. Card type recommendation
For each omitted concept, recommend exactly one:
- Keep omitted
- Study guide only
- Add Basic card
- Add Cloze card
- Add Image card
- Defer pending approved source

Default to adding a card when a concept is official-scope, source-supported,
stable, useful for recall/application, and practice-test-relevant. Recommend
study-guide-only only when the checklist gives a specific no-card reason or the
concept is better learned as context.

6. Redundancy
- Is the omitted concept already covered by another card?
- Would adding a card create a duplicate learning target?
- Would a new card test a materially different skill?

Return a table with:

| Omitted Concept | In Scope? | Source Supported? | Stable? | Worth Active Recall? | Recommendation | Reason |
|---|---|---|---|---|---|---|

Then provide:

- GO or NO-GO on omitted-concept decisions
- Required additions, if any
- Concepts correctly left study-guide-only
- Concepts correctly omitted entirely
- Practice-test-relevant concepts that must become cards
- Concepts that need better documentation in checklist.md
- Any source ambiguity
- Any risk of card bloat

Do not edit files.
```

---

# 2. Independent Content Review Prompt

Use this prompt after the omitted-concepts check and after any required fixes.

```text
Run an independent content review for OpenAPlus Objective <OBJECTIVE_NUMBER> — <OBJECTIVE_NAME>.

Do not modify files.

Review only:

content/comptia/aplus/220-1201/<OBJECTIVE_SLUG>/
assets/diagrams/220-1201/<OBJECTIVE_NUMBER>/ if present
output/tsv/220-1201/<OBJECTIVE_SLUG>/
output/media/220-1201/<OBJECTIVE_SLUG>/ if present

Do not review previous objectives except to confirm they were not modified.
Do not create the next objective.

Goal:
Determine whether Objective <OBJECTIVE_NUMBER> is ready for acceptance, except for the manual Anki smoke test if it has not yet been performed.

Evaluate:

1. Source fidelity
- Was the official CompTIA objectives PDF used as the primary scope source?
- Does checklist.md record the official CompTIA domain, objective number, full
  objective phrase, and bullet scope?
- Was the official objective wording used to drive the card approach rather
  than an internal standard/troubleshooting mode?
- Was the Professor Messer PDF used only as the secondary validation/page-reference source?
- Were Professor Messer practice exam PDFs, if used, used only as private
  secondary gap-check sources and not as scope authority?
- If a matching practice exam was available, was a practice-exam gap check
  completed before acceptance?
- Are all cards and study-guide claims supported by approved sources?
- Were any Messer videos, vendor docs, or other secondary sources used without explicit approval?
- Are any claims unsupported, overstated, or too vendor/model-specific?
- Are volatile details avoided unless clearly source-backed and justified?
- Are source references sufficient for cards and study-guide sections?

2. Copyright safety
- Is wording substantially paraphrased?
- Are there copied passages, copied tables, copied diagrams, screenshots,
  source-layout reproductions, practice questions, answer choices, or practice
  exam explanations?
- Are all diagrams original?

3. Objective coverage
- Does the study guide cover the objective concept set?
- Do cards stay inside the official CompTIA objective scope?
- Do cards reflect the official objective verb and learner task? For example:
  - `Given a scenario` should include applied scenario, selection, first-check,
    or best-next-step cards where useful.
  - `Compare and contrast` should emphasize distinctions and tradeoffs.
  - `Explain` should emphasize concepts, purposes, and consequences.
  - `Identify` should emphasize recognition and direct recall.
- Does checklist.md accurately map concepts to study-guide sections and card IDs?
- Are intentionally not-carded concepts justified?
- Are any objective items missing or under-covered?
- Are official-scope, source-supported, stable, practice-test-relevant concepts
  useful for recall/application carded by default?
- If any such concept remains study-guide-only, does checklist.md give a
  specific no-card reason?

4. Card quality
- Are Basic cards scenario-based where the official objective wording supports
  scenario-based application?
- Are Cloze cards limited to compact factual recall?
- Are Image cards useful and not answer-leaking?
- Are any cards too broad, too vague, redundant, or trivia-like?
- Are any cards likely to take longer than 15–20 seconds to answer?

5. Redundant learning targets
- Are any Basic, Cloze, or Image cards testing the same fact without testing a materially different skill?
- Compare every Basic card against every Cloze card. Does any Basic/Cloze pair test the same recall target in different note types?
- Are Basic cards reserved for understanding, comparison, purpose, practical recognition, short scenarios, or small decisions?
- Are Cloze cards reserved for compact facts, acronym expansions, short definitions, term recall, or one-line associations?
- If a Basic card and a Cloze card overlap, does each test a materially different skill, or should one be deleted?
- Prefer keeping the Basic card when the concept needs explanation, comparison, purpose, common-confusion handling, or useful Instructor Notes.
- Prefer keeping the Cloze card when the Basic card adds no value beyond the same compact fact.
- Do not preserve duplicate Basic/Cloze pairs merely to keep card count high.
- Image cards may overlap with text cards only when they test a distinct visual-recognition skill.
- Are similar concepts separated cleanly?
- Should any card be deleted instead of rewritten?

6. HighYield classification
- Are HighYield cards justified by the OpenAPlus HighYield rubric?
- Are any HighYield cards over-marked?
- Should any non-HighYield cards be upgraded?

7. Difficulty classification
- Are Easy/Medium/Hard assignments consistent with the OpenAPlus difficulty rubric?
- Are direct recall cards incorrectly marked Medium/Hard?
- Are multi-step scenario cards marked too low?

8. Instructor Notes
- Do Instructor Notes add teaching value?
- Do they avoid merely repeating the answer?
- Do they explain exam traps, real help desk relevance, distinctions, or reasoning where useful?

9. Study guide clarity
- Is the study guide accurate, readable, and scoped to this objective?
- Does it distinguish stable exam concepts from volatile vendor/model-specific details?
- Are references/citations clear?
- Does it avoid unsupported wording?

10. Generated output
- Are TSV files regenerated and consistent with Markdown source?
- Is Card ID first in all TSVs?
- Are Objective fields rendered in the expected display format?
- Are tags generated as Anki metadata and not learner-facing fields?
- Are image references filename-only?
- Is generated media present and consistent with Image.tsv?

11. Scope boundaries
- Were previous objectives left unchanged?
- Was the next objective not created?
- Were no private PDFs or copyrighted source files committed?
- Was no separate troubleshooting/interview content created unless explicitly
  requested or supported by the official objective wording, and source-scoped?
- If interview material exists, is it objective-local and excluded from TSV output?

Return:

- GO or NO-GO decision
- Remaining blockers, if any
- Required fixes, if any
- Recommended improvements, if any
- Cards to delete, if any
- Cards to rewrite, if any
- Basic/Cloze duplicate pairs found, if any
- Confirmation that Basic and Cloze roles are separated
- HighYield changes, if any
- Difficulty changes, if any
- Whether the objective can be accepted after the manual Anki smoke test
- Whether omitted-concept decisions are acceptable
- Whether practice-test gap-check decisions are acceptable
- Whether the card approach matches the official objective wording

Do not edit files.
```

---

# 3. Blocker-Fix Verification Prompt

Use this after Codex applies fixes from an independent review.

```text
Verify OpenAPlus Objective <OBJECTIVE_NUMBER> review fixes.

Do not modify files.

Review only:

content/comptia/aplus/220-1201/<OBJECTIVE_SLUG>/
assets/diagrams/220-1201/<OBJECTIVE_NUMBER>/ if present
output/tsv/220-1201/<OBJECTIVE_SLUG>/
output/media/220-1201/<OBJECTIVE_SLUG>/ if present

Goal:
Check only whether the previous review blockers were fixed.

Previous blockers to verify:

<Paste previous NO-GO blockers here>

Evaluate:
- Were the required fixes completed?
- Did the fixes introduce new unsupported claims?
- Did the fixes create duplicate learning targets?
- Did the fixes preserve alignment with the official objective domain,
  objective number, full objective phrase, and bullet scope?
- Did the fixes use the official objective wording to drive card approach
  rather than an internal standard/troubleshooting mode?
- If Basic/Cloze redundancy was a blocker, were all Basic cards compared against all Cloze cards?
- Were exact Basic/Cloze duplicate learning targets deleted instead of retained for card count?
- Do remaining Basic cards test understanding, comparison, purpose, practical recognition, scenarios, or decisions?
- Do remaining Cloze cards test compact facts, acronym expansions, short definitions, term recall, or one-line associations?
- Do any remaining Image cards overlap only because they test distinct visual recognition?
- Were checklist.md and changelog.md updated?
- Was generated TSV/media output regenerated?
- Are Card IDs stable?
- Were previous objectives left unchanged?
- Was the next objective not created?
- Was no separate troubleshooting/interview content created unless explicitly
  requested or supported by the official objective wording, and source-scoped?

Return:

- GO or NO-GO
- Remaining blockers
- Any new issues caused by fixes
- Basic/Cloze redundancy status
- Whether the objective can proceed to manual Anki smoke test
- Whether the card approach remains aligned to the official objective wording

Do not edit files.
```

---

# 4. Manual Anki Smoke Test Recording Prompt

Use this after the manual Anki import test passes.

```text
Finalize OpenAPlus Objective <OBJECTIVE_NUMBER> acceptance.

Do not create new A+ content.
Do not modify previous objectives.
Do not start the next objective.
Do not modify the pipeline unless a direct documentation mismatch is found.
Do not add APKG generation, PDF generation, or website rendering.

Goal:
Record that Objective <OBJECTIVE_NUMBER> passed manual Anki smoke testing and is accepted.

Manual Anki smoke test result:

- Test deck/profile: OpenAPlus Import Test
- Basic.tsv imported successfully
- Cloze.tsv imported successfully
- Image.tsv imported successfully if present
- Headers were not imported as notes
- Card ID was first field and used for duplicate/update behavior
- HTML rendered correctly
- Cloze cards generated correctly
- Custom OpenAPlus Basic, Cloze, and Image note types worked
- Instructor Notes displayed correctly after answer reveal
- Tags imported correctly as Anki metadata, not learner-facing fields
- Generated media was installed into Anki collection.media if image cards exist
- Image media rendered correctly if image cards exist
- Re-import updated existing notes instead of duplicating them
- Result: Pass

Required updates:

1. Update:

content/comptia/aplus/220-1201/<OBJECTIVE_SLUG>/checklist.md

Record:
- Manual Anki smoke test passed
- Basic/Cloze/Image imports passed as applicable
- Media rendering passed if applicable
- Re-import/update behavior passed
- Tags imported as Anki metadata
- Objective accepted

2. Update:

content/comptia/aplus/220-1201/<OBJECTIVE_SLUG>/changelog.md

Record:
- Final acceptance decision
- Manual Anki smoke test pass
- Media pipeline verification if applicable
- Custom note type verification
- No next objective content was created

3. Run verification:

python scripts/validate.py
python scripts/build.py
python -m pytest
ruff check .
ruff format --check .

If local shell requires virtualenv paths, use:

.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .

Acceptance criteria:

- Objective checklist says accepted
- Objective changelog records final acceptance
- Manual Anki smoke test is recorded as passed
- Validation/build/tests/lint pass
- Previous objectives are unchanged
- No new A+ content is created
- Next objective is not created
- No separate troubleshooting/interview content is created unless explicitly
  requested or supported by the official objective wording, and source-scoped
```

---

# Placeholder Reference

Replace:

- `<OBJECTIVE_NUMBER>` with `2.1`, `2.2`, etc.
- `<OBJECTIVE_NAME>` with the objective title.
- `<OBJECTIVE_SLUG>` with the folder slug, for example:
  - `2.1-ip-addressing-and-common-ports`
  - `3.2-cable-types-connectors-features-and-purposes`
  - or whatever OpenAPlus uses for that objective.
