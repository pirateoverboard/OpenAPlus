# Card schema

Cards live at:

```text
content/comptia/aplus/<exam>/<objective>-<slug>/cards/<card-id>.md
```

Each file starts with YAML front matter and continues with Markdown sections.
The validator rejects malformed YAML and duplicate YAML keys.

## Required metadata

| Field | Type | Rule |
| --- | --- | --- |
| `id` | string | Unique within its exam, filename-matching, and immutable |
| `exam` | string | Must match the exam directory |
| `objective` | string | Must match the ID and objective directory |
| `objective_name` | string | Must agree across the objective |
| `type` | string | `basic`, `cloze`, or `image` |
| `difficulty` | string | `easy`, `medium`, or `hard` |
| `high_yield` | boolean | YAML `true` or `false` |
| `tags` | list of strings | Custom tags only; see [TAGGING.md](TAGGING.md) |
| `source` | list of strings | Non-empty source citations |

Image cards additionally require string-valued `question_image` and
`answer_image` paths. Source images must stay under the approved
`assets/diagrams/` tree, but generated TSV files reference only staged filenames
from `output/media/`.

## Rendered Anki fields

Source metadata remains atomic so validation, paths, IDs, and derived tags can
use stable values. During TSV generation, the Anki `Objective` field is rendered
as a display value:

```text
<exam> <objective> - <objective_name>
```

For example, source metadata `exam: 220-1201`, `objective: "1.1"`, and
`objective_name: Laptop Hardware` renders as:

```text
220-1201 1.1 - Laptop Hardware
```

This display field does not change card IDs, source citations, or derived tags.

For domain-split objectives, generated Anki tags may also include
path-derived domain tags and source-validation tags. For example, Objective 1.3
cards receive a domain tag such as `A+::220-1201::Domain1-MobileDevices` or
`A+::220-1201::Domain1-Security`, plus `Source::Messer-v170` when the objective
was validated against the Professor Messer PDF v1.70. This tag does not mean
Professor Messer defines objective scope; the official CompTIA objective PDF
remains the scope authority. These tags are generated output; do not add them to
YAML front matter.

## Difficulty rubric

- **Easy:** Direct recall of one fact, with no scenario reasoning; typically a
  common term or definition.
- **Medium:** Applies a concept in a simple scenario, makes a comparison, selects
  a first troubleshooting step, or distinguishes similar options.
- **Hard:** Requires multi-step reasoning, several troubleshooting constraints,
  a PBQ-like decision, avoiding a plausible distractor, or combining concepts
  across objectives.

Difficulty measures the reasoning required by the card. Obscurity alone does
not make a fact hard.

## Stable IDs

IDs have the form `<objective>-<type-letter><three digits>` and must be unique
within the exam:

- `1.1-B001` for Basic
- `1.1-C001` for Cloze
- `1.1-I001` for Image

The ID is the first Anki field and is used to update an existing note. Never
reuse, renumber, or change a published ID when wording, tags, or difficulty
changes. A published card cannot move to another objective because its stable
ID contains the objective; retire it and create a new card instead.

## Markdown sections

- Basic requires `## Question` and `## Answer`.
- Cloze requires `## Text` with one or more valid `{{c1::answer}}` expressions.
- Image requires `## Prompt` and `## Answer`.
- Basic cards may include an optional `## Hint` section. Hints are learner-facing
  pre-reveal guidance and should steer the troubleshooting thought process
  without giving away the answer; see [HINTS.md](HINTS.md).
- `## Instructor Notes` is required for accepted production cards unless the
  objective checklist or changelog documents why notes add no value. The
  validator warns when it is absent. Notes must add value rather than repeat the
  answer. Cloze also supports `## Extra`.

Section headings are case-sensitive. Headings inside fenced code blocks are
treated as code. Markdown source is converted to HTML during TSV generation.
See [INSTRUCTOR_NOTES_GUIDE.md](INSTRUCTOR_NOTES_GUIDE.md) for accepted note
sections and examples.
