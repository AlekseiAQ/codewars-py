"""Distance from the average"""

import pytest

from solutions.kyu_7.distance_from_the_average import distances_from_average

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([55, 95, 62, 36, 48], [4.2, -35.8, -2.8, 23.2, 11.2]),
        ([1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
        ([1, -1, 1, -1, 1, -1], [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]),
        ([1, -1, 1, -1, 1], [-0.8, 1.2, -0.8, 1.2, -0.8]),
        ([2, -2], [-2.0, 2.0]),
        ([1], [0]),
        ([123, -65, 32432, -353, -534], [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert distances_from_average(arg) == expected
