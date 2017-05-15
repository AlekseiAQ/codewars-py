"""Help Mr. E"""

import pytest

from solutions.kyu_7.help_mr_e import evenator

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('', ''),
        ('I got a hole in 1!', 'II gott aa hole in 11'),
        ('underscore is not considered a word..in this case,', 
            'underscore is nott considered aa wordin this case'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert evenator(arg) == expected
