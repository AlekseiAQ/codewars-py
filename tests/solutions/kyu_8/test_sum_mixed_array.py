"""Sum Mixed Array"""

import pytest

from solutions.kyu_8.sum_mixed_array import sum_mix

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([9, 3, '7', '3'], 22),
        (['5', '0', 9, 3, 2, 1, '9', 6, 7], 42),
        (['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'], 41),
        (['1', '5', '8', 8, 9, 9, 2, '3'], 45),
        ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_mix(arg) == expected
