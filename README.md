# yasbd-auxlang 

[![Python Version](https://img.shields.io/badge/Python-3.11%20--%203.14-blue)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/yasbd-auxlang?kill_cache=2)](https://pypi.org/project/yasbd-auxlang)
[![Tests](https://img.shields.io/github/actions/workflow/status/speedyk-005/yasbd-auxlang/build-and-test.yml?branch=main&label=tests)](https://github.com/speedyk-005/yasbd-auxlang/actions)
[![Stability](https://img.shields.io/badge/stability-beta-yellowgreen)](https://github.com/speedyk-005/yasbd-auxlang)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)



**Auxiliary language profiles for [yasbd-lib](https://github.com/speedyk-005/yasbd).**

Adds sentence segmentation support for constructed international auxiliary languages (auxlangs). register and go.

## Languages

|Code | Language       | Status |
|------|----------------|--------|
| `eo` | Esperanto      | ✅     |
| `ie` | Interlingue    | ✅     |
| `ia` | Interlingua    | ✅     |
| `io` | Ido            | ✅     |

## Installation

```bash
pip install yasbd-auxlang
```

## Usage

```python
from yasbd import BoundaryDetector
from yasbd.rules import register_lang_packs

register_lang_packs(["yasbd_auxlang"])

detector = BoundaryDetector("eo")
sentences = list(detector.segment("Saluton mondo! Kiel vi fartas? Mi bone."))
# ["Saluton mondo!", "Kiel vi fartas?", "Mi bone."]
```

## Development

```bash
git clone https://github.com/speedyk-005/yasbd-auxlang
cd yasbd-auxlang
pip install -e ".[dev]"
pytest
```

This project is licensed under the MIT License.
