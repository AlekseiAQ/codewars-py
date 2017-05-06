"""Self-Descriptive Numbers"""

import pytest

from solutions.kyu_7.self_descriptive_numbers import self_descriptive

EXAMPLES = (
    ('arg', 'expected'),
    [
        (21200, True),
        (3211000, True),
        (42101000, True),
        (21230, False),
        (11200, False),
        (1210, True),
        (51120111, False),
        (2020, True),
        (11201, False),
        (6210001000, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert self_descriptive(arg) == expected
