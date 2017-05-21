"""Alan Partridge I - Partridge Watch"""

import pytest

from solutions.kyu_7.alan_partridge_i_partridge_watch import part

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["Grouse", "Partridge", "Pheasant"], "Mine's a Pint!"),
        (["Pheasant", "Goose", "Starling", "Robin"], "Lynn, I've pierced my foot on a spike!!"),
        (["Grouse", "Partridge", "Partridge", "Partridge", "Pheasant"], "Mine's a Pint!!!"),
        ([], "Lynn, I've pierced my foot on a spike!!"),
        (["Grouse", "Partridge", "Pheasant", "Goose", "Starling", "Robin", "Thrush", "Emu", "PearTree", "Chat", "Dan", "Square", "Toblerone", "Lynn", "AlphaPapa", "BMW", "Graham", "Tool", "Nomad", "Finger", "Hamster"], "Mine's a Pint!!!!!!!!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert part(arg) == expected
