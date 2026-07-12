# OpenAPlus Official Objective Author Agent

Create real OpenAPlus content for one CompTIA A+ 220-1201 objective.

This agent creates objectives from official CompTIA A+ Certification Exam
Objectives wording. The official domain, objective number, full objective
phrase, and bullet list define the scope and the intended learner task.

Do not force troubleshooting-interview style unless the official objective
wording or the user request supports broad troubleshooting practice.

## Boundaries

- Create or update only the requested objective.
- Do not modify earlier objectives unless explicitly asked.
- Do not start the next objective.
- Do not add APKG generation, PDF generation, website rendering, or native image occlusion.
- Do not add unrelated tooling or workflow changes.

Use the current OpenAPlus pipeline, schema, validator, media pipeline, docs, note-type assumptions, tagging rules, AGENTS.md, and authoring rules.

## Private reference sources

Use these private reference sources when available:

- Core 1 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1201-exam-objectives-v4.0.pdf`
- Core 2 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1202-exam-objectives-v4.0.pdf`
- Professor Messer Core 1 notes:
  `~/openaplus-private-sources/professor-messer-comptia-220-1201-a-plus-course-notes-v170.pdf`
- Professor Messer Core 1 practice exams:
  `~/openaplus-private-sources/professor-messer-a-plus-220-1201-core-1-practice-exams-v112.pdf`

Source hierarchy:

1. Official CompTIA exam objectives PDF determines objective scope.
2. Professor Messer PDFs validate concepts and page references.
3. Professor Messer practice exam PDFs may be used only as private secondary
   gap-check sources after official scope is established.
4. OpenAPlus content must be original, paraphrased, objective-scoped, and
   learner-focused.

## Source handling rules

- Use private PDFs as private references only.
- Do not copy private PDFs into the repository.
- Do not quote long passages.
- Do not reproduce tables, diagrams, layouts, screenshots, photos, or source wording.
- Paraphrase heavily.
- Create original explanations, scenarios, and diagrams.
- Cite source pages in card metadata and study-guide references.
- Use the official CompTIA objective PDF as the primary scope authority for what
  belongs in the objective.
- Use Professor Messer PDFs as approved secondary validation/page-reference
  sources after the official CompTIA objective establishes scope.
- Use Professor Messer practice exam PDFs only as private secondary gap-check
  sources. Do not copy, closely paraphrase, or reconstruct practice questions,
  answer choices, explanations, or scenarios. Do not create cards from
  practice-test-only concepts unless the concept is also supported by official
  objective scope and an approved validation/reference source. Do not cite
  practice exams in card metadata or study-guide references; record their use
  only in checklist or changelog review notes when useful.
- When a matching practice exam is available, perform the gap check before
  objective acceptance. If the gap check surfaces an official-scope,
  source-supported, stable concept that is useful for active recall or
  application, add an Anki card by default. Leaving it study-guide-only requires
  a specific reason in `checklist.md`.
- Do not use Messer videos, vendor docs, or other secondary sources unless the
  user explicitly approves them for the objective.

## Objective setup

First, extract the official CompTIA objective scope before consulting Messer.
Use the official objective domain, number, full objective phrase, title, and
bullet list as the objective boundary. Record that official context in
`checklist.md`, for example:

```text
Domain 1.0 Mobile Devices, Objective 1.1: Given a scenario, monitor mobile
device hardware and use appropriate replacement techniques.
```

Then determine the correct objective title and slug from the official scope and
current repository naming conventions.

Create a directory like:

`content/comptia/aplus/220-1201/<objective>-<objective-slug>/`

Required deliverables:

- `study-guide.md`
- `checklist.md`
- `changelog.md`
- Markdown card files under `cards/`
- Basic cards
- Cloze cards
- Image cards only where useful
- Original SVG diagrams only if useful
- Generated TSV output
- Generated media output if image cards are used

Do not create an `interview/` directory unless the official objective wording
supports broad troubleshooting practice or the user asks for interview
material.

## Required tagging behavior

Every card must receive generated tags for:

- `A+::220-1201::<objective>`
- `A+::220-1201::<normalized objective name>`
- appropriate CompTIA domain tag
- card type tag
- `HighYield` if `high_yield` is true
- source validation tag if implemented, such as `Source::Messer-v170`
- custom topic tags only from author metadata

Do not manually duplicate derived tags in card front matter.

If the objective needs a new generated tag mapping, update:

- `docs/TAGGING.md`
- `tests/test_content_pipeline.py`

following the existing pattern.

## Card style

Quality over quantity.

Do not create cards just to increase card count.

Avoid redundant learning targets.

Choose card patterns from the official objective wording:

- `Given a scenario` objectives should include applied scenario, selection,
  first-check, or best-next-step cards where useful.
- `Compare and contrast` objectives should emphasize distinctions, tradeoffs,
  and recognition of similar technologies.
- `Explain` objectives should emphasize concepts, purposes, and consequences.
- `Identify` objectives should emphasize recognition and direct recall.

Regular Anki cards should generally be:

- direct
- clear
- exam-objective focused
- concise
- concept-first
- easy to review repeatedly

Do not make every card a troubleshooting ticket unless the official objective
wording supports that level of troubleshooting practice.

Use Basic cards for:

- direct concept questions
- short scenarios
- comparisons
- “why” questions
- first check
- best next step
- most likely cause
- practical recognition
- applying a concept to a small situation

Use Cloze cards for:

- short memorization facts
- acronyms
- standards
- frequencies
- port/protocol facts
- compact recall
- brief definitions

Use Image cards only when:

- visual identification improves learning
- a diagram makes a concept clearer
- hardware shape, connector recognition, topology, signal path, or screen/output recognition matters

Do not create Basic, Cloze, Image, and Command versions of the same fact unless each card tests a materially different skill.

## Hint behavior

Basic cards may include optional `## Hint`, but hints are not required.

Use hints sparingly unless the official objective wording calls for scenario or
troubleshooting decisions where a non-revealing hint improves reasoning.

Add a hint only when it improves reasoning before reveal.

Do not add hints to simple definition, acronym, standard, or direct recall cards unless the hint is genuinely useful.

Hints must not reveal the answer.

A good hint guides the category of thinking.

A bad hint names the answer, tool, protocol, component, standard, or fix.

## Instructor Notes

Instructor Notes are required unless there is a documented reason they add no value.

Instructor Notes should explain:

- why the answer is correct
- how to distinguish it from nearby concepts
- what the exam is likely testing
- common confusion points

Do not merely repeat the answer.

## HighYield

Set `high_yield: true` only when justified by the OpenAPlus HighYield rubric.

HighYield should be reserved for concepts that are:

- central to the objective
- commonly tested
- practical for entry-level support
- useful for distinguishing similar terms or technologies

Do not mark every card HighYield.

## Study guide

The study guide should:

- explain the objective concepts clearly
- separate stable exam concepts from implementation-specific details
- include caveats for volatile/vendor-specific details
- avoid copied source structure
- avoid unnecessary depth outside the objective

## Checklist

Before writing cards:

1. Extract the objective concepts from official CompTIA scope.
2. Record the official domain, objective number, full objective phrase, and
   bullet scope in `checklist.md`.
3. Choose card patterns from the official objective wording.
4. Validate concepts and page references against the Professor Messer PDF.
5. Create a coverage map in `checklist.md`.
6. Identify which concepts deserve cards.
7. Identify which concepts belong only in the study guide.
8. Record intentionally not-carded concepts with reasons.
9. Run the matching practice-exam gap check when available, without copying or
   reconstructing practice-test content.
10. Convert practice-test-relevant concepts to cards by default when they are
   official-scope, source-supported, stable, and useful for recall or
   application; document any study-guide-only exceptions.
11. Record source ambiguity instead of guessing.
12. Avoid redundant Basic/Cloze/Image/Command cards.

## Objective-specific cautions

For the requested objective, add a short caution section in `checklist.md`.

Examples:

- Do not mix concepts from neighboring objectives unless official scope requires it.
- Do not over-card exact speeds, frequencies, dimensions, UI paths, or vendor-specific behavior unless clearly source-supported.
- Distinguish stable exam concepts from implementation-specific details.
- Put unstable details in the study guide caveats or omit them from flashcards.

## Image-card requirements

If image cards are used:

- Prefer original SVG diagrams/icons for conceptual diagrams.
- Use user-created original photos or reviewed Wikimedia Commons photos only
  when realistic hardware recognition improves learning and complete
  license/attribution metadata is recorded.
- Store original SVGs in the correct assets/media source location used by the project.
- Use deterministic filenames.
- Ensure generated TSV references Anki-safe filename-only media references.
- Ensure generated media output is created under `output/media/220-1201/<objective-slug>/`.
- Validate that media referenced in TSV exists in generated media output.
- Do not use copied source diagrams, screenshots, vendor-specific designs,
  source layouts, random web images, product photos without clear licensing, or
  images with unclear licensing.
- Question-side media must not reveal the answer through title, desc,
  aria-label, visible text, comments, metadata, or learner-visible filenames.

## After writing content

Run:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
