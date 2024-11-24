# pyshell_venv

Re-run the Python shell script in the venv environment

English | [日本語](README.ja.md)

## Overview

This code creates a virtual environment and re-executes it when called from Python code.
This code itself works by itself as `src/pyshell_venv.py` without adding any libraries.

The purpose is to allow you to freely install libraries and run Python shell scripts without polluting the host's Python environment.

The actual venv directory is set with the following priority.

The directory where the venv's actual files are stored is set with the following priority:
1. It is set in $XDG_DATA_HOME.
2. If $XDG_DATA_HOME cannot be set, it is set in ~/.local/share.
3. If it cannot be set even then, an error is raised.


## Example

`src/example.py`

```python
from pyshell_venv import PyShellVenv

if not PyShellVenv.is_in_venv():
    require_package = "numpy"
    psv = PyShellVenv(require_package_text=require_package)
    result: int = psv.execute()
    sys.exit(result)

# This code runs in a virtual environment.
import numpy as np
ary = np.array([1, 2, 3])
print(ary)
sys.exit(0)
```
