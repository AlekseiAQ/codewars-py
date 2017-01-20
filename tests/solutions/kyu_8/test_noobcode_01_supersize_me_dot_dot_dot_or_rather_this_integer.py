"""noobCode 01: SUPERSIZE ME.... or rather, this integer! """

import pytest

from solutions.kyu_8.noobcode_01_supersize_me_dot_dot_dot_or_rather_this_integer import super_size

EXAMPLES = (
    ('arg', 'expected'),
    [
        (69,96),
        (513,531),
        (2017,7210),
        (414,441),
        (608719,987610),
        (123456789,987654321),
        (700000000001,710000000000),
        (666666,666666),
        (2,2),
        (0,0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert super_size(arg) == expected
