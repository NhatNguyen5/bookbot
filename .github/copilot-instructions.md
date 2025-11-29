<!-- Copilot / AI agent instructions for working on the `bookbot` repo -->
# Quick Overview

BookBot is a small single-purpose CLI Python project (no dependencies) that analyzes plain-text books placed under the `books/` directory. The runtime is a simple script `main.py` that imports helpers from `stats.py` and prints analysis to stdout.

# Key Files

- `main.py` — CLI entrypoint. Reads `sys.argv[1]` (path to book), calls helper functions from `stats.py`, and prints results. Example run:

  `python3 main.py books/frankenstein.txt`

- `stats.py` — pure-Python helpers:
  - `get_book_text(path_to_file)` — reads and returns file contents.
  - `get_num_words(str)` — splits on whitespace to count words.
  - `count_alpbt(str)` — builds a dict of per-character counts. Special keys: newline becomes `"\\n"` and space becomes `"' '"` for display.
  - `sort_char_pairs(str_dict)` — converts the char->count dict into a list of `{"char": <char>, "num": <count>}` and sorts by `num` descending.

- `books/` — sample ebooks (plain text) used for manual testing.

# Big-picture architecture and data flow

- Single-process CLI: `main.py` parses args -> `get_book_text` -> `get_num_words` & `count_alpbt` -> `sort_char_pairs` -> `display`.
- Data shape to expect across functions:
  - `count_alpbt` returns `dict[str, int]` (keys may be special tokens like `"\\n"` and `"' '"`).
  - `sort_char_pairs` consumes that dict and returns `List[Dict{"char": str, "num": int}]`.

# Project-specific conventions & quirks (important for autosuggestions)

- No package structure or virtualenv: code runs with system Python; there is no `requirements.txt`.
- Plain dictionaries are used instead of dataclasses/tuples for small objects (see `char_pair` construction in `sort_char_pairs`). Keep this pattern when adding small helpers for consistency.
- Display formatting: `display()` in `main.py` expects the list-of-dicts shape created by `sort_char_pairs`.
- Special-character representation: newline and space are intentionally converted into printable tokens inside `count_alpbt` for easier console display — preserve this when modifying display logic.

# Known issues to watch for (discoverable in-source)

- `main.py` contains a syntax bug in the `display` loop: it currently prints `f"{pair["char"]: {pair["num"]}\n"` which uses nested double quotes and will raise a `SyntaxError`. When editing this file, use single quotes inside the f-string, for example:

  `print(f"{pair['char']}: {pair['num']}\n")`

- `main.py` assumes `sys.argv[1]` exists; code catches `IndexError` to print usage, but adding a clearer arg-parsing (e.g., `argparse`) is safe and acceptable.

# Typical developer workflows (what to run locally)

- Run CLI against sample books:

  `python3 main.py books/mobydick.txt`

- There are no automated tests or CI configured. If adding tests, keep them lightweight (e.g., pytest) and target `stats.py` helpers first.

# Safe edits and suggestions an AI agent can make automatically

- Fixing small syntax bugs (like the `display` f-string) is reasonable.
- Improving robustness (use `with open(..., encoding='utf-8')` and `argparse`) is acceptable but keep changes small and well-tested locally.
- When changing data shapes (e.g., switching from dicts to dataclasses), update both `stats.py` and `main.py` together and include small unit tests demonstrating the new shape.

# If you need to modify behavior, check these files first

- `stats.py` — change counting/sorting logic here.
- `main.py` — change CLI parsing and display formatting.

# PR & commit guidance for AI agents

- Keep diffs minimal and focused (one small bugfix or feature per PR).
- If you fix the `display` syntax bug, include a one-line test or demonstrate the CLI output in the PR description.

# Assumptions made by these instructions

- Repository is intentionally minimal; there are no hidden build steps or dependencies.
- All data files are UTF-8 plain text.

---
If any of these assumptions are incorrect (for example you rely on a specific Python version, or there are hidden CI steps), tell me what to inspect next and I'll update these instructions.
