"""Sum of Pairs
https://www.codewars.com/kata/sum-of-pairs

----
Sum of Pairs
----

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

```python
sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
```

Negative numbers and duplicate numbers can and will appear.

__NOTE:__ There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""


def sum_pairs(ints, s):
    min_el = None
    min_pair = None
    list_len = len(ints)
    
    for i, el1 in enumerate(ints):
        if min_el and i >= min_el:
            return min_pair
        
        for j in range(i+1, list_len):
            el2 = ints[j]
            if el1 + el2 == s:
                if min_el is None or j < min_el:
                    min_el = j
                    min_pair = [el1, el2]
                    list_len = j
                break

    return min_pair

# [10, 3, 5, 7, 2, 3, 7, 1, 2, 3, 4 , 5]
