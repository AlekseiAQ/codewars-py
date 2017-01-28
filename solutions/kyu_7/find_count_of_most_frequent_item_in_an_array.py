"""Find Count of Most Frequent Item in an Array
https://www.codewars.com/kata/find-count-of-most-frequent-item-in-an-array

Write a program to find count of the most frequent item of an array. 

Assume that input is array of integers.

Ex.:
```
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
```
Most frequent number in example array is -1. It occurs 5 times in input array.

"""


def most_frequent_item_count(collection):
    return max(collection.count(el) for el in set(collection)) if collection else 0
