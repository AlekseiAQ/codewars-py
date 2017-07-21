"""Multi-tap Keypad Text Entry on an Old Mobile Phone"""

import pytest

from solutions.kyu_6.multi_tap_keypad_text_entry_on_an_old_mobile_phone import \
    presses

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("LOL", 9),
        ("HOW R U", 13),
        ("lol", 9),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert presses(arg) == expected
