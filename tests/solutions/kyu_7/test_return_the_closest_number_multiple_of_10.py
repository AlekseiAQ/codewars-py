"""Return the closest number multiple of 10"""

import pytest

from solutions.kyu_7.return_the_closest_number_multiple_of_10 import closest_multiple_10

EXAMPLES = (
    ('arg', 'expected'),
    [
        (54, 50),
        (55, 60),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert closest_multiple_10(arg) == expected
