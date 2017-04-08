"""Which string is worth more?"""

import pytest

from solutions.kyu_7.which_string_is_worth_more import highest_value

EXAMPLES = (
    ('a', 'b', 'expected'),
    [
        ("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567", "KkLlMmNnOoPp4567"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, expected):
    assert highest_value(a, b) == expected
