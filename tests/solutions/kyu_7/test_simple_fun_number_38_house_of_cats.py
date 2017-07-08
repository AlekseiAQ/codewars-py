"""Simple Fun #38:  House Of Cats"""

import pytest

from solutions.kyu_7.simple_fun_number_38_house_of_cats import house_of_cats

EXAMPLES = (
    ('arg', 'expected'),
    [
        (6, [1, 3]),
        (2, [1]),
        (8, [0, 2, 4]),
        (4, [0, 2]),
        (44, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert house_of_cats(arg) == expected
