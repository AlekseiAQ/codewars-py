"""From-To-Step Sequence Generator"""

import pytest

from solutions.kyu_7.from_to_step_sequence_generator import generator

EXAMPLES = (
    ('from_', 'to', 'step', 'expected'),
    [
        (10, 20, 1, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        (20, 10, 1, [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]),
        (10, 20, 0, []),
        (10, 20, 5, [10, 15, 20]),
        (0, 1, 1, [0, 1]),
        (10, 20, 7, [10, 17]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(from_, to, step, expected):
    assert generator(from_, to, step) == expected
