"""Convert Improper Fraction to Mixed Number"""

import pytest

from solutions.kyu_7.convert_improper_fraction_to_mixed_number import get_mixed_num

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('18/11', '1 7/11'),
        ('13/5', '2 3/5'),
        ('75/10', '7 5/10'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_mixed_num(arg) == expected
