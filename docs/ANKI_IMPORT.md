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

1. Select or create a custom OpenAPlus note type whose fields match the
   `#columns` line, in the same order. Card ID must be its first field.
2. Use separate OpenAPlus Basic, Cloze, and Image note types. The Cloze note
   type must be Cloze-derived, and its template must apply the cloze filter to
   the Text field.
3. Confirm the separator is Tab, HTML is enabled, and the final field maps to
   Anki's special Tags metadata row. Tags should not be imported as a normal
   learner-facing note field. The file headers normally set these options
   automatically.
4. Enable updating when the first field matches. Anki will then use the stable
   Card ID to update existing notes without replacing review history.

The `Objective` field is a rendered display field, not the raw source metadata.
It uses:

```text
<exam> <objective> - <objective_name>
```

Example:

```text
220-1201 1.1 - Laptop Hardware
```

If an Anki client does not recognize the headers, configure those four settings
manually. The `#columns` line is a comment, not a data row.

## Image cards

Image TSV fields contain HTML such as `<img src="1.1-I001-question.svg">`.
Before importing, copy the staged files from
`output/media/<exam>/<objective>/` into Anki's `collection.media` directory
using the filenames shown in the TSV. Do not create subdirectories there.

The build uses deterministic staged filenames:

- `<card-id>-question.<ext>`
- `<card-id>-answer.<ext>`

TSV files must reference filenames only. They must not contain source asset
paths such as `assets/diagrams/...`.

The question image appears on the front and the answer image on the back. This
is an occlusion-style workflow, not native Anki Image Occlusion.

## Installing Media for Manual Anki Smoke Tests

After running `python scripts/build.py`, install staged media into the local
Anki profile used for smoke testing. The helper copies files from
`output/media/<exam>/<objective>/` into the profile's `collection.media`
directory.

```bash
python scripts/install_anki_media.py --profile "User 1" --objective 1.1-laptop-hardware
```

Preview the copy without modifying Anki media:

```bash
python scripts/install_anki_media.py --profile "User 1" --objective 1.1-laptop-hardware --dry-run
```

Use an explicit destination when the profile is outside the default Anki
location:

```bash
python scripts/install_anki_media.py --media-dir "$HOME/.local/share/Anki2/User 1/collection.media" --objective 1.1-laptop-hardware
```

By default, the installer is conservative:

- identical existing files are skipped;
- differing existing files fail the install;
- `--overwrite` is required to replace differing files;
- missing source or destination directories fail the install;
- unsupported file types fail the install.

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
4. Import `Image.tsv` when it exists, after copying its staged media files from
   `output/media/<exam>/<objective>/`.
5. Verify comment and import headers were not imported as notes.
6. Verify Card ID is the first field.
7. Verify the first field is used for duplicate and update detection.
8. Verify HTML renders rather than appearing as markup.
9. Verify every expected Cloze card is generated correctly.
10. Verify generated and custom tags are assigned correctly.
11. Verify tags are Anki metadata, not visible learner-facing fields.
12. Verify the OpenAPlus Basic, Cloze, and Image note types render as expected.
13. Verify `question_image` appears on the front.
14. Verify `answer_image` appears on the back.
15. Re-import the same files and confirm notes update rather than duplicate.
16. Confirm note counts match the data rows in the TSV files.
17. Record the date, Anki version, tester, files tested, note counts, and result.

### Pass/fail criteria

The smoke test passes only when all applicable checks above succeed, the second
import creates no duplicate notes, and observed counts equal expected data rows.
An image check is not applicable when the objective has no Image TSV.

Any unexpected note, missing or duplicate note, literal HTML, incorrect tag,
tag imported as a normal learner-facing field, broken Cloze, missing image, or
update failure is a failed test. Record the failure and do not accept the
objective until it is resolved and the complete smoke test passes.
