"""Simple Fun #40:  Timed Reading"""

import pytest

from solutions.kyu_7.simple_fun_number_40_timed_reading import timed_reading

EXAMPLES = (
    ('args', 'expected'),
    [
        ((4, "The Fox asked the stork, 'How is the soup?'"), 7),
        ((1, "..."), 0),
        ((3, "This play was good for us."), 3),
        ((3, "Suddenly he stopped, and glanced up at the houses"), 5),
        ((6, "Zebras evolved among the Old World horses within the last four million years."), 11),
        ((5, "Although zebra species may have overlapping ranges, they do not interbreed."), 6),
        ((1, "Oh!"), 0),
        ((5, "Now and then, however, he is horribly thoughtless, and seems to take a real delight in giving me pain."), 14),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert timed_reading(*args) == expected
