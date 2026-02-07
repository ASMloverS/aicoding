# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

<!-- Add project description here -->

## Development Commands

<!-- Add common commands as the project develops:
- Build: `command here`
- Test: `command here`
- Lint: `command here`
- Run single test: `command here`
-->

## Architecture

<!-- Add high-level architecture notes here as the project develops -->

## Python Coding Style

### File Header
```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

### File Format
- All files must be UTF-8 encoded
- Use Unix line endings (LF), not Windows (CRLF)
- Strip trailing whitespace from all lines

### Module Docstring
```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

### Import Order
1. Standard library imports (e.g., `os`, `sys`)
2. Third-party imports (e.g., `numpy`)
3. Local imports (e.g., `from myproject.table import Table`)

```python
import os
import sys
from typing import Mapping, Sequence

import numpy as np
from myproject.table import Table
from myproject.util import helper
```

### Constants
Use `UPPER_CASE_WITH_UNDERSCORES` for module-level constants:
```python
CONST_VALUE = 256
```

### Type Hints
Always use type hints for function parameters and return values:
```python
def fetch_samlltable(
    table_handle: Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool | None = None
) -> Mapping[str, tuple[str, ...]]:
```

### Function Docstring Format
Use tree characters (├─, └─) for structured documentation:
```python
def function_name(param: type) -> return_type:
    """One line summary.

    Longer description if needed.

    Args:
        ├─ param: type   -> Description of parameter.
        └─ another: type -> Description of another parameter.
    Returns:
        └─ type -> Description of return value.
    Raises:
        └─ Exception -> Description of when exception is raised.
    """
```

### Class Docstring Format
Include an `Attributes` section for instance variables:
```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        ├─ likes_spam: bool -> A boolean indicating if we like SPAM or not.
        └─ eggs: int        -> An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False) -> None:
        """Initializes the instance based on spam preference."""
        super(SampleClass, self).__init__()
        self.likes_spam = likes_spam
        self.eggs = 0
```
