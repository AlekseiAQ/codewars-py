"""Array comparator"""

import pytest

from solutions.kyu_7.array_comparator import match_arrays

EXAMPLES = (
    ('args', 'expected'),
    [
        ((['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang']), 0),
        ((['Erlang', 'JavaScript'], ['Go', 'C++', 'Python']), 0),
        (([True, 3, 9, 11, 15], [True, 3, 11]), 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert match_arrays(*args) == expected
