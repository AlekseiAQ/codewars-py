"""Mobile operator detector"""

import pytest

from solutions.kyu_7.mobile_operator_detector import detect_operator

EXAMPLES = (
    ('arg', 'expected'),
    [
        (80661111841,"MTS"),
        (80671991111,"Kyivstar"),
        (80631551111,"Life:)"),
        (80931551111,"Life:)"),
        (80111551111,"no info"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert detect_operator(arg) == expected
