# Image card guide

OpenAPlus image cards use an occlusion-style pair of reviewed images:

- `question_image` appears on the front and hides, masks, grays out, or boxes
  the answer.
- `answer_image` appears on the back and reveals, labels, or highlights the
  answer.

The prompt and textual answer remain required. True Anki Image Occlusion is not
implemented.

## Appropriate uses

Image cards are useful for recognizing:

- ports and connectors;
- motherboard parts;
- BIOS or firmware screens;
- printer paths;
- RAID layouts;
- networking diagrams;
- other concepts where spatial or visual identification is essential.

Do not use an image when text tests the concept more directly.

## Diagram requirements

- Prefer original SVG diagrams/icons for conceptual diagrams.
- Use user-created original photos or reviewed Wikimedia Commons photos only
  when realistic hardware recognition improves learning.
- Do not trace, screenshot, copy, or modify a copyrighted diagram, source
  layout, proprietary manual image, or vendor diagram.
- Do not use screenshots, random web images, product photos without clear
  licensing, or images with unclear licensing.
- Store files under the approved `assets/diagrams/` hierarchy.
- Use `.svg`, `.png`, `.jpg`, `.jpeg`, or `.webp`.
- The build stages images with deterministic Anki media names such as
  `1.1-I001-question.svg` and `1.1-I001-answer.svg`.
- Keep question and answer images the same dimensions and layout; change only
  what is necessary to reveal the answer.
- Use readable labels, sufficient contrast, and a textual answer for
  accessibility and review.
- Question-side images must not reveal answers in visible text, title, desc,
  aria-label, comments, metadata, or learner-visible filenames.
- Every reviewed external image requires source, author, license, reuse,
  modification, attribution, local filename, review date, selection reason, and
  modification metadata in `docs/image-sources/<objective-slug>.md`.

**Good:** The question image masks one target while retaining enough original
context to identify its location; the answer image reveals that target clearly.

**Bad:** The question image hides several unrelated targets, changes the layout,
or relies on a copied vendor image.

Generated TSV fields contain `<img src="filename">` with no source asset path.
Follow [ANKI_IMPORT.md](ANKI_IMPORT.md) to copy staged files from
`output/media/<exam>/<objective>/` into Anki's media directory before import.
