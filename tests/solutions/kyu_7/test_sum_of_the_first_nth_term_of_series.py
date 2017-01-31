"""Sum of the first nth term of Series"""

import pytest

from solutions.kyu_7.sum_of_the_first_nth_term_of_series import series_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, "1.00"),
        (2, "1.25"),
        (3, "1.39"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert series_sum(arg) == expected
