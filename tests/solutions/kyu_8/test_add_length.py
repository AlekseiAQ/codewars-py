"""Add Length"""

import pytest

from solutions.kyu_8.add_length import add_length

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('apple ban',["apple 5", "ban 3"]),
        ('you will win',["you 3", "will 4", "win 3"]),
        ('you',["you 3"]),
        ('y',["y 1"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert add_length(arg) == expected
