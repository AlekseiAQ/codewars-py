"""Remove exclamation marks"""

import pytest

from solutions.kyu_8.remove_exclamation_marks import remove_exclamation_marks

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hello World!", "Hello World"),
        ("Hello World!!!", "Hello World"),
        ("Hi! Hello!", "Hi Hello"),
        ("", ""),
        ("Oh, no!!!", "Oh, no"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert remove_exclamation_marks(arg) == expected
