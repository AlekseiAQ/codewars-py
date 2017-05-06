"""Find the anonymous function
https://www.codewars.com/kata/find-the-anonymous-function

<h1>Find the anonymous function in the array</h1>
Find the anonymous function in the given array and use the function to filter the array

<h3>Input</h3>
Your input. First Parameter will be an array with an anonymous function somewhere in the lot, The second Parameter will be an array which you will filter using the anonymous function you find.

<h3>Output</h3>
Your output. Output a filtered version of the second parameter using the function found in the first parameter.


Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

"""


def find_function(func,arr):
    return filter(filter(callable, func)[0], arr)
