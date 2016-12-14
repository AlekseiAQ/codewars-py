"""Are they the "same"?"""

import pytest

from solutions.kyu_6.are_they_the_same import comp

EXAMPLES = (
    ('array1', 'array2', 'expected'),
    [
        ([121, 144, 19, 161, 19, 144, 19, 11],
        [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19],
        True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array1, array2, expected):
    assert comp(array1, array2) == expected
