"""Number of People in the Bus"""

import pytest

from solutions.kyu_8.number_of_people_in_the_bus import number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([[10,0],[3,5],[5,8]], 5),
        ([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]], 17),
        ([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]], 21),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert number(arg) == expected
