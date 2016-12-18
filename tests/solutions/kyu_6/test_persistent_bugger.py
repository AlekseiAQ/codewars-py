"""Persistent Bugger."""

import pytest

from solutions.kyu_6.persistent_bugger import persistence

EXAMPLES = (
    ('arg', 'expected'),
    [
        (39, 3),
        (4, 0),
        (25, 2),
        (999, 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert persistence(arg) == expected
