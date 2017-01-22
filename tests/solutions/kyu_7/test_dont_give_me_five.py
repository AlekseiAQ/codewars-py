"""Don't give me five!"""

import pytest

from solutions.kyu_7.dont_give_me_five import dont_give_me_five

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1,9), 8),
        ((4,17), 12),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert dont_give_me_five(*args) == expected
