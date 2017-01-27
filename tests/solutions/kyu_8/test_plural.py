"""Plural"""

import pytest

from solutions.kyu_8.plural import plural

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, True),
        (1, False),
        (100, True),
        (0.5, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert plural(arg) == expected
