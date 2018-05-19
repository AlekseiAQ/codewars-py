"""Array element parity"""

import pytest

from solutions.kyu_7.array_element_parity import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,-1,2,-2,3],3),
        ([-3,1,2,3,-1,-4,-2],-4),
        ([1,-1,2,-2,3,3],3),
        ([-110,110,-38,-38,-62,62,-38,-38,-38],-38),
        ([ -9,-105,-9,-9,-9,-9,105],-9),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
