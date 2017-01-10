"""Name Shuffler"""

import pytest

from solutions.kyu_8.name_shuffler import name_shuffler

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('john McClane','McClane john'),
        ('Mary jeggins','jeggins Mary'),
        ('tom jerry','jerry tom'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert name_shuffler(arg) == expected
