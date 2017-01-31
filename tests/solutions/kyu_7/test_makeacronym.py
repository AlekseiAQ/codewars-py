"""makeAcronym"""

import pytest

from solutions.kyu_7.makeacronym import make_acronym

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('My aunt sally','MAS'),
        ('Please excuse my dear aunt Sally','PEMDAS'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert make_acronym(arg) == expected
