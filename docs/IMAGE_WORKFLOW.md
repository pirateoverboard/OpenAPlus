# OpenAPlus Wikimedia Commons Image Workflow

Use this as the guide for safely adding real photos from Wikimedia Commons to
OpenAPlus.

## Purpose

OpenAPlus prefers original SVG diagrams/icons for conceptual diagrams. Real
photos are allowed when visual recognition needs realistic hardware. The
preferred photo source is a user-created original photo. Wikimedia Commons
photos may be used when license, attribution, technical accuracy, and
modification rights are reviewed and recorded.

## Preferred Image Source Order

1. User-created original photos
2. Original SVG diagrams/icons
3. Wikimedia Commons images with recorded license and attribution
4. Other stock image sources only after explicit user approval

## Do Not Use

Do not use images that include:

- Vendor product photos
- Screenshots from PDFs, websites, apps, or manuals
- Copied diagrams or source layouts
- Random web images
- Visible logos, brand marks, serial numbers, asset tags, or personal data
- Recognizable people
- Product-specific layouts where the card depends on one model
- Images whose license does not clearly allow reuse for a public educational project

## Wikimedia Commons Review Checklist

Only use a Wikimedia Commons image if all of these are true:

- The license allows reuse.
- The license allows modification if the image will be cropped, edited, annotated, or converted.
- Attribution requirements are clear.
- The image is technically accurate for the card.
- The image is generic enough for A+ study, not tied to one vendor/model.
- No visible logo, brand mark, serial number, personal data, or recognizable person appears.
- The image is not a screenshot, manual diagram, vendor promo image, or copied layout.
- Source URL, creator, license, license URL, and attribution text are recorded.
- A technical review confirms the photo matches the intended learning target.
- Question-side images do not reveal the answer in visible text, title, desc,
  aria-label, comments, metadata, or learner-visible filenames.

## Metadata Convention

For every reviewed external image, create or update one Markdown metadata record
for the objective:

```text
docs/image-sources/<objective-slug>.md
```

Record these fields for each image:

- card ID
- topic/connector/object
- source URL
- Wikimedia Commons file title
- author/creator
- license
- license URL if available
- attribution text
- commercial reuse allowed: yes/no/unclear
- modification allowed: yes/no/unclear
- local filename
- date reviewed
- reason selected
- modifications made

## Attribution Guidance

Attribution should be preserved in:

- The objective metadata document under `docs/image-sources/`
- Card Instructor Notes only if useful and concise

Do not put long attribution text on the front of cards.

## Suggested Project Structure

Use the current project structure:

```text
assets/diagrams/<exam>/<objective>/
docs/image-sources/<objective-slug>.md
```

Keep existing SVG assets unless a photo replacement has been approved and tested.

## SVG-to-Photo Replacement Workflow

1. Identify the card ID and current SVG image.
2. Find candidate Wikimedia Commons images.
3. Review each candidate for license, attribution, technical accuracy, and visual clarity.
4. Reject images with brands, people, screenshots, or vendor-specific details.
5. Record metadata in `docs/image-sources/<objective-slug>.md`.
6. Add attribution text to the objective metadata document.
7. Replace the card image reference only after approval.
8. Regenerate TSV and media output.
9. Run validation, build, tests, and lint.
10. Manually smoke test in Anki.

## Codex Prompt: Add Wikimedia Commons Image Policy

```text
Add a Wikimedia Commons image-source workflow for OpenAPlus.

Do not replace existing SVG image cards unless explicitly instructed.
Do not download or commit images automatically unless the image license and attribution metadata are recorded.
Do not use vendor product photos, copied diagrams, screenshots, or images with visible logos/brands.
Do not add APKG generation, PDF generation, website rendering, or native image occlusion.

Goal:
Create a safe workflow for using Wikimedia Commons photos as optional real-photo replacements for OpenAPlus image cards.

Context:
OpenAPlus prefers original SVG diagrams/icons for conceptual diagrams. Real photos may be used when visual recognition needs realistic hardware, preferably user-created photos first and Wikimedia Commons photos second when the license is compatible and attribution is tracked.

Create documentation and optional metadata structure for Wikimedia Commons image usage.

Required policy:

1. Preferred image source order:

- User-created original photos
- Original SVG diagrams/icons
- Wikimedia Commons images with recorded license and attribution
- Other stock image sources only after explicit user approval

2. Wikimedia Commons requirements:

Only use an image if:

- The license allows reuse and modification for educational/public project use
- Attribution requirements are clear
- The image is technically accurate for the card
- The image does not depend on a brand/model-specific feature
- The image has no visible logo, brand mark, serial number, personal data, or recognizable person
- The image is not a screenshot, copied manual diagram, or vendor promotional product photo
- The source URL, creator, license, and attribution text are recorded

3. Metadata requirement:

For every reviewed external image, create or update
`docs/image-sources/<objective-slug>.md` and record:

- card ID
- topic/connector/object
- source URL
- Wikimedia Commons file title
- author/creator
- license
- license URL if available
- attribution text
- commercial reuse allowed: yes/no/unclear
- modification allowed: yes/no/unclear
- local filename
- date reviewed
- reason selected
- modifications made

4. Attribution handling:

Add a documentation note explaining that attribution should be preserved in:

- `docs/image-sources/<objective-slug>.md`
- optionally the card Instructor Notes only if needed

Do not put long attribution text on the front of cards.

5. Create or update docs.

Create or update a document such as:

docs/image-sources/<objective-slug>.md

Include:

- permitted image sources
- prohibited image sources
- Wikimedia Commons review checklist
- metadata example
- attribution guidance
- replacement workflow for SVG-to-photo migration
- warning that Wikimedia license terms vary by file

6. Metadata structure.

Use:

docs/image-sources/<objective-slug>.md

Do not move existing SVG assets unless necessary.

7. Optional validation idea.

If practical without overengineering, add a lightweight validation rule or TODO documentation that every non-original/non-SVG photo must have an entry in `docs/image-sources/<objective-slug>.md`.

Do not break the current build.

8. Do not add Wikimedia images unless explicitly instructed and metadata is recorded.

This task is only to prepare the policy and workflow.

Run:

.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .

Acceptance criteria:

- A clear Wikimedia Commons image-use policy exists
- A metadata convention exists under `docs/image-sources/<objective-slug>.md`
- The policy warns against logos, brands, people, screenshots, vendor photos, and copied diagrams
- The policy explains attribution handling
- Existing SVG image cards still build
- No Wikimedia image is added unless explicitly instructed and metadata is recorded
- No existing Objective content is changed unless documentation links require it
- Validation/build/tests/lint pass
```

## Codex Prompt: Propose Wikimedia Commons Candidates

```text
Find and propose Wikimedia Commons candidate photos for the Objective <OBJECTIVE_NUMBER> image card <CARD_ID>.

Do not commit images yet.
Do not replace the existing SVG yet.

Target card:
<CARD_ID and tool name>

Find candidate images that are:

- technically accurate
- generic, not vendor/model-specific
- free of visible logos/brands
- free of recognizable people
- licensed for reuse/modification
- appropriate for an educational public project

Return:

- candidate file page URLs
- license
- creator
- attribution text
- why each image is or is not suitable
- final recommendation

Do not download or modify files until I approve one image.
```

## Codex Prompt: Replace an Approved SVG With a Wikimedia Photo

```text
Replace the approved OpenAPlus image card SVG with the approved Wikimedia Commons photo.

Do not search for new images.
Do not replace any other cards.
Do not modify unrelated objectives.
Do not use vendor product photos, screenshots, copied diagrams, or images with visible logos/brands.

Target card:
<CARD_ID>

Approved Wikimedia Commons file page:
<URL>

Approved image/license metadata:
<PASTE METADATA>

Required work:

1. Download or add the approved image source only.
2. Store it in the project’s approved photo asset location.
3. Create or update the required objective metadata document.
4. Add or update attribution documentation.
5. Update the card image reference if needed.
6. Regenerate TSV and media output.
7. Verify Anki-safe filename-only media references.
8. Verify generated media exists in output/media.
9. Run validation/build/tests/lint.

Run:

.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .

Acceptance criteria:

- Only the approved card/image assets are changed
- Wikimedia metadata entry exists in `docs/image-sources/<objective-slug>.md`
- Attribution metadata is updated
- No visible logo/brand/person appears
- TSV/media output is regenerated
- Image renders in Anki smoke test
- Validation/build/tests/lint pass
```
