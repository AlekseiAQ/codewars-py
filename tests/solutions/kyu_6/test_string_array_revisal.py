"""String  array revisal"""

import pytest

from solutions.kyu_6.string_array_revisal import dup

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"],
            ['codewars', 'picaniny', 'hubububo']),
        (["abracadabra", "allottee", "assessee"],
            ['abracadabra', 'alote', 'asese']),
        (["kelless", "keenness"],
            ['keles', 'kenes']),
        (["Woolloomooloo", "flooddoorroommoonlighters", "chuchchi"],
            ['Wolomolo', 'flodoromonlighters', 'chuchchi']),
        (["adanac", "soonness", "toolless", "ppellee"],
            ['adanac', 'sones', 'toles', 'pele']),
        (["callalloo", "feelless", "heelless"],
            ['calalo', 'feles', 'heles']),
        (["putteellinen", "keenness"],
            ['putelinen', 'kenes']),
        (["kelless", "voorraaddoosspullen", "achcha"],
            ['keles', 'voradospulen', 'achcha']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert dup(arg) == expected
