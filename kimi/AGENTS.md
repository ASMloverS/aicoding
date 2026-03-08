# Python Coding Standards

Follow the [PEP8](https://peps.python.org/pep-0008/) style guide.

## File Format

- **Encoding**: UTF-8
- **Line endings**: Unix style (LF)
- **File header**:

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

## Import Order

1. Standard library
2. Third-party libraries
3. Local project

```python
import os
import sys
from typing import Mapping, Sequence

import numpy as np
from myproject.table import Table
from myproject.util import helper
```

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Constants | ALL_CAPS_WITH_UNDERSCORES | `CONST_VALUE = 256` |
| Functions/Variables | snake_case | `fetch_data()`, `item_count` |
| Classes | PascalCase | `SampleClass` |

## Docstrings (Google Style)

Use `"""triple double quotes"""`. Functions include Args/Returns/Raises, classes include Attributes.

```python
def fetch_data(keys: Sequence[str]) -> Mapping[str, tuple[str, ...]]:
    """Fetch rows by keys.

    Args:
        keys: Sequence of keys to fetch.

    Returns:
        Dict mapping keys to row data.

    Raises:
        IOError: If table access fails.
    """
```

## Type Annotations

Use Python 3.10+ union type syntax:

```python
def func(param: bytes | str, optional: bool | None = None) -> list[int]:
    ...
```

## super() Calls

Use explicit class name style:

```python
super(SampleClass, self).__init__()
```

---

# Git Commit Conventions

## Format

```
<gitmoji> <english description>
```

## Common gitmoji

| Emoji | Code | Usage |
|-------|------|-------|
| ✨ | `:sparkles:` | Introduce new features |
| 🐛 | `:bug:` | Fix bugs |
| 📝 | `:memo:` | Add/update documentation |
| ♻️ | `:recycle:` | Refactor code |
| ✅ | `:white_check_mark:` | Add/update tests |
| 🔧 | `:wrench:` | Update configuration |
| 🚀 | `:rocket:` | Deployment related |
| ⬆️ | `:arrow_up:` | Upgrade dependencies |

## Examples

```bash
git commit -m ":sparkles: Add user authentication module"
git commit -m ":bug: Fix null pointer exception in login"
git commit -m ":memo: Update API documentation"
```
