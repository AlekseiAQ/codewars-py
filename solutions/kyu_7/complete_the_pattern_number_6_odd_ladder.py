"""Complete The Pattern #6 - Odd Ladder
https://www.codewars.com/kata/complete-the-pattern-number-6-odd-ladder

###Task:

You have to write a function `pattern` which creates the following pattern (see examples) up to the desired number of rows.

* If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

* If any even number is passed as argument then the pattern should last upto the largest odd number which is smaller than the passed even number.

###Examples:

pattern(9):

    1
    333
    55555
    7777777
    999999999

pattern(6):

    1
    333
    55555

```Note: There are no spaces in the pattern```

```Hint: Use \n in string to jump to next line```

"""


def pattern(n):
    return '\n'.join(str(i) * i for i in range(1, n + 1, 2))
