# Image card guide

OpenAPlus image cards use an occlusion-style pair of original images:

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

- Create original diagrams only. Do not trace, screenshot, or modify a
  copyrighted diagram.
- Store files under the approved `assets/diagrams/` hierarchy.
- Use `.svg`, `.png`, `.jpg`, `.jpeg`, or `.webp`.
- Give every image a unique basename because Anki media uses a flat directory.
- Keep question and answer images the same dimensions and layout; change only
  what is necessary to reveal the answer.
- Use readable labels, sufficient contrast, and a textual answer for
  accessibility and review.

**Good:** The question image masks one target while retaining enough original
context to identify its location; the answer image reveals that target clearly.

**Bad:** The question image hides several unrelated targets, changes the layout,
or relies on a copied vendor image.

Generated TSV fields contain `<img src="filename">`. Follow
[ANKI_IMPORT.md](ANKI_IMPORT.md) to copy the original files into Anki's media
directory before import.
