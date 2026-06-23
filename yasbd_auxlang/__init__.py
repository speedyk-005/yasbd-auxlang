"""Constructed language profiles for yasbd-lib.

Usage:
    from yasbd.rules import register_lang_packs

    register_lang_packs(["yasbd_auxlang"])
"""

from yasbd_auxlang.eo import EoRules
from yasbd_auxlang.ie import IeRules
from yasbd_auxlang.ia import IaRules
from yasbd_auxlang.io import IoRules

PROFILES = [
    EoRules,
    IeRules,
    IaRules,
    IoRules,
]
