"""8 towers"""

import pytest

from solutions.kyu_7.eight_towers import tower_combination

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2, 2),
        (3, 6),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert tower_combination(arg) == expected
