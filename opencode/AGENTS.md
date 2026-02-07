# AGENTS.md - Agent Coding Guidelines

## Build/Lint/Test Commands

**NOTE**: This project currently has no standard Python build configuration files (pyproject.toml, setup.py, requirements.txt, tox.ini).

Standard commands to add as project matures:
```bash
# Install dependencies
pip install -e .

# Run linters
ruff check .
pylint project_name

# Run formatters
black .
isort .

# Run all tests
pytest

# Run single test
pytest tests/test_module.py::test_function
```

## Code Style Guidelines

### File Format

- **Encoding**: All files must use UTF-8 encoding (no BOM)
- **Line Endings**: Unix style (LF only, no CRLF)
- **Whitespace**: Auto-trim trailing whitespace on every line
- Configure editor/IDE to enforce these settings automatically

### File Header

All Python files must start with:
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""One line summary of the module or program, terminated by a period.

Leave one blank line. The rest of this docstring should contain an
overall description of the module or program. Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

### Import Order

1. Standard library imports (os, sys, typing, etc.)
2. Third-party imports (numpy, pandas, etc.)
3. Local project imports

```python
import os
import sys
from typing import Mapping, Sequence

import numpy as np
from myproject.table import Table
from myproject.util import helper
```

### Constants

- UPPER_SNAKE_CASE for constants
- Place after imports, before classes/functions
```python
CONST_VALUE = 256
MAX_RETRIES = 3
```

### Type Annotations

- REQUIRED for all function signatures
- Use Python 3.10+ union syntax (`|`) instead of `Union[]`
- Use generic types (`Sequence`, `Mapping`, etc.) instead of `list`, `dict`

```python
def fetch_data(keys: Sequence[bytes | str], require_all: bool | None = None) -> Mapping[str, tuple[str, ...]]:
    """Function docstring."""
    pass
```

### Function Docstrings

Use Google-style docstrings with section headers:

```python
def function_name(param1: Type1, param2: Type2 = default) -> ReturnType:
    """One-line summary of the function.

    Longer description of what the function does.

    Args:
        ├─ param1: Type1 -> Description of param1.
        ├─ param2: Type2 -> Description of param2.
        └─ optional_param: Type3 -> Description of optional parameter.

    Returns:
        └─ ReturnType -> Description of what is returned.

    Raises:
        └─ IOError -> Description of when this error is raised.
    """
```

### Class Docstrings

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        ├─ attr1: type -> Description of attr1.
        └─ attr2: type -> Description of attr2.
    """

    def __init__(self, param: type) -> None:
        """Initializes the instance."""
        super(SampleClass, self).__init__()
        self.attr = param
```

### Naming Conventions

| Entity | Convention | Example |
|--------|------------|---------|
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Functions/Methods | snake_case | `fetch_smalltable` |
| Classes | PascalCase | `SampleClass` |
| Private methods | _snake_case | `_internal_method` |

### Key Requirements

- **NO TYPE SUPPRESSION**: Never use `# type: ignore` or `Any` without justification
- **Explicit inheritance**: Always inherit from `object` for classes in Python 2/3 compatibility
- **Super calls**: Use `super(ClassName, self).__init__()` pattern
- **Docstrings required**: Every class, function, and module must have a docstring
