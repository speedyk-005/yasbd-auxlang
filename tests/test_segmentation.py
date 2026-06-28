import pytest

from tests import ALL_TEST_DATA
from yasbd import BoundaryDetector, register_lang_packs

# Register self
register_lang_packs(["yasbd_auxlang"])


@pytest.mark.parametrize("lang,test_data", ALL_TEST_DATA.items())
def test_segment_multiple_langs(subtests, lang, test_data):
    """test that each language's test data passes."""
    seg = BoundaryDetector(lang=lang)
    for marked_text in test_data:
        # Extract the expected sentences by splitting on the marker
        expected = [sent.strip() for sent in marked_text.split("|")]

        # Reconstruct the clean original input text by removing the marker
        input_text = marked_text.replace("|", "")

        with subtests.test():
            result = list(seg.segment(input_text))
            assert result == expected, f"Input: {input_text}"
