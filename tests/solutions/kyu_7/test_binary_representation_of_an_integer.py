"""Binary Representation of an Integer"""

import pytest

from solutions.kyu_7.binary_representation_of_an_integer import showBits

EXAMPLES = (
    ('arg', 'expected'),
    [
        (701,
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
          0, 1, 0, 1, 1, 1, 1, 0, 1]),
        (-245,
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 0, 0, 0, 0, 1, 0, 1, 1]),
        (12336,
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
         0, 0, 0, 1, 1, 0, 0, 0, 0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert showBits(arg) == expected
