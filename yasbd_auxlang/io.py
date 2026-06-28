from yasbd.rules.base import Rules


class IoRules(Rules):
    """Rules for Ido sentence segmentation."""

    REFERENCE_ABBRVS = Rules.REFERENCE_ABBRVS | {
        "p",
        "kp",
        "vd",
        "nr",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS | {
        # Logical Connectors
        "t.e",
        "ekz",
        "t.n",
        "ex",
        # Streets and Spatial Elements
        "av",
        "bul",
        "pl",
        "str",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Chapitro",
        "Parto",
        "Sekciono",
        "Artiklo",
        "Paragrafo",
        "Volumo",
        "Libro",
    }

    COMMON_SENT_STARTERS = {
        # Pronouns
        "Me",
        "Tu",
        "Vu",
        "Il",
        "Ilu",
        "El",
        "Elu",
        "Ol",
        "Olu",
        "Ni",
        "Vi",
        "Li",
        "Li",
        "Ili",
        "Eli",
        "Oli",
        "Onu",
        # Question words
        "Qua",
        "Quo",
        "Qui",
        "Qua",
        "Ube",
        "Kande",
        "Quale",
        "Pro quo",
        "Ka",
        # Adverbs
        "Yes",
        "No",
        "Do",
        "Ma",
        "Tamen",
        "Anke",
        "Plu",
        "Tre",
        "Multo",
        "Multe",
        "Malgre",
        "Preske",
        "Totale",
        "Sempre",
        "Nun",
        "Lore",
        "Pos",
        "Ante",
        "Seguante",
        "Fine",
        "Unesme",
        "Duesme",
        "Triesme",
        # Others
        "To",
        "Ta",
        "Tala",
        "Tante",
        "Tanta",
    }
