"""Reverse complement (DNA )"""

import pytest

from solutions.kyu_7.reverse_complement_dna import reverse_complement

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("TTCCGGAA", "TTCCGGAA"),
        ("GACTGACTGTA","TACAGTCAGTC"),
        ("", ""),
        ("XYZ", "Invalid sequence"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_complement(arg) == expected
