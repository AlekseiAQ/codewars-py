"""Help the bookseller !"""

import pytest

from solutions.kyu_6.help_the_bookseller import stock_list

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

EXAMPLES = (
    ('args', 'expected'),
    [
        ((b, c), "(A : 200) - (B : 1140)"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert stock_list(*args) == expected
