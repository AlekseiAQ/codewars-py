"""Hit Count"""

import pytest

from solutions.kyu_7.hit_count import counter_effect

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1250", [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]]),
        ("0050", [[0], [0], [0, 1, 2, 3, 4, 5], [0]]),
        ('0000', [[0], [0], [0], [0]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert counter_effect(arg) == expected
