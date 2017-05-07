"""Clean up after your dog"""

import pytest

from solutions.kyu_7.clean_up_after_your_dog import crap

EXAMPLES = (
    ('args', 'expected'),
    [
        (([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2), "Clean"),
        (([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1), "Cr@p"),
        (([['_','_'], ['_','@'], ['D','_']], 2, 2), "Dog!!"),
        (([['_','_','_','_'], ['_','_','_','_'], ['_','_','_', '_']], 2, 2), "Clean"),
        (([['@','@'], ['@','@'], ['@','@']], 3, 2), "Clean"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert crap(*args) == expected
