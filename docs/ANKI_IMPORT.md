# Importing TSV files into Anki

Generated files under `output/tsv/` contain Anki import headers:

```text
#separator:Tab
#html:true
#tags column:<column number>
#columns:Card ID<TAB>...
```

These headers are supported by Anki 2.1.54 and newer. OpenAPlus deliberately
does not emit a `#notetype` header because stable OpenAPlus note types are not
distributed in this phase.

## Import settings

For each TSV type:

1. Select or create a note type whose fields match the `#columns` line, in the
   same order. Card ID must be its first field.
2. Use a Cloze-derived note type for `Cloze.tsv`; its template must apply the
   cloze filter to the Text field.
3. Confirm the separator is Tab, HTML is enabled, and the final field maps to
   Tags. The file headers normally set these options automatically.
4. Enable updating when the first field matches. Anki will then use the stable
   Card ID to update existing notes without replacing review history.

If an Anki client does not recognize the headers, configure those four settings
manually. The `#columns` line is a comment, not a data row.

## Image cards

Image TSV fields contain HTML such as `<img src="laptop-memory-question.svg">`.
Before importing, copy each referenced source image into Anki's
`collection.media` directory using the basename shown in the TSV. Do not create
subdirectories there. The validator prevents different source images from
sharing a basename.

The question image appears on the front and the answer image on the back. This
is an occlusion-style workflow, not native Anki Image Occlusion.

## Rendering contract

Card bodies remain Markdown in source control. The generator converts common
Markdown—paragraphs, emphasis, inline code, lists, and fenced code blocks—to
HTML and declares `#html:true` for Anki.

## Required smoke tests

Run an Anki import smoke test:

- before the first real objective is accepted;
- after any import-format or TSV schema change;
- for every objective containing image cards; and
- whenever a contributor or reviewer suspects import behavior changed.

Record the result in the objective's `checklist.md` or `changelog.md`.

### Procedure

1. Create a disposable Anki profile or test deck.
2. Import `Basic.tsv`.
3. Import `Cloze.tsv`.
4. Import `Image.tsv` when it exists, after copying its media files.
5. Verify comment and import headers were not imported as notes.
6. Verify Card ID is the first field.
7. Verify the first field is used for duplicate and update detection.
8. Verify HTML renders rather than appearing as markup.
9. Verify every expected Cloze card is generated correctly.
10. Verify generated and custom tags are assigned correctly.
11. Verify `question_image` appears on the front.
12. Verify `answer_image` appears on the back.
13. Re-import the same files and confirm notes update rather than duplicate.
14. Confirm note counts match the data rows in the TSV files.
15. Record the date, Anki version, tester, files tested, note counts, and result.

### Pass/fail criteria

The smoke test passes only when all applicable checks above succeed, the second
import creates no duplicate notes, and observed counts equal expected data rows.
An image check is not applicable when the objective has no Image TSV.

Any unexpected note, missing or duplicate note, literal HTML, incorrect tag,
broken Cloze, missing image, or update failure is a failed test. Record the
failure and do not accept the objective until it is resolved and the complete
smoke test passes.
