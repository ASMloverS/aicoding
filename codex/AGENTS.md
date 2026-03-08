# AGENTS.md

## Python Coding Style

Python code in this project must follow PEP 8, with clear comments and docstrings.

## Code Rules

- Follow PEP 8 for formatting, naming, imports, and layout.
- Keep line length within PEP 8 limits (usually 79 for code, 72 for docs where practical).
- Use 4-space indentation; never use tabs.
- Group imports as standard library, third-party, and local, with one blank line between groups.
- Remove unused imports and dead code.
- Use `snake_case` for functions/variables/modules, `PascalCase` for classes, and `UPPER_CASE` for constants.
- Prefer small, single-responsibility functions and methods.
- Write comments in clear English, accurate to behavior, and synchronized with code changes.
- Use inline comments only when logic is not self-evident; avoid obvious comments.
- Add docstrings for public modules/classes/functions/methods.
- Use a consistent docstring style (Google preferred), with `Args:`, `Returns:`, and `Raises:` when applicable.
- Keep docstring summaries concise and end the first sentence with a period.
- Add type hints for public function/method parameters and return values.
- Prefer modern types (for example `str | None`) and explicit `typing` types when they improve readability.
- Use UTF-8 encoding, LF line endings for text files, and remove trailing whitespace.

## Commit Message Rules

- Commit messages must be written in English.
- Every commit message must include a gitmoji prefix.
- Recommended format: `<gitmoji> <type>(<scope>): <summary>`.
- Keep the summary concise and action-oriented.
