"""Processes"""

import pytest

from solutions.kyu_5.processes import processes_


test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

EXAMPLES = (
    ('args', 'expected'),
    [
        (('field', 'bread', test_processes), ['gather', 'mill', 'bake']),
        (('field', 'ferrari', test_processes), []),
        (('field', 'field', test_processes), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert processes_(*args) == expected
