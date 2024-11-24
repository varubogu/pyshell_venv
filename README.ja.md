# pyshell_venv

venv環境でPythonシェルスクリプトを再実行する

[English](README.md) | 日本語

## 概要

Pythonのコードから呼び出された場合、仮想環境を作成し再実行するためのコードです。
このコード自体はライブラリを追加することなく`src/pyshell_venv.py`単体で動作します。

ホストのPython環境を汚さずに自由にライブラリをインストールし、
Pythonのシェルスクリプトを実行することを目的としています。

venvの実態のディレクトリは以下の優先度で設定します。

1. $XDG_DATA_HOMEに設定します。
2. $XDG_DATA_HOMEが設定できない場合は~/.local/shareに設定します。
3. それでも設定できない場合はエラーを出します。

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
