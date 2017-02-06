"""Some Circles"""

import pytest

from solutions.kyu_7.some_circles import sum_circles

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, ), 'We have this much circle: 3'),
        ((2, 3, 4), 'We have this much circle: 23'),
        ((48, 7, 8, 9, 10), 'We have this much circle: 2040'),
        ((1, ), 'We have this much circle: 1'),
        ((1, 1, 1, 2, 3, 4, 5), 'We have this much circle: 45'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sum_circles(*args) == expected
