# OpenAPlus

OpenAPlus is an open-source learning platform for CompTIA certifications. The
current MVP stores flashcards as Markdown with YAML front matter, validates the
sources, and generates Anki-ready TSV files. Only a minimal pipeline sample is
included; full certification content has not been added.

> [!IMPORTANT]
> OpenAPlus is an independent project and is not affiliated with or endorsed by
> CompTIA. CompTIA and related certification names are trademarks of CompTIA,
> Inc.

## Repository layout

```text
.
├── assets/diagrams/       Original educational diagrams (CC BY 4.0)
├── content/               Markdown learning sources (CC BY 4.0)
├── output/tsv/            Generated Anki-ready files (CC BY 4.0)
├── scripts/               Validation and generation commands (MIT)
├── src/openaplus/         Python package (MIT)
├── tests/                 Python tests
├── website/               Docusaurus application (MIT)
└── .github/               Automation and contribution templates
```

## Requirements

- Python 3.11 or newer
- Node.js 24.14 or newer
- npm

## Local development

Create a Python environment and install the development tools:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
pytest
ruff check .
ruff format --check .
```

## Content pipeline

Each card is a Markdown file whose YAML front matter contains its stable
identity, exam objective, type, difficulty, custom tags, and sources. The
Markdown body contains card fields under level-two headings. See the complete
[card schema](docs/CARD_SCHEMA.md) and [content rules](docs/CONTENT_CREATION_RULES.md).

Validate all source cards:

```bash
python scripts/validate.py
```

Run validation and generate all TSV files:

```bash
python scripts/build.py
```

Generated files are written below. The build replaces this complete tree, so
deleted or renamed objectives cannot leave stale TSV files.

```text
output/tsv/
```

The supported card types are:

- **Basic:** a question, answer, and Instructor Notes.
- **Cloze:** text containing at least one Anki cloze deletion such as
  `{{c1::answer}}`, with Instructor Notes and optional extra context.
- **Image:** a prompt and `question_image` on the front, followed by the answer
  and `answer_image` on the back.

Instructor Notes are required for accepted production cards unless the
objective checklist or changelog explains why they add no value.

Image cards mimic image occlusion with separate concealed and revealed images.
They do not generate native Anki Image Occlusion notes or APKG packages.

Markdown source is converted to HTML in generated TSV fields. Every TSV uses
Card ID as its first field and includes Anki headers for tab separation, HTML,
column names, and tag mapping. Card IDs are immutable because Anki uses that
first field for duplicate detection and updates. See
[Anki import instructions](docs/ANKI_IMPORT.md) and the
[derived tag policy](docs/TAGGING.md).

Before authoring content, read:

- [content creation rules](docs/CONTENT_CREATION_RULES.md);
- [card schema](docs/CARD_SCHEMA.md);
- [Anki import and smoke testing](docs/ANKI_IMPORT.md);
- [tagging and HighYield rules](docs/TAGGING.md);
- [objective completion checklist](docs/OBJECTIVE_COMPLETION_CHECKLIST.md); and
- [card quality examples](docs/CARD_QUALITY_EXAMPLES.md).

Run the documentation site in a second terminal:

```bash
cd website
npm ci
npm run start
```

Build the production site with `npm run build` from `website/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please do not submit copyrighted exam
questions, exam dumps, or material copied from proprietary sources.

## Licensing

- Source code, configuration, and software documentation are licensed under
  the [MIT License](LICENSE).
- Educational content, diagrams, and derived TSV files are licensed under
  [Creative Commons Attribution 4.0 International](LICENSE-CONTENT).

Files that state a different license remain subject to that stated license.
