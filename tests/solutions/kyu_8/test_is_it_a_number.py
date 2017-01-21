"""Is it a number?"""

import pytest

from solutions.kyu_8.is_it_a_number import isDigit

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("s2324", False),
        ("-234.4", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert isDigit(arg) == expected
