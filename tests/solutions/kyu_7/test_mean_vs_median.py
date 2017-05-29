"""Mean vs. Median"""

import pytest

from solutions.kyu_7.mean_vs_median import mean_vs_median

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 1, 1], "same"),
        ([1, 2, 37], "mean"),
        ([7, 14, -70], "median"),
        ([-10, 20, 5], 'same'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert mean_vs_median(arg) == expected
