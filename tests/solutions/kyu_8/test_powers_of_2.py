"""Powers of 2"""

import pytest

from solutions.kyu_8.powers_of_2 import powers_of_two

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, [1]),
        (1, [1, 2]),
        (4, [1, 2, 4, 8, 16]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert powers_of_two(arg) == expected
