"""Convert number to reversed array of digits"""

import pytest

from solutions.kyu_8.convert_number_to_reversed_array_of_digits import digitize

EXAMPLES = (
    ('arg', 'expected'),
    [
        (35231,[1,3,2,5,3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert digitize(arg) == expected
