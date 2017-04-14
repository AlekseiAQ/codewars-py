"""Find Added """

import pytest

from solutions.kyu_6.find_added import find_added

EXAMPLES = (
    ('args', 'expected'),
    [
        (('44554466', '447554466'), '7'),
        (('9876521', '9876543211'), '134'),
        (('4455446', '447555446666'), '56667'),
        (('678', '876'), ''),
        (('678', '6'), ''),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert find_added(*args) == expected
