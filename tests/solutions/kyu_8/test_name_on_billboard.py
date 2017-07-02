"""Name on billboard"""

import pytest

from solutions.kyu_8.name_on_billboard import billboard

EXAMPLES = (
    ('args', 'expected'),
    [
        (("Jeong-Ho Aristotelis",), 600),
        (("Abishai Charalampos",), 570),
        (("Idwal Augustin",), 420),
        (("Hadufuns John", 20), 260),
        (("Zoroaster Donnchadh",), 570),
        (("Claude Miljenko",), 450),
        (("Werner Vigi", 15), 165),
        (("Anani Fridumar",), 420),
        (("Paolo Oli",), 270),
        (("Hjalmar Liupold", 40), 600),
        (("Simon Eadwulf",), 390),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert billboard(*args) == expected
