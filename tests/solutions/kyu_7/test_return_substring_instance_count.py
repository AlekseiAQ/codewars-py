"""Return substring instance count"""

import pytest

from solutions.kyu_7.return_substring_instance_count import solution

EXAMPLES = (
    ('args', 'expected'),
    [
        (('abcdeb','b'), 2),
        (('abc','b'), 1),
        (('abbc','bb'), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solution(*args) == expected
