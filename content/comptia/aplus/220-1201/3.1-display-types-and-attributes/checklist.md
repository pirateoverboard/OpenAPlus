# Objective 3.1 completion checklist

**Objective status: ACCEPTED.** Objective 3.1 has source-backed content,
generated output, independent review, and a passing manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `3.1-display-types-and-attributes` | Hardware | `A+::220-1201::Domain3-Hardware` |

## Scope decision

The Objective 3.1 scope is treated as display types plus display attributes.
Active-recall cards focus on panel tradeoffs, input hardware, lighting
troubleshooting, and stable attribute definitions. One original diagram is used
because the backlight-versus-self-emissive distinction is visual and hardware
focused.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LCD requires a separate backlight | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Display panel types | 3.1-C001, 3.1-I001 | Cloze, Image | N/A; compact definition and visual hardware distinction are distinct | Self-reviewed |
| Mini LED backlight zones | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Display panel types | 3.1-B001, 3.1-C006 | Basic, Cloze | N/A; scenario choice and compact technology recall are distinct | Self-reviewed |
| OLED self-emissive panel | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Display panel types | 3.1-B009, 3.1-C002, 3.1-I001 | Basic, Cloze, Image | N/A; workload choice, acronym recall, and visual hardware distinction are distinct | Self-reviewed |
| TN panel tradeoff | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | LCD panel technologies | 3.1-B003, 3.1-C003 | Basic, Cloze | N/A; scenario tradeoff and acronym recall are distinct | Self-reviewed |
| IPS panel tradeoff | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | LCD panel technologies | 3.1-B002, 3.1-C004 | Basic, Cloze | N/A; scenario tradeoff and acronym recall are distinct | Self-reviewed |
| VA panel tradeoff | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | LCD panel technologies | 3.1-C005 | Cloze | N/A | Self-reviewed |
| Touchscreen input | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Touch and pen input | 3.1-B004 | Basic | N/A | Self-reviewed |
| Digitizer/stylus input | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Touch and pen input | 3.1-B004 | Basic | N/A; compared with touchscreen in one scenario | Self-reviewed |
| Backlight and inverter troubleshooting | Messer v1.70 p.21; CompTIA 3.1 | Present, p.21 | Backlight and inverter troubleshooting | 3.1-B005 | Basic | N/A | Self-reviewed |
| Pixel density | Messer v1.70 pp.21-22; CompTIA 3.1 | Present, pp.21-22 | Display attributes | 3.1-B007, 3.1-C007 | Basic, Cloze | N/A; comparison and compact definition are distinct | Self-reviewed |
| Refresh rate | Messer v1.70 p.22; CompTIA 3.1 | Present, p.22 | Display attributes | 3.1-B006, 3.1-C008 | Basic, Cloze | N/A; mode-selection scenario and unit recall are distinct | Self-reviewed |
| Screen resolution | Messer v1.70 p.22; CompTIA 3.1 | Present, p.22 | Display attributes | 3.1-C010 | Cloze | N/A; core concept carded without exact named resolution tables | Self-reviewed |
| Color gamut and coverage | Messer v1.70 p.22; CompTIA 3.1 | Present, p.22 | Display attributes | 3.1-B008, 3.1-C009 | Basic, Cloze | N/A; workload choice and compact definition are distinct | Self-reviewed |
| Exact refresh/resolution mode tables | Messer v1.70 p.22 | Examples only | Intentionally limited detail | None | None | Intentionally omitted; volatile and better handled when cable/version support is in scope | Self-reviewed |
| Vendor-specific display model claims | Not explicit in CompTIA 3.1 | Not required | Intentionally limited detail | None | None | Intentionally omitted; product-specific and unstable | Self-reviewed |
| Laptop disassembly steps for display repair | Messer v1.70 p.21 | Only a high-level caution | Intentionally limited detail | None | None | Study-guide only; exact repair procedure varies by device | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 3.1-B001 | Mini LED versus conventional LCD is a common display-selection distinction | Self-review; needs independent agreement |
| 3.1-B002 | IPS selection is foundational for color-sensitive display choices | Self-review; needs independent agreement |
| 3.1-B005 | Dim-image backlight/inverter reasoning is a common hardware troubleshooting cue | Self-review; needs independent agreement |
| 3.1-B006 | Refresh-rate selection is a common display-performance decision | Self-review; needs independent agreement |
| 3.1-B008 | Color gamut selection is foundational for photo/video workflows | Self-review; needs independent agreement |
| 3.1-B009 | OLED self-emissive behavior is a core display-type distinction | Self-review; needs independent agreement |
| 3.1-I001 | Backlight versus self-emissive recognition reinforces a core hardware distinction | Self-review; needs independent agreement |

## Research and extraction

- [x] Objective 3.1 title and slug selected from current objective sections and repository naming convention.
- [x] Professor Messer 220-1201 v1.70 pages 21-22 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, image, study-guide-only, and omitted decisions recorded.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified display-selection and troubleshooting scenarios.
- [x] Cloze cards cover compact acronym and attribute recall.
- [x] Image card uses original simplified SVGs for useful hardware recognition.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 9 Basic, 10 Cloze, 1 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams reviewed for clarity, licensing, and answer-leak risk.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV/media output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed, if required.
- [x] Objective accepted by maintainer.

## Manual Anki smoke test

Required before acceptance because Objective 3.1 contains an Image card.

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 20 |
| Actual note count | 20 |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Passed |
| Headers imported as notes | Passed; headers were not imported as notes |
| Card ID duplicate/update behavior | Passed; Card ID was the first field and drove updates |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom note types | Passed; OpenAPlus Basic, Cloze, and Image note types worked |
| Instructor Notes display | Passed; displayed correctly after answer reveal |
| Tags | Passed; imported as Anki metadata, not learner-facing fields |
| Media rendering | Passed; Image cards rendered correctly |
| Question-side SVG answer-leak check | Passed; no answer leaked through visible text or accessibility metadata |
| Answer-side SVG labels | Passed; correct labels displayed after reveal |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Final result | Pass |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-30 | Initial Objective 3.1 draft and coverage decisions completed | Independent review and Anki smoke test | Needs independent review |
| Automated verification | 2026-06-30 | Validation, build, pytest, Ruff, website typecheck, and website build passed | Manual Anki smoke test still pending | Draft verified |
| Independent content review | 2026-06-30 | NO-GO blockers fixed before Anki smoke test | Question-side SVG answer leak fixed; one screen-resolution active-recall card added; exact refresh/resolution mode tables remain omitted; vendor-specific model claims remain omitted; laptop disassembly steps remain study-guide-only or omitted from cards; Objective 3.2 was not created | Ready for verification before manual Anki smoke test |
| Manual Anki smoke test | 2026-06-30 | Basic, Cloze, and Image imports passed in `OpenAPlus Import Test`; custom note types, Instructor Notes, tags-as-metadata, SVG media, answer-leak check, and re-import update behavior passed | None | Accepted |
