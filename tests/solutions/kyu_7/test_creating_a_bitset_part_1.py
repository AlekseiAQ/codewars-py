"""Creating a Bitset, Part 1"""

import pytest

from solutions.kyu_7.creating_a_bitset_part_1 import byte_to_set

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, set()),
        (3, {6, 7}),
        (255, {0, 1, 2, 3, 4, 5,6 ,7}),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert byte_to_set(arg) == expected
