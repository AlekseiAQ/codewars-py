"""Count the Characters"""

import pytest

from solutions.kyu_7.count_the_characters import count_char

EXAMPLES = (
    ('args', 'expected'),
    [
        (("Hello there", "e"), 3),
        (("Hello there", "t"), 1),
        (("Hello there", "h"), 2),
        (("Hello there", "L"), 2),
        (("Hello there", " "), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert count_char(*args) == expected
