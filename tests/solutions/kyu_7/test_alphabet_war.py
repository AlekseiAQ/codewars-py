"""Alphabet war"""

import pytest

from solutions.kyu_7.alphabet_war import alphabet_war


EXAMPLES = (
    ('arg', 'expected'),
    [
        ("z", "Right side wins!"),
        ("zdqmwpbs", "Let's fight again!"),
        ("wq", "Left side wins!"),
        ("zzzzs", "Right side wins!"),
        ("wwwwww", "Left side wins!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert alphabet_war(arg) == expected
