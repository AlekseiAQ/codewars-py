"""Digital cypher"""

import pytest

from solutions.kyu_7.digital_cypher import encode

EXAMPLES = (
    ('args', 'expected'),
    [
        (("scout", 1939), [20, 12, 18, 30, 21]),
        (("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert encode(*args) == expected
