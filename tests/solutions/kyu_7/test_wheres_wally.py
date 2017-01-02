"""Where's Wally"""

import pytest

from solutions.kyu_7.wheres_wally import wheres_wally

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("",-1),
        ("WAlly",-1),
        ("wAlly",-1),
        ("Wally",0),
        ("Where's Wally",8),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert wheres_wally(arg) == expected
