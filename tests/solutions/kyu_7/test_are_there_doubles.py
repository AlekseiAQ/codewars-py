"""Are there doubles?"""

import pytest

from solutions.kyu_7.are_there_doubles import double_check

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("abca", False),
        ("aabc", True),
        ("a 11 c d", True),
        ("AabBcC", True),
        ("a b  c", True),
        ("a b c d e f g h i h k", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert double_check(arg) == expected
