"""Form The Minimum"""

import pytest

from solutions.kyu_7.form_the_minimum import min_value

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 3, 1], 13),
        ([4, 7, 5, 7], 457),
        ([4, 8, 1, 4], 148),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert min_value(arg) == expected
