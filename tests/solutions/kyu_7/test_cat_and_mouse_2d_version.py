"""Cat and Mouse - 2D Version"""

import pytest

from solutions.kyu_7.cat_and_mouse_2d_version import cat_mouse

map_ = '''\
..C......
.........
....m....'''

EXAMPLES = (
    ('args', 'expected'),
    [
        ((map_, 5), 'Caught!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert cat_mouse(*args) == expected
