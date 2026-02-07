# AGENTS.md

## Python Coding Style

This project follows the style implied by `../py_guide.py`.
When writing or updating Python code, follow these rules.

## 1. File Header and Module Docstring

- Use shebang for executable scripts: `#!/usr/bin/env python`
- Use UTF-8 encoding declaration when needed: `# -*- coding: UTF-8 -*-`
- Write a module docstring in triple quotes.
- The first docstring line is a one-sentence summary ending with a period.
- Leave one blank line after the summary line, then provide details.
- Add a short usage example when it improves clarity.

## 2. Import Order

- Group imports into three blocks with one blank line between blocks.
- Standard library imports first (for example `os`, `sys`, `typing`).
- Third-party imports second (for example `numpy`).
- Local project imports last (for example `from myproject...`).
- Avoid unused imports.

## 3. Naming and Constants

- Use `snake_case` for functions and variables.
- Use `PascalCase` for classes.
- Use uppercase with underscores for module constants (for example `CONST_VALUE`).
- Prefer clear names and avoid spelling mistakes.

## 4. Type Hints

- Add type hints to public function and method parameters and returns.
- Use modern union syntax `|` (for example `bytes | str`, `bool | None`).
- Use explicit container types from `typing` where helpful
  (for example `Mapping[str, tuple[str, ...]]`, `Sequence[...]`).

## 5. Docstring Format (Google Style)

- Add docstrings to modules, public functions, methods, and classes.
- Function docstrings should include sections when relevant:
- `Args:`
- `Returns:`
- `Raises:`
- Class docstrings should include `Attributes:` when useful.
- Keep summaries concise and ensure examples match real behavior.

## 6. Classes and Methods

- Keep `__init__` focused on explicit state initialization.
- Public methods should describe behavior and key constraints.
- Prefer short methods with single responsibility.

## 7. Readability and Consistency

- Keep spacing, indentation, and structure consistent.
- When refactoring, update type hints and docstrings with code changes.

## 8. File Encoding and Whitespace Hygiene

- Keep source files in UTF-8 encoding.
- Use Unix line endings (`LF`) for text files.
- Automatically remove trailing whitespace on save or via formatting tools.
