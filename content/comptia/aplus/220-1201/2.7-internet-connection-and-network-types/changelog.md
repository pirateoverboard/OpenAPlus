# Objective 2.7 changelog

## 2026-06-29 — Initial Objective 2.7 draft

- Confirmed the official title and created the slug
  `2.7-internet-connection-and-network-types`.
- Confirmed the official scope: satellite, fiber, cable, DSL, cellular, WISP,
  LAN, WAN, PAN, MAN, SAN, and WLAN.
- Used Professor Messer v1.70 pages 18–19 only to validate concept presence and
  page references. No source wording, tables, diagrams, layouts, or product
  examples were copied.
- Created an original study guide and coverage map before card authoring.
- Added 11 Basic cards and 9 Cloze cards.
- Created no Image cards because variable equipment appearance and generic
  topology diagrams would not improve the objective's comparison targets.
- Added the generated Objective 2.7 domain/source-validation tags through the
  existing pipeline mapping.
- Intentionally did not card exact speeds, prices, data caps, latency figures,
  distance limits, DOCSIS versions, cellular generations, radio parameters, or
  vendor/provider-specific implementations.
- Deferred networking tools to Objective 2.8.
- Did not modify accepted Objectives 1.1 through 2.6.
- Did not create Objective 2.8 content.
- Validation, deterministic TSV generation, pytest, and Ruff checks passed.
- Omitted-concepts review, independent content review, and manual Anki smoke
  testing remain pending.

## 2026-06-29 — Independent review fixes before Anki smoke test

- Completed the omitted-concepts review; no additional cards were required.
- Completed the independent content review and applied its source-support
  wording fixes.
- Limited the cellular study-guide section to cellular networking, tethering,
  and mobile hotspots.
- Reworded `2.7-B005` so it distinguishes the local device-to-phone connection
  from cellular upstream service without naming unsupported tethering media.
- Reworded `2.7-B002` to use the supported fiber installation/equipment cost
  and repair-difficulty distinctions.
- Removed the unsupported line-condition phrase from `2.7-B004` while retaining
  the supported DSL distance sensitivity.
- Limited the study guide and `2.7-B006` to terrestrial WISP service and outdoor
  customer equipment without path, alignment, distance, or nearby-provider
  claims.
- Regenerated Objective 2.7 TSV output.
- Added no cards and deleted no cards.
- Did not create Objective 2.8 content.

## 2026-06-29 — Final acceptance

- Objective 2.7 accepted.
- Manual Anki smoke test passed in the `OpenAPlus Import Test` deck/profile.
- Basic.tsv and Cloze.tsv imported successfully.
- Image.tsv was not applicable because Objective 2.7 has no Image cards.
- Expected and actual note counts both equaled 20.
- Headers were not imported as notes.
- Card ID was the first field and supported duplicate/update behavior.
- HTML rendered correctly, and Cloze cards generated correctly.
- Custom OpenAPlus Basic and Cloze note types worked.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata rather than learner-facing fields.
- Re-import updated existing notes without creating duplicates.
- No Objective 2.8 content was created.
