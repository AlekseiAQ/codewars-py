"""Well of Ideas - Easy Version"""

import pytest

from solutions.kyu_8.well_of_ideas_easy_version import well

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['bad', 'bad', 'bad'], 'Fail!'),
        (['good', 'bad', 'bad', 'bad', 'bad'], 'Publish!'),
        (['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'], 'I smell a series!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert well(arg) == expected
