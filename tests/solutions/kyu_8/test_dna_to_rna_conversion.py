"""DNA to RNA Conversion"""

import pytest

from solutions.kyu_8.dna_to_rna_conversion import DNAtoRNA

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("TTTT", "UUUU"),
        ("GCAT", "GCAU"),
        ("GACCGCCGCC", "GACCGCCGCC"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert DNAtoRNA(arg) == expected
