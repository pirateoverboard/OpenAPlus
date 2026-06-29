# Objective 2.6 changelog

## 2026-06-29 — Initial Objective 2.6 draft

- Determined the official title and slug: `Basic SOHO Network Configuration`,
  `2.6-basic-soho-network-configuration`.
- Reconciled the broad wired/wireless SOHO title with the explicit official
  bullet list and approved reference pages, which cover IP addressing only.
- Created an original study guide covering IPv4 public/private addressing,
  IPv6, static/dynamic assignment, subnet masks, gateways, and APIPA.
- Created the coverage map and no-card decisions before card authoring.
- Added 6 Basic cards and 7 Cloze cards.
- Created no Image cards because address-format visuals would not improve the
  tested recognition or configuration decisions.
- Added the Objective 2.6 generated domain/source-validation tag mapping:
  `A+::220-1201::Domain2-Networking` and `Source::Messer-v170`.
- Used Professor Messer pages 17–18 only for concept validation and concise page
  references. No source tables, diagrams, layouts, or wording were copied.
- Avoided duplicate DHCP configuration, wireless-standard, and network-device
  learning targets from accepted objectives.
- Intentionally omitted full subnetting math, classful-addressing detail,
  address-count trivia, exhaustive IPv6 rules, APIPA implementation sequencing,
  and vendor-specific configuration paths.
- Deferred cabling/connectors to Objective 3.2 and networking tools to Objective
  2.8 instead of inferring them into Objective 2.6.
- No Objective 2.7 content was created.
- Omitted-concepts review, independent review, and manual Anki smoke testing
  remain pending.

## 2026-06-29 — Independent review fixes before Anki smoke test

- Added concise, source-backed NAT context to the study guide to explain how a
  SOHO router commonly supports private IPv4 clients accessing public networks.
- Clarified the `2.6-B001` Instructor Notes with the same NAT explanation.
- Kept NAT as study-guide-only context and created no NAT card.
- Reworded `2.6-B006` to ask what an APIPA address indicates without asserting
  one specific underlying DHCP failure.
- Regenerated Objective 2.6 TSV output.
- Recorded completion of the omitted-concepts and independent content reviews.
- Added no cards and deleted no cards.
- Did not create Objective 2.7 content.

## 2026-06-29 — Final acceptance

- Objective 2.6 accepted.
- Manual Anki smoke test passed in the `OpenAPlus Import Test` deck/profile.
- Basic.tsv and Cloze.tsv imported successfully.
- Image.tsv was not applicable because Objective 2.6 has no Image cards.
- Headers were not imported as notes.
- Card ID was the first field and supported duplicate/update behavior.
- HTML rendered correctly, and Cloze cards generated correctly.
- Custom OpenAPlus Basic and Cloze note types worked.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata rather than learner-facing fields.
- Re-import updated existing notes without creating duplicates.
- No Objective 2.7 content was created.
