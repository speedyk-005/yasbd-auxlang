# yasbd-auxlang

**Auxiliary language profiles for [yasbd-lib](https://github.com/speedyk-005/yasbd).**

Adds sentence segmentation support for constructed international auxiliary languages (auxlangs). register and go.

## Languages

| Code | Language       | Status |
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
