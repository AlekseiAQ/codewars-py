"""repeatIt"""

import pytest

from solutions.kyu_8.repeatit import repeat_it

EXAMPLES = (
    ('args', 'expected'),
    [
        (("*",3), "***"),
        (("Hello",11), "HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert repeat_it(*args) == expected
