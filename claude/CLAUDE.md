# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git Commit Convention

- Commit messages **MUST** be in **English** and start with a [gitmoji](https://gitmoji.dev/)
- Format: `<emoji> <type>(<scope>): <subject>`
- Examples:
  - `:sparkles: feat(auth): add OAuth2 login support`
  - `:bug: fix(parser): handle empty input gracefully`
  - `:recycle: refactor(utils): simplify date formatting logic`
  - `:memo: docs(README): update installation instructions`
  - `:white_check_mark: test(api): add unit tests for user endpoint`
  - `:construction: chore(deps): upgrade requests to 2.31`

## Python Coding Style

Follow [PEP 8](https://peps.python.org/pep-0008/) and [PEP 257](https://peps.python.org/pep-0257/) as the baseline.

### File Header
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

### File Format
- UTF-8 encoded, Unix line endings (LF), strip trailing whitespace
- 4 spaces indentation, max line length 79 (docstrings/comments: 72)

### Naming Conventions
| Element | Style | Example |
|---|---|---|
| Modules/packages | `lowercase` | `mymodule` |
| Classes | `PascalCase` | `SampleClass` |
| Functions/variables | `snake_case` | `fetch_data` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Private | `_leading_underscore` | `_internal` |

### Import Order
Separate groups with blank lines: 1) stdlib  2) third-party  3) local
```python
import os
import sys

import numpy as np

from myproject.table import Table
```

### Type Hints
Always use modern type hints (for example `str | None`) for function parameters and return values.

### Docstrings (Google-style)
```python
"""Module summary.

Detailed description and usage examples.
"""

class SampleClass:
    """Summary of class.

    Attributes:
        likes_spam: Whether we like SPAM or not.
        eggs: Count of eggs laid.
    """

    def __init__(self, likes_spam: bool = False) -> None:
        """Initialize the instance based on spam preference."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def cook(self, style: str, temperature: int = 100) -> bool:
        """One line summary.

        Longer description if needed.

        Args:
            style: Description of parameter.
            temperature: Description of another parameter.

        Returns:
            Description of return value.

        Raises:
            ValueError: Description of when raised.
        """
```
