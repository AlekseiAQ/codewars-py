"""No zeros for heros"""

import pytest

from solutions.kyu_8.no_zeros_for_heros import no_boring_zeros

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1450, 145),
        (960000, 96),
        (1050, 105),
        (-1050, -105),
        (0, 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert no_boring_zeros(arg) == expected
