"""Printing Array elements with Comma delimiters"""

import pytest

from solutions.kyu_8.printing_array_elements_with_comma_delimiters import print_array

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([2,4,5,2],"2,4,5,2"),
        ([2,4,5,2],"2,4,5,2"),
        ([2.0,4.2,5.1,2.2],"2.0,4.2,5.1,2.2"),
        (["2","4","5","2"],"2,4,5,2"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert print_array(arg) == expected
