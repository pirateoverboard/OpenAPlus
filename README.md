# OpenAPlus

OpenAPlus is an open-source learning platform for CompTIA certifications. The
repository currently provides the platform foundation; certification learning
content has not yet been added.

> [!IMPORTANT]
> OpenAPlus is an independent project and is not affiliated with or endorsed by
> CompTIA. CompTIA and related certification names are trademarks of CompTIA,
> Inc.

## Repository layout

```text
.
├── docs/                  Educational content (CC BY 4.0)
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

Run the documentation site in a second terminal:

```bash
cd website
npm install
npm run start
```

Build the production site with `npm run build` from `website/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please do not submit copyrighted exam
questions, exam dumps, or material copied from proprietary sources.

## Licensing

- Source code, configuration, and software documentation are licensed under
  the [MIT License](LICENSE).
- Educational content under `docs/` is licensed under
  [Creative Commons Attribution 4.0 International](docs/LICENSE).

Files that state a different license remain subject to that stated license.
