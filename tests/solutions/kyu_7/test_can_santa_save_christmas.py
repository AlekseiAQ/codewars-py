"""Can Santa save Christmas?"""

import pytest

from solutions.kyu_7.can_santa_save_christmas import determineTime

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["01:00:00", "02:30:00"], True),
        (["01:00:00", "02:30:00", "22:00:00"], False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert determineTime(arg) == expected
