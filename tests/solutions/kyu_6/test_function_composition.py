"""Function Composition"""

import pytest

from solutions.kyu_6.function_composition import compose


def add1(a):
    return a + 1


def this(a):
    return a


EXAMPLES = (
    ('args', 'params', 'expected'),
    [
        ((add1, this), (0, ), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, params, expected):
    assert compose(*args)(*params) == expected


# import unittest


# class TestCompose(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(compose(add1, this)(0), 1)
        
#     def test_2(self):
#         self.assertEqual(compose(add1, this)(1, 2, 3), 5)
