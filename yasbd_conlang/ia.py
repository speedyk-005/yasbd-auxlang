from yasbd_conlang.ie import IeRules


class IaRules(IeRules):
    """Rules for Interlingua sentence segmentation."""

    SECTION_MARKERS = IeRules.SECTION_MARKERS | {
        "Capitulo", "Articulo", "Paragrapho",
        "Volumine", "Libro",
    }

    COMMON_SENT_STARTERS = {
        # Pronouns
        "Io", "Tu", "Ille", "Illa", "Illo", "Nos", "Vos", "Illes", "Ilias",

        # Question words
        "Qui", "Que", "Qual", "Quando", "Ubi", "Como", "Perque", "Quanto", "Esque",

        # Adverbs
        "Si", "No", "Multo", "Anque", "Etiam", "Solmente", "Semper",
        "Jamais", "Sovente", "Totevia", "Dunque", "Alora", "Postea", "Antea",
        "Actually", "Finalmente", "Primo", "Secundo", "Tertio",

        # Others
        "Hic", "Ibi", "Illic", "Hodie", "Deman", "Heri",
    }
