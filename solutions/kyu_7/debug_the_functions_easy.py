"""Debug the functions EASY
https://www.codewars.com/kata/debug-the-functions-easy

<h1 id="heading">Debug the functions</h1>

<i>Should be easy, begin by looking at the code. Debug the code and the functions should work.</i>

<i>There are three functions: ```Multiplication (x)``` ```Addition (+)``` and ```Reverse (!esreveR)```</i>

<style>
i {
  font-size:16px;
}

#heading {
  padding: 2em;
  text-align: center;
  background-color: #0033FF;
  width: 100%;
  height: 5em;
}
</style>
"""


import operator
import functools


def multi(l_st):
    return functools.reduce(operator.mul, l_st, 1)

def add(l_st):
    return sum(l_st)

def reverse(strng):
    return strng[::-1]
