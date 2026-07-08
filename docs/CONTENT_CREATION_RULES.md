# Content creation rules

OpenAPlus content should help a learner understand, recall, and apply a sourced
concept. Quality matters more than card count. A small, reviewed objective is
better than a large deck of shallow or uncertain prompts.

## Core principles

- **Source-backed only:** Every factual claim must be traceable to an approved
  source. Every card requires a non-empty `source` list.
- **No invented facts:** Do not fill gaps from memory, inference, or generated
  text. If a source is unclear, stop and request clarification.
- **Original expression:** Paraphrase source material. Never copy exam questions,
  proprietary explanations, or diagrams.
- **One objective at a time per workstream:** Keep each pull request or authoring
  workstream focused on one objective. Multiple contributors may work on
  separate objectives in parallel, but changes to shared schema, pipeline code,
  or global documentation require coordination.
- **Quality over quantity:** Do not create cards merely to meet a count. Each card
  must have a specific learning purpose.

OpenAPlus is not an AI card dump. AI-assisted drafts are untrusted until a human
checks every claim against its cited source, rewrites it clearly, and reviews it
under the same standards as manually drafted content. Volume is not evidence of
quality.

## Avoid redundant cards

Do not create Basic, Cloze, and Image versions of the same fact unless each card
tests a materially different skill. A direct-recall Basic card and a Cloze card
with the same retrieval target are duplicates; delete one rather than keeping
both. A recall card and an applied scenario may coexist when the scenario
requires a distinct decision.

Coverage does not require a card for every extracted concept. Record concepts
that remain study-guide-only in the objective coverage map. See
[CARD_QUALITY_EXAMPLES.md](CARD_QUALITY_EXAMPLES.md) for comparisons.
When an approved matching practice exam is available, use it as a private
gap-check before objective acceptance. Practice-test-relevant concepts still
must be official-scope and independently source-supported, but if they are
stable and useful for recall or application, the default is to add an Anki card
rather than leave them study-guide-only. A study-guide-only decision for such a
concept needs a specific checklist reason.

## Authoring workflow

1. Confirm the exam version and objective directory.
2. Review sources according to the roles defined by
   [SOURCE_AND_CITATION_RULES.md](SOURCE_AND_CITATION_RULES.md).
3. Extract concepts without copying source wording.
4. Draft the study guide and objective checklist.
5. Create only the Basic, Cloze, and Image cards justified by the concepts,
   using [CARD_QUALITY_EXAMPLES.md](CARD_QUALITY_EXAMPLES.md) as the quality bar.
6. Add concise, useful Instructor Notes and custom tags.
7. Peer review facts, wording, citations, and diagrams.
8. Run `python scripts/validate.py`, `python scripts/build.py`, and `pytest`.

Follow [CARD_SCHEMA.md](CARD_SCHEMA.md) for metadata and stable IDs,
[CARD_AUTHORING_GUIDE.md](CARD_AUTHORING_GUIDE.md) for card design, and
[TAGGING.md](TAGGING.md) for custom tags.

For troubleshooting-heavy objectives, longer spoken-answer practice belongs in
objective-local `interview/` files rather than regular Anki cards. See
[INTERVIEW_TROUBLESHOOTING.md](INTERVIEW_TROUBLESHOOTING.md) for the boundary
between broad interview prompts and atomic review cards.

## Definition of complete

An objective is not complete until all of the following are reviewed together:

- `study-guide.md`
- `checklist.md`
- `changelog.md`
- the objective's source cards
- successfully generated TSV files

Validation and TSV generation must pass, generated output must be committed,
and the [objective completion checklist](OBJECTIVE_COMPLETION_CHECKLIST.md) must
be satisfied. Passing the validator alone does not establish content quality.
