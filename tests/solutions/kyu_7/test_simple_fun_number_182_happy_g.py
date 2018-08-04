"""Simple Fun #182: Happy 'g'"""

import pytest

from solutions.kyu_7.simple_fun_number_182_happy_g import happy_g

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("ogoggo", False),
        ("gg0gg3gg0gg", True),
        ("gog", False),
        ("ggg ggg g ggg", False),
        ("A half of a half is a quarter.", True),
        ("good grief", False),
        ("bigger is ggooder", True),
        ("gggggggggg", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert happy_g(arg) == expected
