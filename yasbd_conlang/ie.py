from yasbd.rules.base import Rules


class IeRules(Rules):
    """Rules for Interlingue sentence segmentation."""

    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        "Sr",
        "Sra",
        "Srta",
        "Dr",
    }

    REFERENCE_ABBRVS = Rules.REFERENCE_ABBRVS | {
        "v",
        "pg",
        "cf",
        "sq",
        "conc",
        "nró",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS | {
        "resp",
        "p.ex",
        "i.e",
        "cf",
        "sq",
        "conc",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Capitul",
        "Parte",
        "Section",
        "Articul",
        "Paragraf",
        "Volúmine",
        "Libre",
    }

    COMMON_SENT_STARTERS = {
        # Pronouns
        "Yo",
        "Tu",
        "Il",
        "Ella",
        "It",
        "Noi",
        "Vu",
        "Ili",
        "To",
        "Ti",
        "Tal",
        # Question Words
        "Qui",
        "Quo",
        "Qual",
        "Qualmen",
        "Ubi",
        "Quande",
        # Adverbs and Connectors
        "Yes",
        "No",
        "Ma",
        "Tamen",
        "Forsan",
        "Naturalmen",
        "Do",
        "Pos",
        "Nu",
        "Alora",
        "Finalmente",
        "Prim",
        "Secundmen",
        # Others
        "Li",
        "Un",
        "Altri",
        "Omni",
        "Chascun",
    }
