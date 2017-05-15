"""Bumps in the Road"""

import pytest

from solutions.kyu_7.bumps_in_the_road import bumps

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("n", "Woohoo!"),
        ("_nnnnnnn_n__n______nn__nn_nnn", "Car Dead"),
        ("______n___n_", "Woohoo!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert bumps(arg) == expected
