"""Letterbox Paint-Squad"""

import pytest

from solutions.kyu_7.letterbox_paint_squad import paint_letterboxes

EXAMPLES = (
    ('args', 'expected'),
    [
        ((125, 132), [1,9,6,3,0,1,1,1,1,1])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert paint_letterboxes(*args) == expected
