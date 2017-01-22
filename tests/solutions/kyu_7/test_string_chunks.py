"""String chunks"""

import pytest

from solutions.kyu_7.string_chunks import string_chunk

EXAMPLES = (
    ('args', 'expected'),
    [
        (('codewars', 2), ['co', 'de', 'wa', 'rs']),
        (('thiskataeasy', 4), ['this', 'kata', 'easy']),
        (('hello world', 3), ['hel', 'lo ', 'wor', 'ld']),
        (('everlong', 100), ['everlong']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert string_chunk(*args) == expected
