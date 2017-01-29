"""Help Suzuki rake his garden!"""

import pytest

from solutions.kyu_7.help_suzuki_rake_his_garden import rake_garden

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('slug spider rock gravel gravel gravel gravel gravel gravel gravel',
        'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert rake_garden(arg) == expected
