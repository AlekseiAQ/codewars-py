"""Find the nth occurrence of a word in a string!"""

import pytest

from solutions.kyu_7.find_the_nth_occurrence_of_a_word_in_a_string import (
    find_nth_occurrence,
)

STRING = (
    "This is an example. Return the nth occurrence of example in this example string."
)

EXAMPLES = (
    ("args", "expected"),
    [
        (("example", STRING, 1), 11),
        (("example", STRING, 2), 49),
        (("example", STRING, 3), 65),
        (("example", STRING, 4), -1),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert find_nth_occurrence(*args) == expected
