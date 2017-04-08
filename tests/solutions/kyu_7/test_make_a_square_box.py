"""Make a square box!"""

import pytest

from solutions.kyu_7.make_a_square_box import box

EXAMPLES = (
    ('arg', 'expected'),
    [
        (5, ['-----',
            '-   -',
            '-   -',
            '-   -',
            '-----']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert box(arg) == expected
