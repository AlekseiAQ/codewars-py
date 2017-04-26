"""A function within a function"""

import pytest

from solutions.kyu_8.a_function_within_a_function import always

EXAMPLES = (
    ('arg', 'expected'),
    [
        (3, 3),
        (5, 5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert always(arg)() == expected
