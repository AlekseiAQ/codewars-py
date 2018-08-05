"""sum2total"""

import pytest

from solutions.kyu_7.sum2total import total

EXAMPLES = (
    ("arg", "expected"),
    [
        ([1, 2, 3, 4, 5], 48),
        ([5, 4, 3, 2, 1], 48),
        ([1, 2, 3, 4], 20),
        ([1, 2, 3], 8)
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert total(arg) == expected
