"""Numbers in strings"""

import pytest

from solutions.kyu_7.numbers_in_strings import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('gh12cdy695m1', 695),
        ('2ti9iei7qhr5', 9),
        ('vih61w8oohj5', 61),
        ('f7g42g16hcu5', 42),
        ('lu1j8qbbb85', 85),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
