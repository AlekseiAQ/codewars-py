"""Insert Dashes 2"""

import pytest

from solutions.kyu_7.insert_dashes_2 import insert_dash2

EXAMPLES = (
    ('arg', 'expected'),
    [
        (454793, '4547-9-3'),
        (123456, '123456'),
        (40546793, '4054*67-9-3'),
        (1012356895, '10123-56*89-5'),
        (0, '0'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert insert_dash2(arg) == expected
