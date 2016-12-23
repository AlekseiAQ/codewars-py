"""Twisted Sum
https://www.codewars.com/kata/twisted-sum

Find the sum of the digits of all the numbers from 1 to N (both ends included).

For N = 10 the sum is 1+2+3+4+5+6+7+8+9+(1+0) = 46

For N = 11 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) = 48

For N = 12 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) +(1+2)= 51
"""


def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))
