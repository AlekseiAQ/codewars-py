"""Chinese Zodiac"""

import pytest

from solutions.kyu_7.chinese_zodiac import chinese_zodiac

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1965, "Wood Snake"),
        (1938, "Earth Tiger"),
        (1998, "Earth Tiger"),
        (2016, "Fire Monkey"),
        (1924, "Wood Rat"),
        (1968, "Earth Monkey"),
        (2162, "Water Dog"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert chinese_zodiac(arg) == expected
