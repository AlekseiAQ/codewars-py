"""Find Added 
https://www.codewars.com/kata/find-added

You are given two strings (st1, st2) as inputs.  Your task is to return a string containing the numbers in st2 which are not in str1. Make sure the numbers are returned in ascending order.
All inputs will be a string of numbers.

Here are some examples:

```findAdded('4455446', '447555446666');   // '56667' ``` <br>
```findAdded('44554466', '447554466');   // '7'``` <br>
```findAdded('9876521', '9876543211');   // '134' ``` <br>
```findAdded('678', '876');   // '' ``` <br>
```findAdded('678', '6');   // '' ``` <br>


"""


from collections import Counter


def find_added(st1, st2):
    return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))
