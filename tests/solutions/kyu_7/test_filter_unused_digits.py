"""Filter unused digits"""

import pytest

from solutions.kyu_7.filter_unused_digits import unused_digits

EXAMPLES = (
    ('args', 'expected'),
    [
        ((12, 34, 56, 78), "09"),
        ((2015, 8, 26), "3479"),
        ((276, 575), "013489"),
        # ((643), "0125789"),
        ((864, 896, 744), "01235"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert unused_digits(*args) == expected
