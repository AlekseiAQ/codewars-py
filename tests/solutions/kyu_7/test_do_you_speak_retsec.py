"""Do you speak retsec?"""

import pytest

from solutions.kyu_7.do_you_speak_retsec import reverse_by_center

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("secret", "retsec"),
        ("agent", "nteag"),
        ("raw", "war"),
        ("onion", "onion"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_by_center(arg) == expected
