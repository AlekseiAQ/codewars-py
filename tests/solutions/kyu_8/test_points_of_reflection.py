"""Points of Reflection"""

import pytest

from solutions.kyu_8.points_of_reflection import symmetric_point

EXAMPLES = (
    ('args', 'expected'),
    [
        (([0,0], [1,1]), [2, 2]),
        (([2, 6], [-2, -6]), [-6, -18]),
        (([10, -10], [-10, 10]), [-30, 30]),
        (([1, -35], [-12, 1]), [-25, 37]),
        (([1000, 15], [-7, -214]), [-1014, -443]),
        (([0, 0], [0, 0]), [0, 0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert symmetric_point(*args) == expected
