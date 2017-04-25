"""Centroid I"""

import pytest

from solutions.kyu_7.centroid_i import centroid

EXAMPLES = (
    ('arg', 'expected'),
    [
        (([[1,0,5], [0,1,5], [2,2,5]]), [1.0, 1.0, 5.0]),
        (([[7,0,5], [3,1,5], [2,1,5]]), [4.0, 0.67, 5.0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert centroid(arg) == expected
