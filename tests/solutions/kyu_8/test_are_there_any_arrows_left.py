"""Are there any arrows left?"""

import pytest

from solutions.kyu_8.are_there_any_arrows_left import any_arrows

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], False),
        ([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}], True),
        ([{'range': 10, 'damaged': True}, {'damaged': True}], False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert any_arrows(arg) == expected
