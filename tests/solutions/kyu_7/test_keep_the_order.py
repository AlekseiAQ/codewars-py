"""Keep the Order"""

import pytest

from solutions.kyu_7.keep_the_order import keep_order

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 2, 3, 4, 7], 5), 4),
        (([1, 2, 3, 4, 7], 0), 0),
        (([1, 1, 2, 2, 2], 2), 2),
        (([1, 2, 3, 4], 5), 4),
        (([1, 2, 3, 4], -1), 0),
        (([1, 2, 3, 4], 2), 1),
        (([1, 2, 3, 4], 0), 0),
        (([1, 2, 3, 4], 1), 0),
        (([1, 2, 3, 4], 2), 1),
        (([1, 2, 3, 4], 3), 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert keep_order(*args) == expected
