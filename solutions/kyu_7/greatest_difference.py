"""Greatest Difference
https://www.codewars.com/kata/greatest-difference

Your task is to find the number couple with the greatest difference from a given array of number-couples. 

All number couples will be given as strings and all numbers in them will be positive integers.  

For instance: ['56-23','1-100']; in this case, you should identify '1-100' as the number couple with the greatest difference and return it.

In case there are more than one option, for instance ['1-3','5-7','2-3'], you should identify whichever is first, so in this case '1-3'. 

If there is no difference, like so ['11-11', '344-344'], return false.




"""


def diff(arr):
    max_diff = max_pair = False
    for pair in arr:
        x, y = map(int, pair.split('-'))
        current = abs(x - y)
        if current > max_diff:
            max_diff = current
            max_pair = pair
    return max_pair
