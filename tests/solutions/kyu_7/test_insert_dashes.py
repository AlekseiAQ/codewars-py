"""Insert dashes"""

import pytest

from solutions.kyu_7.insert_dashes import insert_dash

EXAMPLES = (
    ('arg', 'expected'),
    [
        (454793, '4547-9-3'),
        (123456, '123456'),
        (1003567, '1003-567'),
        (24680, '24680'),
        (13579, '1-3-5-7-9'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert insert_dash(arg) == expected
