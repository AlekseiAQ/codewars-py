"""Frequency sequence"""

import pytest

from solutions.kyu_7.frequency_sequence import freq_seq

EXAMPLES = (
    ('s', 'sep', 'expected'),
    [
        ('hello world', '-', '1-1-3-3-2-1-1-2-1-3-1'),
        ('19999999',    ':', '1:7:7:7:7:7:7:7'),
        ('^^^**$',      'x', '3x3x3x2x2x1'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(s, sep, expected):
    assert freq_seq(s, sep) == expected
