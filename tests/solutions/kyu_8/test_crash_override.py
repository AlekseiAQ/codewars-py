"""Crash Override"""

import pytest

from solutions.kyu_8.crash_override import alias_gen

EXAMPLES = (
    ('args', 'expected'),
    [
        (('Mike', 'Millington'), 'Malware Mike'),
        (('Fahima', 'Tash'), 'Function T-Rex'),
        (('Daisy', 'Petrovic'), 'Data Payload'),
        (('Barny', 'White'), 'Beta Worm'),
        (('Hank', 'Kutz'), 'Half-life Killer'),
        (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
        (('walter', 'white'), 'WiFi Worm'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert alias_gen(*args) == expected
