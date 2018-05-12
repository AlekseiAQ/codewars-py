"""Radio DJ helper function"""

import pytest

from solutions.kyu_7.radio_dj_helper_function import longest_possible


EXAMPLES = (
    ('arg', 'expected'),
    [
        (215, "For Reasons Unknown"),
        (270, "YYZ"),
        (13, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert longest_possible(arg) == expected
