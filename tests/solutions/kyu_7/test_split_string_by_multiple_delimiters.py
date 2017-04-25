"""Split string by multiple delimiters"""

import pytest

from solutions.kyu_7.split_string_by_multiple_delimiters import multiple_split

EXAMPLES = (
    ('args', 'expected'),
    [
        (('Hi everybody!', [' ', '!']), ['Hi', 'everybody']),
        (('(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*']), ['1', '2', '6', '3', '9']),
        (('Solve_this|kata-very\quickly!', ['!', '|', '\\', '_', '-']), ['Solve', 'this', 'kata', 'very', 'quickly']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert multiple_split(*args) == expected
