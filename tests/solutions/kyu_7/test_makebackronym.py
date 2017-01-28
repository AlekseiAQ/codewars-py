"""makeBackronym"""

import pytest

from solutions.kyu_7.makebackronym import make_backronym

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('interesting','ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious'),
        ('codewars','confident oscillating disturbing eager weird awesome rant stylish'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert make_backronym(arg) == expected
