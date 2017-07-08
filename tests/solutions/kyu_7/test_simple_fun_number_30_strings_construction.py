"""Simple Fun #30:  Strings  Construction"""

import pytest

from solutions.kyu_7.simple_fun_number_30_strings_construction import strings_construction

EXAMPLES = (
    ('args', 'expected'),
    [
        (("abc", "abccba"), 2),
        (("hnccv", "hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"), 3),
        (("abc", "def"), 0),
        (("zzz", "zzzzzzzzzzz"), 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert strings_construction(*args) == expected
