"""Refactored Greeting"""

import pytest

from solutions.kyu_7.refactored_greeting import Person

jack = Person("Jack")
jill = Person("Jill")

EXAMPLES = (
    ("arg", "expected"),
    [
        (jack.greet("Jill"), "Hello Jill, my name is Jack"),
        (jack.greet("Mary"), "Hello Mary, my name is Jack"),
        (jill.greet("Jack"), "Hello Jack, my name is Jill"),
        (jill.name, "Jill"),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
