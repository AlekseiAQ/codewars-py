"""Get Planet Name By ID"""

import pytest

from solutions.kyu_8.get_planet_name_by_id import get_planet_name

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2, 'Venus'),
        (5, 'Jupiter'),
        (3, 'Earth'),
        (4, 'Mars'),
        (8, 'Neptune'),
        (1, 'Mercury'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_planet_name(arg) == expected
