# Changelog

## 2026-06-28 — Objective 1.1 accepted with documented scope caveats

- Objective 1.1 accepted with documented scope caveats for camera/webcam
  placement and wireless-card replacement details.
- Maintainer accepted the camera/webcam and wireless-card replacement-detail
  caveats for this pass because the available approved source material does not
  provide enough source-backed detail to create reliable OpenAPlus cards for
  those items. These caveats remain documented and may be revisited later if
  approved sources are added.
- Manual Anki smoke test: Passed in the `OpenAPlus Import Test` profile/deck.
- Basic, Cloze, and Image TSV imports verified with custom OpenAPlus Basic,
  Cloze, and Image note types.
- Expected note count: 19; actual note count: 19.
- Import headers were not imported as notes.
- Card ID was first field and used for duplicate/update behavior.
- HTML rendered correctly.
- Cloze cards generated correctly.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata, not learner-facing fields.
- Media pipeline verified: generated media was installed into
  `collection.media`, and image media rendered correctly.
- Re-import updated existing notes instead of duplicating them.
- No Objective 1.2 content was created.

## 2026-06-28 — Independent-review corrections

- Rewrote `1.1-B005` to test model-specific keyboard replacement planning,
  fasteners, and ribbon-cable handling rather than an external-keyboard workaround.
- Rewrote `1.1-B012` as sourced antenna-lead identification and removed the
  unsupported claim that display repair caused a wireless fault.
- Clarified and shortened `1.1-B008`, `1.1-B011`, and `1.1-C003`.
- Changed `1.1-B006` and `1.1-B010` from Medium to Easy.
- Removed HighYield from `1.1-C005`, `1.1-I001`, and `1.1-I002`; six cards remain
  HighYield with documented rubric reasons.
- Redesigned `1.1-I001` as an original A/B DIMM versus SO-DIMM comparison and
  redesigned `1.1-I002` with three neutral candidate cable paths.
- Removed unsupported repair-detail and antenna-fault prose from the study guide.
- Added explicit documented scope caveats for camera/webcam and wireless-card
  replacement details. No Objective 1.2 content was created.
- Applied all concrete changes requested by the independent review.

## 2026-06-28 — Objective 1.1 authoring

- Replaced the Phase 2 placeholder with an original Objective 1.1 study guide.
- Added 12 Basic, 5 Cloze, and 2 Image cards; the existing `B001`, `C001`, and
  `I001` IDs remain associated with SO-DIMM learning targets.
- Added an original question/answer SVG pair for Wi-Fi antenna placement.
- Created the coverage map before card authoring and recorded intentional
  no-card decisions.
- Used Professor Messer 220-1201 v1.70 pages 1–2 as a private authoring reference
  and CompTIA 220-1201 Exam Objectives v2.0 Objective 1.1 for scope.

### Scope and source decisions

- Exact repair times and screw counts were treated as model-specific examples,
  not universal facts or card targets.
- Battery shapes, NFC anecdotes, and microphone connector variants remain
  supporting study-guide context rather than separate cards.
- The source describes M.2 installation but does not establish a single M.2
  storage protocol, so no protocol claim or protocol card was created.
- CompTIA Objective 1.1 v2.0 lists camera/webcam, while the supplied expected
  scope omits it and the private notes place camera/webcam in the following 1.2
  material. No camera/webcam content was added; placement needs clarification.
- CompTIA uses the broader term “wireless cards,” while the private Objective 1.1
  pages support antenna placement and general Bluetooth/Wi-Fi roles rather than
  a model-independent wireless-card replacement procedure. No unsupported
  replacement steps were invented.

### Review status

- Self-review completed for wording, source attribution, atomicity, duplication,
  HighYield rationale, and diagram originality.
- Independent content review requested corrections; follow-up review accepted
  Objective 1.1 with documented scope caveats.
- Manual Anki smoke testing passed for Basic, Cloze, and Image imports,
  including media rendering and re-import update behavior.
