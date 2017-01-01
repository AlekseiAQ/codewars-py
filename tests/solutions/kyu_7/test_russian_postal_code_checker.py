"""Russian postal code checker"""

import pytest

from solutions.kyu_7.russian_postal_code_checker import zipvalidate

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('198328', True),
        ('310003', True),
        ('424000', True),
        ('12A483', False),
        ('1@63', False),
        ('111', False),
        ('056879', False),
        ('1111111', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert zipvalidate(arg) == expected
