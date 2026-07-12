# Smoke Test Commit Policy

When a manual Anki smoke test passes for an objective, commit the accepted
objective changes to git before starting the next objective.

If the user says "smoke test passes" or "smoke tests pass" for the current
objective, treat that as an instruction to complete the acceptance workflow:

1. update `checklist.md` and `changelog.md` with the smoke-test pass,
   accepted status, final card counts, and generated-output status;
2. regenerate output and run the standard verification set;
3. stage only the accepted objective's files and required supporting changes;
4. commit the staged acceptance changes to git.

The commit should include the complete accepted objective state:

- objective-local Markdown files, including `study-guide.md`, `checklist.md`,
  `changelog.md`, cards, and any objective-local support files;
- generated TSV files under `output/tsv/` for that objective;
- generated media under `output/media/` when the objective has Image cards;
- source diagrams or reviewed media assets when applicable; and
- required supporting docs, tests, or pipeline changes that were made for that
  objective.

Do not include unrelated objectives or unrelated working-tree changes in the
smoke-test acceptance commit. If earlier uncommitted work exists for another
objective, leave it unstaged unless it is required by the accepted objective.

Before committing, run the standard verification set for content changes:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
```

Then verify the staged file set is scoped correctly:

```bash
git status --short
git diff --cached --name-only
```

The commit message should identify the accepted exam objective, for example:

```text
Accept Core 2 objective 1.3
```

An objective is not considered ready to move past acceptance until the smoke
test pass is recorded in `checklist.md` and `changelog.md`, generated output is
current, verification passes, and the acceptance commit is created.
