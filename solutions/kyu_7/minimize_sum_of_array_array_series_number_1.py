"""Minimize  Sum Of Array (Array Series #1)
https://www.codewars.com/kata/minimize-sum-of-array-array-series-number-1

# Introduction and Warm-up (Highly recommended)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)
___

# Task

**_Given_** an **_array of intgers_** , **_Find the minimum sum_** which is obtained *from summing each Two integers product* .
___

# Notes

* **_Array/list_** *will contain* **_positives only_** .
* **_Array/list_** *will always has* **_even size_**
___

# Input >> Output Examples

```cpp
1- minSum({5,4,2,3}) ==> return (22)
```

## **_Explanation_**:

* **_The minimum sum_** *obtained from summing each two integers product* ,  ` 5*2 + 3*4 = 22`
___

```cpp
2- minSum({12,6,10,26,3,24}) ==> return (342)
```

## **_Explanation_**:

* **_The minimum sum_** *obtained from summing each two integers product* ,  ` 26*3 + 24*6 + 12*10 = 342`

___

```cpp
3- minSum({9,2,8,7,5,4,0,6}) ==> return (74)
```

## **_Explanation_**:

* **_The minimum sum_** *obtained from summing each two integers product* ,  ` 9*0 + 8*2 +7*4 +6*5 = 74`

___

```javascript
minSum({5,4,2,3}) // return 22

Explanation ::
5*2 +3*4 = 22

minSum({12,6,10,26,3,24}) // return 342

Explanation ::
26*3 + 24*6 + 12*10 = 342

minSum({9,2,8,7,5,4,0,6}) // return 74

Explanation ::
9*0 + 8*2 +7*4 +6*5 = 74

```

```python
minSum({5,4,2,3}) // return 22

Explanation ::
5*2 +3*4 = 22

minSum({12,6,10,26,3,24}) // return 342

Explanation ::
26*3 + 24*6 + 12*10 = 342

minSum({9,2,8,7,5,4,0,6}) // return 74

Explanation ::
9*0 + 8*2 +7*4 +6*5 = 74

```

```c
minSum({5,4,2,3},4) // return 22

Explanation ::
5*2 +3*4 = 22

minSum({12,6,10,26,3,24},6) // return 342

Explanation ::
26*3 + 24*6 + 12*10 = 342

minSum({9,2,8,7,5,4,0,6},8) // return 74

Explanation ::
9*0 + 8*2 +7*4 +6*5 = 74
```
___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou
"""


def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))
