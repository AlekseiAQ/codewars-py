"""char_to_ascii"""

import pytest

from solutions.kyu_7.char_to_ascii import char_to_ascii

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", None),
        ("a", {"a":97}),
        ("aaa", {"a":97}),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert char_to_ascii(arg) == expected
