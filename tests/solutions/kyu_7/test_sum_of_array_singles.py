"""Sum of array singles"""

import pytest

from solutions.kyu_7.sum_of_array_singles import repeats

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([4, 5, 7, 5, 4, 8], 15),
        ([9, 10, 19, 13, 19, 13], 19),
        ([16, 0, 11, 4, 8, 16, 0, 11], 12),
        ([5, 17, 18, 11, 13, 18, 11, 13], 22),
        ([5, 10, 19, 13, 10, 13], 24),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert repeats(arg) == expected
