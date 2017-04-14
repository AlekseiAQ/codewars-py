"""Find The Parity Outlier
https://www.codewars.com/kata/find-the-parity-outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36] 
  
Should return: 11

[160, 3, 1719, 19, 11, 13, -21] 
  
Should return: 160

"""


def find_outlier(integers):
    for i in range(len(integers) - 1):
        if integers[i] % 2 == integers[i + 1] % 2:
            continue
        else:
            try:
                if integers[i] % 2 == integers[i + 2] % 2:
                    return integers[i + 1]
                else:
                    return integers[i]
            except IndexError:
                return integers[i + 1]
