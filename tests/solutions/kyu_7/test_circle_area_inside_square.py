"""Circle area inside square"""

import pytest

from solutions.kyu_7.circle_area_inside_square import square_area_to_circle

EXAMPLES = (
    ('arg', 'expected'),
    [
        (9, 7.0685834705770345),
        (20, 15.70796326794897),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert round(square_area_to_circle(arg), 8) == round(expected, 8)
