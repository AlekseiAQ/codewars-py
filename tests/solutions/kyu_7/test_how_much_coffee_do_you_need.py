"""How much coffee do you need?"""

import pytest

from solutions.kyu_7.how_much_coffee_do_you_need import how_much_coffee

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], 0),
        (['cw'], 1),
        (['CW'], 2),
        (['cw','CAT'], 3),
        (['cw','CAT','DOG'], 'You need extra sleep'),
        (['cw','CAT', 'cw=others'], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert how_much_coffee(arg) == expected
