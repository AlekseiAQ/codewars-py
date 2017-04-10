"""Format to the 2nd"""

import pytest

from solutions.kyu_7.format_to_the_2nd import print_nums

EXAMPLES = (
    ('args', 'expected'),
    [
        ((), ''),
        ((2,), '2'),
        ((1, 12, 34), '01\n12\n34'),
        ((1009, 2), '1009\n0002'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert print_nums(*args) == expected
