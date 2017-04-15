"""Count characters in your string"""

import pytest

from solutions.kyu_6.count_characters_in_your_string import count

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('aba', {'a': 2, 'b': 1}),
        ('', {}),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert count(arg) == expected
