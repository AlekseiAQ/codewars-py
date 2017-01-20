"""NBA full 48 minutes average"""

import pytest

from solutions.kyu_8.nba_full_48_minutes_average import nba_extrap

EXAMPLES = (
    ('args', 'expected'),
    [
        ((12, 20), 28.8),
        ((10, 10), 48.0),
        ((5, 17), 14.1),
        ((0, 0), 0),
        ((30.8, 34.7), 42.6),
        ((22.9, 33.8), 32.5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert nba_extrap(*args) == expected
