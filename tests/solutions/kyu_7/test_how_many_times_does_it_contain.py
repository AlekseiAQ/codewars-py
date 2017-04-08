"""How many times does it contain?"""

import pytest

from solutions.kyu_7.how_many_times_does_it_contain import string_counter

EXAMPLES = (
    ('strng', 'char', 'expected'),
    [
        ("Hello world","o", 2),
        ("Wait isn't it supposed to be cynical?","i", 4),
        ("I'm gona be the best code warrior ever dad","r", 4),
        ("Do you like Harry Potter?","?", 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(strng, char, expected):
    assert string_counter(strng, char) == expected
