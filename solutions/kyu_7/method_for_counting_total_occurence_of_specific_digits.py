"""Method For Counting Total Occurence Of Specific Digits
https://www.codewars.com/kata/method-for-counting-total-occurence-of-specific-digits

We need a method in the ```List Class``` that may count specific digits from a given list of integers. This marked digits will be given in a second list.
The method ```.count_spec_digits()/.countSpecDigits()``` will accept two arguments, a list of an uncertain amount of integers ```integers_lists/integersLists``` (and of an uncertain amount of digits, too) and a second list, ```digits_list/digitsList``` that has the specific digits to count which length cannot be be longer than 10 (It's obvious, we've got ten digits).
The method will output a list of tuples, each tuple having two elements, the first one will be a digit to count, and second one, its corresponding total frequency in all the integers of the first list. This list of tuples should be ordered with the same order that the digits have in digitsList

Let's see some cases:
```javascript
l = List()

integersList =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digitsList = [1, 3]
l.count_spec_digits(integersList, digitsList) == [(1, 3), (3, 2)]

integersList = [-18, -31, 81, -19, 111, -888]
digitsList = [1, 8, 4]
l.count_spec_digits(integersList, digitsList) == [(1, 7), (8, 5), (4, 0)]

integersList = [-77, -65, 56, -79, 6666, 222]
digitsList = [1, 8, 4]
l.count_spec_digits(integersList, digitsList) == [(1, 0), (8, 0), (4, 0)]
```
```ruby
l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
l.count_spec_digits(integers_list, digits_list) == [(1, 3), (3, 2)]

integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 7), (8, 5), (4, 0)]

integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 0), (8, 0), (4, 0)]
```
```python
l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
l.count_spec_digits(integers_list, digits_list) == [(1, 3), (3, 2)]

integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 7), (8, 5), (4, 0)]

integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) == [(1, 0), (8, 0), (4, 0)]
```
Enjoy it!!
"""


from collections import Counter


class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        counter = Counter(''.join(map(str, integers_list)))
        return [(digit, counter[str(digit)]) for digit in digits_list]
