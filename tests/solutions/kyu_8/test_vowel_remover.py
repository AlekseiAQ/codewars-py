"""Vowel remover"""

import pytest

from solutions.kyu_8.vowel_remover import shortcut

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('hello', 'hll'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert shortcut(arg) == expected
