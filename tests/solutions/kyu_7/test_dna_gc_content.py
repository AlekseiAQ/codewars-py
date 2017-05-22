"""DNA GC-content"""

import pytest

from solutions.kyu_7.dna_gc_content import gc_content

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('', 0.0),
        ('A', 0.0),
        ('C', 100.0),
        ('CA', 50.0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert gc_content(arg) == expected
