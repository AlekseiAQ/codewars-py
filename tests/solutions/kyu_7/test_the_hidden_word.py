"""The Hidden Word"""

import pytest

from solutions.kyu_7.the_hidden_word import hidden

EXAMPLES = (
    ('arg', 'expected'),
    [
        (637, "aid"),
        (7415, "debt"),
        (49632, "email"),
        (942547, "melted"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert hidden(arg) == expected
