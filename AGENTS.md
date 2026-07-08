# OpenAPlus agent instructions

This repository builds OpenAPlus, an open-source learning platform for CompTIA
certification study materials. Agents must follow the repository documentation
before creating, reviewing, or modifying educational content.

## Required reading

Before changing content, pipeline behavior, generated output, or review records,
read the docs and nearby implementation files that apply to the task.

### Always read for content-authoring or objective review

- [docs/CONTENT_CREATION_RULES.md](docs/CONTENT_CREATION_RULES.md)
- [docs/CARD_SCHEMA.md](docs/CARD_SCHEMA.md)
- [docs/CARD_AUTHORING_GUIDE.md](docs/CARD_AUTHORING_GUIDE.md)
- [docs/CLOZE_GUIDE.md](docs/CLOZE_GUIDE.md)
- [docs/HINTS.md](docs/HINTS.md)
- [docs/TAGGING.md](docs/TAGGING.md)
- [docs/SOURCE_AND_CITATION_RULES.md](docs/SOURCE_AND_CITATION_RULES.md)
- [docs/OBJECTIVE_COMPLETION_CHECKLIST.md](docs/OBJECTIVE_COMPLETION_CHECKLIST.md)
- [docs/ANKI_IMPORT.md](docs/ANKI_IMPORT.md)
- [docs/OpenAPlus_Review_Prompt_Pack.md](docs/OpenAPlus_Review_Prompt_Pack.md)

### Read when relevant

For Image card authoring or Image card review, also read:

- [docs/IMAGE_CARD_GUIDE.md](docs/IMAGE_CARD_GUIDE.md)
- [docs/IMAGE_WORKFLOW.md](docs/IMAGE_WORKFLOW.md)

Use `IMAGE_CARD_GUIDE.md` for Image card behavior and original-diagram
requirements. Use `IMAGE_WORKFLOW.md` for real-photo/source-image workflow,
licensing, attribution, and media provenance review.

For troubleshooting-interview material, also read:

- [docs/INTERVIEW_TROUBLESHOOTING.md](docs/INTERVIEW_TROUBLESHOOTING.md)

### Pipeline/tooling changes

For pipeline, tooling, generated-output, validation, or import/export changes,
read the relevant schema, import, tagging, and test files before editing. Inspect
nearby tests and implementation files directly. Do not invent a documentation
requirement when no specific project doc exists for the changed code path.

## Documentation index

All files currently under `docs/`:

- [docs/ANKI_IMPORT.md](docs/ANKI_IMPORT.md) — Anki TSV import settings,
  media installation, smoke-test procedure, and note-type expectations.
- [docs/agents/bloat-reviewer-standard.md](docs/agents/bloat-reviewer-standard.md)
  — Specialist prompt for standard-objective bloat and redundancy review.
- [docs/agents/independent-reviewer-standard.md](docs/agents/independent-reviewer-standard.md)
  — Specialist prompt for independent review of standard objectives.
- [docs/agents/objective-author-standard.md](docs/agents/objective-author-standard.md)
  — Specialist prompt for authoring standard objectives.
- [docs/CARD_AUTHORING_GUIDE.md](docs/CARD_AUTHORING_GUIDE.md) — When to use
  Basic, Cloze, and Image cards; atomicity and scenario-card guidance.
- [docs/CARD_QUALITY_EXAMPLES.md](docs/CARD_QUALITY_EXAMPLES.md) — Bad,
  okay, and great card examples for contributor self-review.
- [docs/CARD_SCHEMA.md](docs/CARD_SCHEMA.md) — Markdown/YAML card schema,
  required metadata, rendered fields, difficulty rubric, and section rules.
- [docs/CLOZE_GUIDE.md](docs/CLOZE_GUIDE.md) — Cloze-card use cases and quality
  rules.
- [docs/CONTENT_CREATION_RULES.md](docs/CONTENT_CREATION_RULES.md) — Core
  content philosophy, source-backed authoring rules, and objective workflow.
- [docs/IMAGE_CARD_GUIDE.md](docs/IMAGE_CARD_GUIDE.md) — Occlusion-style image
  card behavior and original-diagram requirements.
- [docs/IMAGE_WORKFLOW.md](docs/IMAGE_WORKFLOW.md) — Future workflow for
  safely adding real photos, especially Wikimedia Commons images, with license
  review and attribution tracking.
- [docs/HINTS.md](docs/HINTS.md) — Optional `## Hint` section policy,
  pre-reveal usage, and bad/okay/great hint examples.
- [docs/INTERVIEW_TROUBLESHOOTING.md](docs/INTERVIEW_TROUBLESHOOTING.md) —
  Guidance for objective-local troubleshooting interview-practice files and
  the boundary between broad spoken answers and regular Anki cards.
- [docs/INSTRUCTOR_NOTES_GUIDE.md](docs/INSTRUCTOR_NOTES_GUIDE.md) —
  Instructor Notes policy and acceptable note sections.
- [docs/LICENSE](docs/LICENSE) — Documentation/content license file.
- [docs/OBJECTIVE_COMPLETION_CHECKLIST.md](docs/OBJECTIVE_COMPLETION_CHECKLIST.md)
  — Required objective completion, coverage mapping, review, and acceptance
  workflow.
- [docs/OpenAPlus_Review_Prompt_Pack.md](docs/OpenAPlus_Review_Prompt_Pack.md)
  — Review prompt templates and maintainer review workflow guidance.
- [docs/README.md](docs/README.md) — Documentation directory overview.
- [docs/SOURCE_AND_CITATION_RULES.md](docs/SOURCE_AND_CITATION_RULES.md) —
  Source priority, paraphrasing, ambiguity handling, and citation rules.
- [docs/TAGGING.md](docs/TAGGING.md) — Derived tag policy, custom tag rules,
  HighYield rubric, and domain/source-validation tags.

## Source handling

Private reference sources may be used only as private references. Do not commit
PDFs, screenshots, OCR exports, copied tables, copied diagrams, or long copied
passages. OpenAPlus content must use original wording, original explanations,
original examples, and original diagrams. Cite sources by concise page or
objective reference. Practice exam use is an exception: record it only as
private gap-check context in checklist/changelog notes when useful, not as a
card or study-guide citation.

Official CompTIA exam objectives PDFs are approved primary scope sources.
Professor Messer notes are an approved secondary validation/reference source.
Professor Messer practice exams are approved private secondary gap-check
sources only; they must not define objective scope or supply copied question or
explanation wording.
New secondary sources require explicit user approval before use.

## Official exam objective sources

The official CompTIA exam objectives PDFs are the primary scope authority for
OpenAPlus card creation.

Private local paths:

- Core 1 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1201-exam-objectives-v4.0.pdf`

- Core 2 official objectives:
  `~/openaplus-private-sources/comptia-a-plus-220-1202-exam-objectives-v4.0.pdf`

- Professor Messer Core 1 notes:
  `~/openaplus-private-sources/professor-messer-comptia-220-1201-a-plus-course-notes-v170.pdf`

- Professor Messer Core 2 notes:
  `~/openaplus-private-sources/professor-messer-comptia-220-1202-a-plus-course-notes-v140.pdf`

- Professor Messer Core 1 practice exams:
  `~/openaplus-private-sources/professor-messer-a-plus-220-1201-core-1-practice-exams-v112.pdf`

- Professor Messer Core 2 practice exams:
  `~/openaplus-private-sources/professor-messer-a-plus-220-1202-core-2-practice-exams-v111.pdf`

Authoring source hierarchy:

1. Official CompTIA exam objectives PDF determines objective scope.
2. Professor Messer notes validate concepts and page references.
3. Professor Messer practice exams may be used only as a private secondary
   gap-check after official scope is established.
4. OpenAPlus content must be original and paraphrased.

When writing cards:

- First read the relevant official CompTIA objective from the official objectives PDF.
- Use the official objective title, number, domain, and bullet list as the scope boundary.
- Do not add cards for concepts outside the official objective unless the concept
  is necessary context and is documented as study-guide-only.
- Use Professor Messer notes only as a private supporting reference, not as the scope authority.
- Use Professor Messer practice exams only as a private gap-check after official
  objective scope and note validation. Do not create flashcards from
  practice-test-only concepts, exact practice questions, answer choices, or
  explanation wording.
- When a matching practice exam is available, perform the practice-exam
  gap-check before objective acceptance. If that gap-check surfaces an
  official-scope, source-supported, stable concept that is useful for active
  recall or application, add an Anki card by default. Leaving it
  study-guide-only requires a specific reason in `checklist.md`.
- If the official objectives and Professor Messer notes differ, prefer the
  official objectives for scope and document the ambiguity.
- Do not copy official objective wording into cards except for short unavoidable technology names, acronyms, protocol names, or objective labels.
- Do not commit official objectives PDFs, practice exam PDFs, copied objective
  tables, practice questions, answer choices, explanations, screenshots, OCR
  exports, or long copied passages.

Concepts intentionally not carded or marked study-guide-only must be recorded in
the objective's `checklist.md` under the coverage/omitted-concepts section.
Major omitted-concept decisions may also be mentioned in `changelog.md` when
they affect review or acceptance.
Reviewers should treat unjustified study-guide-only omissions as blockers when
the concept is official-scope, source-supported, stable, and useful for active
recall or application, especially when practice-test gap-checking shows the
concept is likely to matter.

Source ambiguity must be documented in the objective `checklist.md`. If the
ambiguity affects a card, also mention it in the card Instructor Notes or source
note only when useful to the learner. If the ambiguity affects review or
acceptance, record it in `changelog.md`.

## Objective authoring modes

OpenAPlus uses two objective-authoring modes:

1. Standard objective mode
2. Troubleshooting objective mode

Use the correct mode before creating or reviewing cards.

### Standard objective mode

Use standard objective mode for normal CompTIA A+ objectives, including:

- mobile devices
- hardware
- networking concepts
- operating systems
- security
- operational procedures
- printer concepts
- display concepts
- device configuration concepts

Standard objective cards should be direct, concept-first, concise,
exam-scope focused, less ticket-style, and not interview-heavy unless the
objective requires it.

Card style:

- Quality over quantity.
- Do not create cards just to increase card count.
- Prefer clear, direct, concept-first cards.
- Use short scenarios only when they improve understanding.
- Do not force every card into a troubleshooting-ticket format.
- Do not create mandatory interview-practice directories unless the user asks for them.
- Use hints sparingly.
- Do not add hints to simple direct-recall cards unless the hint genuinely improves learning.

Use Basic cards for:

- direct concept questions
- comparisons
- “why” questions
- short scenarios
- first check
- best next step
- most likely cause
- practical recognition

Use Cloze cards for:

- compact facts
- acronyms
- standards
- frequencies
- port/protocol facts
- short definitions
- brief term recall

Use Image cards only when:

- visual identification improves learning
- diagram recognition improves learning
- hardware shape, connector recognition, topology, signal path, or output recognition matters

Avoid creating Basic, Cloze, and Image versions of the same fact unless each card tests a materially different skill.

### Troubleshooting objective mode

Use troubleshooting objective mode only for troubleshooting-heavy objectives, especially Domain 5.

Troubleshooting cards may use more scenario-based prompts, but regular Anki cards must still be atomic.

Troubleshooting card style:

- One card = one specific symptom, cause, check, decision, next step, test-result interpretation, escalation decision, documentation decision, or troubleshooting clue.
- Avoid broad “diagnose the whole ticket” cards.
- Avoid overloaded list answers.
- Keep longer spoken troubleshooting answers in the objective-local `interview/` directory.
- Interview material must not be exported into regular TSV output.

Use troubleshooting interview directories only when:

- the objective is explicitly troubleshooting-heavy, or
- the user asks for interview-practice material.

### Default rule

If the objective is not clearly troubleshooting-heavy, use standard objective mode.

Do not apply the Domain 5 interview-heavy style to standard objectives.

## Specialist agent prompts

Reusable specialist prompts live in `docs/agents/`.

When available, use them instead of inventing new review criteria.

Available files:

- `docs/agents/objective-author-standard.md` — create normal objectives in the standard objective style.
- `docs/agents/independent-reviewer-standard.md` — review normal objectives.
- `docs/agents/bloat-reviewer-standard.md` — check normal objectives for redundancy without punishing direct/easy cards.

When asked to review, do not modify files unless explicitly instructed.

When asked to author, modify only the requested objective.

## Standard objective card guidance

For standard objectives, cards should be:

- clear
- concise
- exam-scope focused
- easy to review repeatedly
- source-backed
- not bloated
- not overly scenario-heavy


## Content boundaries

- Work on one objective at a time unless explicitly instructed otherwise.
- Do not modify accepted objectives unless the task explicitly asks for it.
- Do not start the next objective preemptively.
- Do not add APKG generation, PDF generation, website rendering, native image
  occlusion, full practice exams, or large content expansions unless explicitly
  requested.
- Do not manually add derived tags to card front matter. Author tags are custom
  topic tags only.

An objective is considered accepted when its `checklist.md` and `changelog.md`
record:

- review passed or required fixes completed
- manual Anki smoke test passed
- final card counts
- generated TSV/media verified as applicable
- acceptance decision recorded

## Verification

For standard content/objective changes, run the full verification set unless the
task is explicitly scoped smaller:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
```

For documentation-only changes that do not affect content, pipeline behavior,
tests, or generated output, `pytest` and `ruff` may still be run, but
`validate.py` and `build.py` regeneration is not required unless content or
output is touched.

If website files or website-facing docs are changed, also run:

```bash
npm --prefix website run typecheck
npm --prefix website run build
```

Generated TSV output is part of the repository contract. Regenerate it after
card or pipeline changes and verify that unrelated accepted objectives were not
modified.

Use practical git checks before handoff or commit:

```bash
git status --short
git diff --name-only
git diff --cached --name-only
```

For objective-specific commits, verify staged files do not include unrelated
objectives. Adjust the pattern to the objective being worked on:

```bash
git diff --cached --name-only | grep -E '3\.2|4\.|5\.7|6\.' || echo "No skipped/future objectives staged"
```
