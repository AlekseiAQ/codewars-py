"""Greatest Difference"""

import pytest

from solutions.kyu_7.greatest_difference import diff

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['43-45', '1021-55', '000-18888', '92-34', '76-32', '99-1', '1020-54'], '000-18888'),
        (['1-2', '2-4', '5-7', '8-9', '44-45'], '2-4'),
        (['5-37', '5-5', '7-24', '12-21', '12-12', '1-1', '69-69', '11-35'], '5-37'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert diff(arg) == expected
