"""Find the position!"""

import pytest

from solutions.kyu_8.find_the_position import position

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("a", "Position of alphabet: 1"),
        ("z", "Position of alphabet: 26"),
        ("e", "Position of alphabet: 5"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert position(arg) == expected
