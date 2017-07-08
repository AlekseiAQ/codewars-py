"""Unary function chainer"""

import pytest

from solutions.kyu_6.unary_function_chainer import chained


def f1(x):
    return x*2


def f2(x):
    return x+2


def f3(x):
    return x**2


def f4(x):
    return x.split()


def f5(xs):
    return [x[::-1].title() for x in xs]


def f6(xs):
    return "_".join(xs)


def test_chained_0():
    assert chained([f1, f2, f3])(0) == 4


def test_chained_1():
    assert chained([f1, f2, f3])(2) == 36


def test_chained_2():
    assert chained([f3, f2, f1])(2) == 12


def test_chained_3():
    assert chained([f4, f5, f6])("lorem ipsum dolor") == "Merol_Muspi_Rolod"
