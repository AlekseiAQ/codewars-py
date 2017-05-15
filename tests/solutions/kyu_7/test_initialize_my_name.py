"""Initialize my name"""

import pytest

from solutions.kyu_7.initialize_my_name import initializeNames

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Jack Ryan', 'Jack Ryan'),
        ('Lois Mary Lane', 'Lois M. Lane'),
        ('Dimitri', 'Dimitri'),
        ('Alice Betty Catherine Davis', 'Alice B. C. Davis'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert initializeNames(arg) == expected
