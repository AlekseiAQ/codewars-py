"""Credit Card Checker"""

import pytest

from solutions.kyu_7.credit_card_checker import valid_card

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("5457 6238 9823 4311", True),
        ("8895 6238 9323 4311", False),
        ("5457 6238 5568 4311", False),
        ("5457 6238 9323 4311", False),
        ("2222 2222 2222 2224", True),
        ("5457 1125 9323 4311", False),
        ("1252 6238 9323 4311", False),
        ("9999 9999 9999 9995", True),
        ("0000 0300 0000 0000", False),
        ("4444 4444 4444 4448", True),
        ("5457 6238 9323 1252", False),
        ("5457 6238 1251 4311", False),
        ("3333 3333 3333 3331", True),
        ("6666 6666 6666 6664", True),
        ("5457 6238 0254 4311", False),
        ("0000 0000 0000 0000", True),
        ("5457 1111 9323 4311", False),
        ("5457 6238 9823 4311", True),
        ("1145 6238 9323 4311", False),
        ("8888 8888 8888 8888", True),
        ("0025 2521 9323 4311", False),
        ("5457 6238 9323 4311", False),
        ("1111 1111 1111 1117", True),
        ("1234 5678 9012 3452", True),
        ("5458 4444 9323 4311", False),
        ("5457 6238 3333 4311", False),
        ("0123 4567 8901 2345", False),
        ("5555 5555 5555 5557", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert valid_card(arg) == expected
