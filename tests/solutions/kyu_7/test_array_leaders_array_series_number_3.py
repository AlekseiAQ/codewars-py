"""Array Leaders (Array Series #3)"""

import pytest

from solutions.kyu_7.array_leaders_array_series_number_3 import array_leaders

EXAMPLES = (
    ("arg", "expected"),
    [
        ([1, 2, 3, 4, 0], [4]),
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([-1, -29, -26, -2], [-1]),
        ([-36, -12, -27], [-36, -12]),
        ([5, 2], [5, 2]),
        ([0, -1, -29, 3, 2], [0, -1, 3, 2]),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert array_leaders(arg) == expected
