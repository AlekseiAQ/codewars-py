"""Double Char"""

import pytest

from solutions.kyu_8.double_char import double_char

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("String", "SSttrriinngg"),
        ("Hello World", "HHeelllloo  WWoorrlldd"),
        ("1234!_ ", "11223344!!__  "),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert double_char(arg) == expected
