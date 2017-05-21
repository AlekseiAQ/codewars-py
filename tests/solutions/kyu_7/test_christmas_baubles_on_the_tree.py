"""Christmas baubles on the tree"""

import pytest

from solutions.kyu_7.christmas_baubles_on_the_tree import baubles_on_tree

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5,5), [1,1,1,1,1]),
        ((5,0), "Grandma, we will have to buy a Christmas tree first!"),
        ((6,5), [2,1,1,1,1]),
        ((50,9), [6,6,6,6,6,5,5,5,5]),
        ((0,10), [0,0,0,0,0,0,0,0,0,0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert baubles_on_tree(*args) == expected
