"""Correct the mistakes of the character recognition software"""

import pytest

from solutions.kyu_8.correct_the_mistakes_of_the_character_recognition_software import correct

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("L0ND0N","LONDON"),
        ("DUBL1N","DUBLIN"),
        ("51NGAP0RE","SINGAPORE"),
        ("BUDAPE5T","BUDAPEST"),
        ("PAR15","PARIS"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert correct(arg) == expected
