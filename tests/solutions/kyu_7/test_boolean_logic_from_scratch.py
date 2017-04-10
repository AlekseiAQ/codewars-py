"""Boolean logic from scratch"""

import pytest

from solutions.kyu_7.boolean_logic_from_scratch import func_or, func_xor

EXAMPLES = (
    ('arg', 'expected'),
    [
        (func_or(True, True), True),
        (func_or(True, False), True),
        (func_or(False, False), False),
        (func_or(0, 11), True),
        (func_or(None, []), False),
        (func_xor(True, True), False),
        (func_xor(True, False), True),
        (func_xor(False, False), False),
        (func_xor(0, 11), True),
        (func_xor(None, []), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
