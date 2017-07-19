"""Find the motif in DNA sequence."""

import pytest

from solutions.kyu_7.find_the_motif_in_dna_sequence import motif_locator

EXAMPLES = (
    ('args', 'expected'),
    [
        (("TTCCGGAACC", "CC"), [3, 9]),
        (("ACGTTACAACGTTAG", "ACGT"),  [1, 9]),
        (("ACGTACGTACGT", "AAA"), []),
        (("ACGT", "ACGTGAC"), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert motif_locator(*args) == expected
