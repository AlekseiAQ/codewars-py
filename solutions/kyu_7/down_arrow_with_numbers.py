"""Down Arrow With Numbers
https://www.codewars.com/kata/down-arrow-with-numbers

Given a number `n`, make a down arrow shaped pattern.

For example, when `n = 5`, the output would be:

    123454321
     1234321
      12321
       121
        1

and for `n = 11`, it would be:

    123456789010987654321
     1234567890987654321
      12345678987654321
       123456787654321
        1234567654321
         12345654321
          123454321
           1234321
            12321
             121
              1

An important thing to note in the above example is that the numbers greater than 9 still stay single digit, like after 9 it would be 0 - 9 again instead of 10 - 19.

Note: There are spaces for the indentation on the left of each line and no spaces on the right.

Have fun!

"""


from itertools import chain


def make_string(n, i):
    padding = " " * (n - i)
    difference = n - i
    return padding + ''.join(str(d % 10)
                             for d in chain(range(1, n-difference+1),
                                            range(n-difference-1, 0, -1)))


def get_a_down_arrow_of(n):
    if n < 1:
        return ""
    return "\n".join(make_string(n, i) for i in reversed(range(1, n+1)))
