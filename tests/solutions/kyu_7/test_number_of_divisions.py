"""Number of Divisions"""

import pytest

from solutions.kyu_7.number_of_divisions import divisions

EXAMPLES = (
    ('args', 'expected'),
    [
        ((6, 2), 2),
        ((100, 2), 6),
        ((2450, 5), 4),
        ((9999, 3), 8),
        ((2, 3), 0),
        ((5, 5), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert divisions(*args) == expected
