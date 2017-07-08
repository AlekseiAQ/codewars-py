"""Simple Fun #4: Phone Call"""

import pytest

from solutions.kyu_7.simple_fun_number_4_phone_call import phone_call

EXAMPLES = (
    ('args', 'expected'),
    [
        ((3, 1, 2, 20), 14),
        ((2, 2, 1, 2), 1),
        ((10, 1, 2, 22), 11),
        ((2, 2, 1, 24), 14),
        ((1, 2, 1, 6), 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert phone_call(*args) == expected
