"""Find the stray number"""

import pytest

from solutions.kyu_7.find_the_stray_number import stray

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,1,1,1,1,1,2], 2),
        ([2,3,2,2,2], 3),
        ([3,2,2,2,2], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert stray(arg) == expected
