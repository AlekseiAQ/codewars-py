"""Complete The Pattern #2"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_2 import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (2,"21\n2"),
        (5,"54321\n5432\n543\n54\n5"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
