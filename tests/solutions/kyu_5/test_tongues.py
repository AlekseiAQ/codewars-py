"""Tongues"""

import pytest

from solutions.kyu_5.tongues import tongues

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Ita dotf ni dyca nsaw ecc.', 'One ring to rule them all.'),
        ('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.', 'Now is the time for all good men to come to the aid of their country.'),
        ('Giydhlida etr hakat uaedh efi iyd gidagensadh pdiyfsn ytni nsoh', 'Fourscore and seven years ago our forefathers brought unto this'),
        ('litnotatn e tam tenoit.', 'continent a new nation.'),
        ('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.', 'The quick brown fox jumped over the lazy dogs.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert tongues(arg) == expected
