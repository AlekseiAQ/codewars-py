"""validate code with simple regex"""

import pytest

from solutions.kyu_8.validate_code_with_simple_regex import validate_code

EXAMPLES = (
    ('arg', 'expected'),
    [
        (123, True),
        (248, True),
        (8, False),
        (321, True),
        (9453, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_code(arg) == expected
