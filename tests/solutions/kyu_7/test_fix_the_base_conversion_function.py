"""Fix the base conversion function!"""

import pytest

from solutions.kyu_7.fix_the_base_conversion_function import convert_num

EXAMPLES = (
    ('args', 'expected'),
    [
        ((122, 'bin'), '0b1111010'),
        (('dog', 'bin'), 'Invalid number input'),
        ((0, 'hex'), '0x0'),
        ((123, 'lol'), 'Invalid base input'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert convert_num(*args) == expected
