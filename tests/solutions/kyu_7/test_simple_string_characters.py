"""Simple string characters"""

import pytest

from solutions.kyu_7.simple_string_characters import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Codewars@codewars123.com", [1, 18, 3, 2]),
        ("bgA5<1d-tOwUZTS8yQ", [7, 6, 3, 2]),
        ("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H", [9, 9, 6, 9]),
        ("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD", [15, 8, 6, 9]),
        ("$Cnl)Sr<7bBW-&qLHI!mY41ODe", [10, 7, 3, 6]),
        ("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft", [7, 13, 4, 10]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
