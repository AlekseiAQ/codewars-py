"""Power of 4"""

import pytest

from solutions.kyu_7.power_of_4 import powerof4

EXAMPLES = (
    ('arg', 'expected'),
    [
        (4, True),
        (40, False),
        (1, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert powerof4(arg) == expected
