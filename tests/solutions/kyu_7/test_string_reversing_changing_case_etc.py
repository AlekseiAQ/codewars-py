"""String Reversing, Changing case, etc."""

import pytest

from solutions.kyu_7.string_reversing_changing_case_etc import reverse_and_mirror

EXAMPLES = (
    ('args', 'expected'),
    [
        (("FizZ", "buZZ"), "zzUB@@@zZIffIZz"),
        (("String Reversing", "Changing Case"), "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert reverse_and_mirror(*args) == expected
