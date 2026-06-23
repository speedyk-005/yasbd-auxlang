from yasbd.rules.base import Rules


class EoRules(Rules):
    """Rules for Esperanto sentence segmentation."""

    DOTTED_GEOPOL_ABBRVS = (
        Rules.DOTTED_GEOPOL_ABBRVS | {"U.NO"}
    )

    REFERENCE_ABBRVS = Rules.REFERENCE_ABBRVS | {
        "ĉ", "eld", "p", "pag", "kp", "vd", "v",
        "rim", "resp", "ndk",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS | {
        # Logical Connectors
        "t.e", "ekz", "t.n",

        # Streets and Spatial Elements
        "av", "bul", "pl", "str",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Ĉapitro", "Parto", "Sekcio", "Artikolo",
        "Paragrafo", "Volumo", "Libro",
    }

    DATE_ABBRVS = Rules.DATE_ABBRVS | {
        # Months
        "jan", "feb", "mar", "apr", "maj", "jun",
        "jul", "aŭg", "sep", "okt", "nov", "dec",

        # Days of the week
        "lun", "mar", "mer", "ĵaŭ", "ven", "sab", "dim"
    }

    COMMON_SENT_STARTERS = {
        # Pronouns
        "Mi", "Vi", "Li", "Ŝi", "Ĝi", "Ni", "Ili", "Oni",

        # Question words
        "Kiu", "Kiuj", "Kio", "Kie", "Kien", "Kiel", "Kiam", "Kial", "Kiom", "Ĉu",

        # Adverbs
        "Jes", "Ne", "Do", "Tamen", "Eble", "Efektive", "Fakte",
        "Krome", "Ankaŭ", "Sekve", "Tial", "Tuj", "Nun", "Poste", "Antaŭe",
        "Fine", "Unue", "Due", "Trie",

        # Others
        "Tiu", "Tio", "Tie", "Tiam", "Tiel",
    }
