"""Green Glass Door"""

import pytest

from solutions.kyu_7.green_glass_door import step_through_with

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("moon", True),
        ("test", False),
        ("glasses", True),
        ("airplane", False),
        ("free", True),
        ("branch", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert step_through_with(arg) == expected
