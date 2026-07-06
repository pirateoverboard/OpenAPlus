# OpenAPlus Standard Objective Author Agent

Create real OpenAPlus content for one CompTIA A+ 220-1201 objective.

This agent is for normal objectives such as hardware, mobile devices, networking, operating systems, security, and operational procedures.

Do not force troubleshooting-interview style unless the requested objective is explicitly a troubleshooting objective.

## Boundaries

- Create or update only the requested objective.
- Do not modify earlier objectives unless explicitly asked.
- Do not start the next objective.
- Do not add APKG generation, PDF generation, website rendering, or native image occlusion.
- Do not add unrelated tooling or workflow changes.

Use the current OpenAPlus pipeline, schema, validator, media pipeline, docs, note-type assumptions, tagging rules, AGENTS.md, and authoring rules.

## Private reference source

Use this private reference source when available:

`~/openaplus-private-sources/professor-messer-comptia-220-1201-a-plus-course-notes-v170.pdf`

## Source handling rules

- Use the PDF as a private reference only.
- Do not copy the PDF into the repository.
- Do not quote long passages.
- Do not reproduce tables, diagrams, layouts, screenshots, photos, or source wording.
- Paraphrase heavily.
- Create original explanations, scenarios, and diagrams.
- Cite source pages in card metadata and study-guide references.
- Use CompTIA exam scope as the source of truth for what belongs in the objective.
- Use Professor Messer notes as a validation/reference source, not copied content.

## Objective setup

First, determine the correct objective title and slug from the approved source and current repository naming conventions.

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

Do not create an `interview/` directory unless the objective is explicitly troubleshooting-heavy or the user asks for interview material.

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

Regular Anki cards should feel like Objectives 1.x and 2.x:

- direct
- clear
- exam-objective focused
- concise
- concept-first
- easy to review repeatedly

Do not make every card a troubleshooting ticket.

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

Do not create Basic, Cloze, and Image versions of the same fact unless each card tests a materially different skill.

## Hint behavior

Basic cards may include optional `## Hint`, but hints are not required.

For standard objectives, use hints sparingly.

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
2. Validate concepts against the Professor Messer private notes.
3. Create a coverage map in `checklist.md`.
4. Identify which concepts deserve cards.
5. Identify which concepts belong only in the study guide.
6. Record intentionally not-carded concepts with reasons.
7. Record source ambiguity instead of guessing.
8. Avoid redundant Basic/Cloze/Image cards.

## Objective-specific cautions

For the requested objective, add a short caution section in `checklist.md`.

Examples:

- Do not mix concepts from neighboring objectives unless official scope requires it.
- Do not over-card exact speeds, frequencies, dimensions, UI paths, or vendor-specific behavior unless clearly source-supported.
- Distinguish stable exam concepts from implementation-specific details.
- Put unstable details in the study guide caveats or omit them from flashcards.

## Image-card requirements

If image cards are used:

- Use original SVG diagrams/icons only.
- Store original SVGs in the correct assets/media source location used by the project.
- Use deterministic filenames.
- Ensure generated TSV references Anki-safe filename-only media references.
- Ensure generated media output is created under `output/media/220-1201/<objective-slug>/`.
- Validate that media referenced in TSV exists in generated media output.
- Do not use copied source diagrams, product photos, screenshots, vendor-specific designs, or source layouts.
- Question-side SVG metadata must not reveal the answer through title, desc, aria-label, visible text, comments, or metadata.

## After writing content

Run:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
