"""Constructed language profiles for yasbd-lib.

Usage:
    from yasbd.rules import register_lang_packs

    register_lang_packs(["yasbd_conlang"])
"""

from yasbd_conlang.eo import EoRules
from yasbd_conlang.ie import IeRules
from yasbd_conlang.ia import IaRules
from yasbd_conlang.io import IoRules

PROFILES = [
    EoRules,
    IeRules,
    IaRules,
    IoRules,
]
