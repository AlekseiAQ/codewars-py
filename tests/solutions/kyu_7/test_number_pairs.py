"""Number Pairs"""

import pytest

from solutions.kyu_7.number_pairs import get_larger_numbers

EXAMPLES = (
    ('a', 'b', 'expected'),
    [
        ([13, 64, 15, 17, 88], [23, 14, 53, 17, 80], [23, 64, 53, 17, 88]),
        ([34, -64, 15, 17, 88], [23, 14, 53, 17, 80], [34, 14, 53, 17, 88]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, expected):
    assert get_larger_numbers(a, b) == expected
