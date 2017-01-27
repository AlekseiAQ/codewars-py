"""Find the Slope"""

import pytest

from solutions.kyu_8.find_the_slope import find_slope

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([19,3,20,3],"0"),
        ([-7,2,-7,4],"undefined"),
        ([10,50,30,150],"5"),
        ([10,20,20,80],"6"),
        ([-10,6,-10,3],"undefined"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_slope(arg) == expected
