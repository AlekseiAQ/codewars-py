"""Compare within margin"""

import pytest

from solutions.kyu_8.compare_within_margin import close_compare

EXAMPLES = (
    ('args', 'expected'),
    [
        ((4, 5, 0), -1),
        ((5, 5, 0), 0),
        ((6, 5, 0), 1),
        ((2, 5, 3), 0),
        ((5, 5, 3), 0),
        ((8, 5, 3), 0),
        ((8.1, 5, 3), 1),
        ((1.99, 5, 3), -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert close_compare(*args) == expected
