"""Switch/Case - Bug Fixing #6"""

import pytest

from solutions.kyu_8.switch_slash_case_bug_fixing_number_6 import eval_object

EXAMPLES = (
    ('arg', 'expected'),
    [
        ({'a':1,'b':1,'operation':'+'}, 2),
        ({'a':1,'b':1,'operation':'-'}, 0),
        ({'a':1,'b':1,'operation':'/'}, 1),
        ({'a':1,'b':1,'operation':'*'}, 1),
        ({'a':1,'b':1,'operation':'%'}, 0),
        ({'a':1,'b':1,'operation':'**'}, 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert eval_object(arg) == expected
