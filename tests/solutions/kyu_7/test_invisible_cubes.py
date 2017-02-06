"""Invisible cubes"""

import pytest

from solutions.kyu_7.invisible_cubes import not_visible_cubes

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 8),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert not_visible_cubes(arg) == expected
