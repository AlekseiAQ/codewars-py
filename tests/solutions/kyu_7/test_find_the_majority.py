"""Find the majority"""

import pytest

from solutions.kyu_7.find_the_majority import majority

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["A", "B", "A"], "A"),
        (["A", "B", "C"], None),
        (["A", "B", "B", "A"], None),
        (['A','A','A','A'], "A"),
        (['A',], "A"),
        (['A','A','A','BBBBBBBB'], "A"),
        (["A", "B", "C", "C"], "C"),
        ([], None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert majority(arg) == expected
