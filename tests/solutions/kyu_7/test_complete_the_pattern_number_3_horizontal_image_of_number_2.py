"""Complete The Pattern #3 (Horizontal Image of #2)"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_3_horizontal_image_of_number_2 import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (2,"2\n21"),
        (5,"5\n54\n543\n5432\n54321"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
