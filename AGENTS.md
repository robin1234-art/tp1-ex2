# AGENTS.md

## Structure

- **Package** : `toolbox/` — `text_utils.py`, `convert_utils.py`
- **Tests** : `tests/` — `test_text_utils.py`, `test_convert_utils.py`
- **Issues** : `issues/` — bug descriptions for each exercise

## Commands

```bash
pytest              # run all tests (also CI: python 3.12, pip install pytest)
pytest -x           # stop on first failure
pytest tests/test_text_utils.py   # single test file
```

## Gotchas

- `opencode.json` is gitignored — do not commit it
- `is_palindrome` strips nothing — fix needs `.replace(" ", "")` before comparison (issue #1)
- `tag_reading` has a mutable default `tags: list = []` — fix with `tags: list | None = None` and `if tags is None: tags = []` internally (issue #2)
- `word_frequency` and `celsius_to_fahrenheit` / `moving_average` raise `NotImplementedError` — they are unimplemented stubs
