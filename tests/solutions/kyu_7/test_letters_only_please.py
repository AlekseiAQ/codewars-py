"""letters only, please!"""

import pytest

from solutions.kyu_7.letters_only_please import remove_chars

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("test for error!", "test for error"),
        (".tree1", "tree"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert remove_chars(arg) == expected
