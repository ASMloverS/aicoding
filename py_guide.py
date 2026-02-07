#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

import os
import sys
from typing import Mapping, Sequence

import numpy as np
from myproject.table import Table
from myproject.util import helper

CONST_VALUE = 256


def fetch_samlltable(table_handle: Table, keys: Sequence[bytes | str], require_all_keys: bool | None = None) -> Mapping[str, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        ├─ table_handle: Table           -> An open smalltable.Table instance.
        ├─ keys: Sequence[bytes | str]   -> A sequence of strings representing the key of each table row to fetch.  String keys will be UTF-8 encoded.
        └─ require_all_keys: bool | None -> If True only rows with values set for all keys will be returned.
    Returns:
        └─ Mapping[str, tuple[str, ...]] -> A dict mapping keys to the corresponding table row data fetched. Each row is represented as a tuple of strings.

        For example:
            {
                Serak': ('Rigel VII', 'Preparer'),
                'Zim': ('Irk', 'Invader'),
                'Lrrr': ('Omicron Persei 8', 'Emperor')
            }

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).
    Raises:
        └─ IOError -> An error occurred accessing the smalltable.
    """

class SampleClass(object):
    """Summary of class here.

    Longer class information....
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

    def public_method(self) -> None:
        """Performs operation blah."""
