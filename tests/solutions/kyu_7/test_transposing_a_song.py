"""Transposing a song"""

import pytest

from solutions.kyu_7.transposing_a_song import transpose

EXAMPLES = (
    ('args', 'expected'),
    [
        ((['A'], 1), ['A#']),
        ((['Bb', 'C#', 'E'], -4), ['F#', 'A', 'C']),
        ((['C', 'C', 'C#', 'D', 'F', 'D', 'F', 'D', 'D', 'C#', 'C', 'G', 'C', 'C'], 4), ['E', 'E', 'F', 'F#', 'A', 'F#', 'A', 'F#', 'F#', 'F', 'E', 'B', 'E', 'E']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert transpose(*args) == expected
