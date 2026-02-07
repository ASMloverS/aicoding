# Python 编码风格指南

## 文件格式规范

- **编码**：文件必须使用 UTF-8 编码
- **换行符**：使用 Unix 风格换行符（LF），不使用 Windows 风格（CRLF）
- **行尾空白**：自动清除行尾空白符（trailing whitespace）

## 文件头

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

## 模块/程序文档字符串

模块文档字符串应包含以下内容：
1. 单行摘要，以句号结尾
2. 空一行
3. 整体描述（模块或程序的描述）
4. 可选：导出的类和函数简介、使用示例

格式示例：
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

## 导入顺序

1. 标准库导入
2. 第三方库导入
3. 本地项目导入

示例：
```python
import os
import sys
from typing import Mapping, Sequence

import numpy as np
from myproject.table import Table
from myproject.util import helper
```

## 常量命名

常量使用全大写字母，单词间用下划线分隔：
```python
CONST_VALUE = 256
```

## 函数文档字符串（Google 风格）

函数文档字符串应包含：
- 简短描述
- Args: 参数说明（含类型）
- Returns: 返回值说明（含类型）
- Raises: 可能抛出的异常

使用 `├─` 和 `└─` 作为列表符号：
```python
def fetch_samlltable(table_handle: Table, keys: Sequence[bytes | str], require_all_keys: bool | None = None) -> Mapping[str, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        ├─ table_handle: Table           -> An open smalltable.Table instance.
        ├─ keys: Sequence[bytes | str]   -> A sequence of strings representing the key of each table row to fetch.
        └─ require_all_keys: bool | None -> If True only rows with values set for all keys will be returned.
    Returns:
        └─ Mapping[str, tuple[str, ...]] -> A dict mapping keys to the corresponding table row data fetched.

        For example:
            {
                'Serak': ('Rigel VII', 'Preparer'),
                'Zim': ('Irk', 'Invader'),
                'Lrrr': ('Omicron Persei 8', 'Emperor')
            }

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).
    Raises:
        └─ IOError -> An error occurred accessing the smalltable.
    """
```

## 类文档字符串

类文档字符串应包含：
- 类摘要
- 详细描述
- Attributes: 属性说明

示例：
```python
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
```

## 类型注解

- 使用 Python 3.10+ 的联合类型语法（`|` 运算符）
- 函数参数和返回值都应添加类型注解

示例：
```python
def func(param: bytes | str, optional: bool | None = None) -> Mapping[str, tuple[str, ...]]:
    ...
```

## super() 调用

使用显式类名的旧式风格：
```python
super(SampleClass, self).__init__()
```
