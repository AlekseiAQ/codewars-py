"""Age Range Compatibility Equation"""

import pytest

from solutions.kyu_8.age_range_compatibility_equation import dating_range

EXAMPLES = (
    ('arg', 'expected'),
    [
        (17, "15-20"),
        (40, "27-66"),
        (15, "14-16"),
        (35, "24-56"),
        (10, "9-11"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert dating_range(arg) == expected
