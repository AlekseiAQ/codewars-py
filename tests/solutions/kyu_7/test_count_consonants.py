"""Count consonants"""

import pytest

from solutions.kyu_7.count_consonants import consonant_count

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('', 0),
        ('aaaaa', 0),
        ('XaeiouX', 2),
        ('Bbbbb', 5),
        ('helLo world', 7),
        ('h^$&^#$&^elLo world', 7),
        ('0123456789', 0),
        ('012345_Cb', 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert consonant_count(arg) == expected
