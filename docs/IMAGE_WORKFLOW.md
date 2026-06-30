# OpenAPlus Wikimedia Commons Image Workflow

Use this as a future-reference guide and Codex prompt source for safely adding real photos from Wikimedia Commons to OpenAPlus.

## Purpose

OpenAPlus currently uses original SVG diagrams for image cards. Real photos may be added later for tool-recognition cards, especially for Objective 2.8 networking tools. The preferred source is still your own original photos. Wikimedia Commons can be used when the license, attribution, and technical accuracy are reviewed and recorded.

## Preferred Image Source Order

1. User-created original photos
2. Original SVG diagrams/icons
3. Wikimedia Commons images with recorded license and attribution
4. Other stock image sources only after explicit review

## Do Not Use

Do not use images that include:

- Vendor product photos
- Screenshots from PDFs, websites, apps, or manuals
- Copied diagrams or source layouts
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

## Metadata Sidecar Template

For every Wikimedia Commons image added, create a YAML metadata file next to the source image or in a dedicated metadata directory.

Example:

```yaml
source: Wikimedia Commons
source_url:
commons_file_page:
original_file_url:
creator:
license:
license_url:
download_date:
attribution_required: true
attribution_text:
modifications:
technical_review:
  reviewed_by:
  reviewed_date:
  notes:
openaplus_card_ids:
  -
```

## Attribution Guidance

Attribution should be preserved in:

- The sidecar metadata YAML file
- A project-level attribution document, such as `docs/image-attribution.md`
- Card Instructor Notes only if useful and concise

Do not put long attribution text on the front of cards.

## Suggested Project Structure

Possible structure:

```text
assets/photos/220-1201/
assets/photos/metadata/
docs/image-source-policy.md
docs/image-attribution.md
```

Keep existing SVG assets unless a photo replacement has been approved and tested.

## SVG-to-Photo Replacement Workflow

1. Identify the card ID and current SVG image.
2. Find candidate Wikimedia Commons images.
3. Review each candidate for license, attribution, technical accuracy, and visual clarity.
4. Reject images with brands, people, screenshots, or vendor-specific details.
5. Record metadata in a YAML sidecar file.
6. Add attribution to the project attribution document.
7. Replace the card image reference only after approval.
8. Regenerate TSV and media output.
9. Run validation, build, tests, and lint.
10. Manually smoke test in Anki.

## Codex Prompt: Add Wikimedia Commons Image Policy

```text
Add a Wikimedia Commons image-source workflow for OpenAPlus.

Do not replace existing Objective 2.8 SVG image cards yet unless explicitly instructed.
Do not download or commit images automatically unless the image license and attribution metadata are recorded.
Do not use vendor product photos, copied diagrams, screenshots, or images with visible logos/brands.
Do not add APKG generation, PDF generation, website rendering, or native image occlusion.

Goal:
Create a safe workflow for using Wikimedia Commons photos as optional real-photo replacements for OpenAPlus image cards.

Context:
OpenAPlus currently uses original SVG diagrams for image cards. Eventually, we may replace some tool-recognition images with real photos, preferably user-created photos first, and Wikimedia Commons photos second when the license is compatible and attribution is tracked.

Create documentation and optional metadata structure for Wikimedia Commons image usage.

Required policy:

1. Preferred image source order:

- User-created original photos
- Original SVG diagrams/icons
- Wikimedia Commons images with recorded license and attribution
- Other stock image sources only when explicitly reviewed later

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

For every Wikimedia image added, create a sidecar metadata file near the image source asset.

Use YAML like:

source: Wikimedia Commons
source_url:
commons_file_page:
original_file_url:
creator:
license:
license_url:
download_date:
attribution_required: true
attribution_text:
modifications:
technical_review:
  reviewed_by:
  reviewed_date:
  notes:
openaplus_card_ids:
  -

4. Attribution handling:

Add a documentation note explaining that attribution should be preserved in:

- the sidecar metadata file
- a project-level image attribution document
- optionally the card Instructor Notes only if needed

Do not put long attribution text on the front of cards.

5. Create or update docs.

Create a document such as:

docs/image-source-policy.md

Include:

- permitted image sources
- prohibited image sources
- Wikimedia Commons review checklist
- metadata example
- attribution guidance
- replacement workflow for SVG-to-photo migration
- warning that Wikimedia license terms vary by file

6. Optional helper structure.

If appropriate, create directories such as:

assets/photos/220-1201/
assets/photos/metadata/

or another structure consistent with the current project.

Do not move existing SVG assets unless necessary.

7. Optional validation idea.

If practical without overengineering, add a lightweight validation rule or TODO documentation that every non-original/non-SVG photo must have a metadata YAML file.

Do not break the current build.

8. Do not add actual Wikimedia images yet unless explicitly instructed.

This task is only to prepare the policy and workflow.

Run:

.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .

Acceptance criteria:

- A clear Wikimedia Commons image-use policy exists
- A metadata YAML template exists
- The policy warns against logos, brands, people, screenshots, vendor photos, and copied diagrams
- The policy explains attribution handling
- Existing SVG image cards still build
- No actual Wikimedia image is added yet
- No existing Objective content is changed unless documentation links require it
- Validation/build/tests/lint pass
```

## Codex Prompt: Propose Wikimedia Commons Candidates

```text
Find and propose Wikimedia Commons candidate photos for the Objective 2.8 image card <CARD_ID>.

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
3. Create the required YAML metadata sidecar.
4. Add or update project-level image attribution documentation.
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
- Wikimedia metadata sidecar exists
- Attribution document is updated
- No visible logo/brand/person appears
- TSV/media output is regenerated
- Image renders in Anki smoke test
- Validation/build/tests/lint pass
```
