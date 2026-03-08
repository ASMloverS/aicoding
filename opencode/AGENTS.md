# AGENTS.md - Agent Coding Guidelines

## Build/Lint/Test Commands

```bash
pip install -e .          # Install dependencies
ruff check .              # Run linter
black . && isort .        # Run formatters
pytest                    # Run all tests
pytest tests/test_module.py::test_function  # Run single test
```

## Git Commit Messages

- **Language**: English only
- **Format**: `<gitmoji> <type>: <description>`
- Common gitmojis: ✨ feat, 🐛 fix, 📝 docs, ♻️ refactor, ✅ test, 🔧 chore

Example: `✨ feat: add user authentication module`

## Code Style Guidelines (PEP 8)

### File Format

- Encoding: UTF-8 (no BOM)
- Line Endings: LF only
- Indentation: 4 spaces
- Line Length: 79 (code), 72 (docstrings/comments)
- Trim trailing whitespace

### File Header

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module summary. Extended description if needed."""
```

### Import Order

1. Standard library
2. Third-party
3. Local project

```python
import os
from typing import Sequence

import numpy as np

from myproject.table import Table
```

### Type Annotations

**Required** for all functions. Use Python 3.10+ syntax:

```python
def fetch_data(keys: Sequence[str | bytes], flag: bool | None = None) -> dict[str, tuple[str, ...]]:
    """Fetch data from keys."""
    pass
```

### Naming Conventions

| Entity | Convention | Example |
|--------|------------|---------|
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Functions/Variables | snake_case | `fetch_data`, `user_count` |
| Classes | PascalCase | `SampleClass` |
| Exceptions | PascalCase + Error | `InvalidDataError` |
| Private/Protected | _leading_underscore | `_internal_method` |

### Docstrings

Triple double quotes. Summary first, then details.

```python
def func(param1: Type1, param2: Type2 = default) -> ReturnType:
    """One-line summary.

    Args:
        param1: Description.
        param2: Description.

    Returns:
        Description.

    Raises:
        IOError: When raised.
    """
    pass
```

### Comments

- Block: `# comment` at code indentation level
- Inline: `x = x + 1  # two spaces before #`

### Whitespace

```python
spam(ham[1], {eggs: 2})  # Correct
foo = (0,)               # Correct
spam( ham[ 1 ] )         # Wrong
```

### Other Recommendations

- Use `is`/`is not` for `None` comparisons
- Use `isinstance()` for type checking
- Use `startswith()`/`endswith()` for prefix/suffix checks
- Use `with` statement for resource cleanup
