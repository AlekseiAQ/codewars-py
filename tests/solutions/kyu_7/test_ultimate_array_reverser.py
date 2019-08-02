"""Ultimate Array Reverser"""

import pytest

from solutions.kyu_7.ultimate_array_reverser import reverse

EXAMPLES = (
    ("arg", "expected"),
    [
        (
            ["I", "like", "big", "butts", "and", "I", "cannot", "lie!"],
            ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"],
        ),
        (
            [
                "?kn",
                "ipnr",
                "utotst",
                "ra",
                "tsn",
                "iksr",
                "uo",
                "yer",
                "ofebta",
                "eote",
                "vahu",
                "oyodpm",
                "ir",
                "hsyn",
                "amwoH",
            ],
            [
                "How",
                "many",
                "shrimp",
                "do",
                "you",
                "have",
                "to",
                "eat",
                "before",
                "your",
                "skin",
                "starts",
                "to",
                "turn",
                "pink?",
            ],
        ),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse(arg) == expected
