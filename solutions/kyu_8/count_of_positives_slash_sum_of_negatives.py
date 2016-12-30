"""Count of positives / sum of negatives
https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:
<ul>
  <li><strong>C#/Java:</strong> ```new int[] {}``` / ```new int[0]```;</li>
  <li><strong>C++:</strong> ```std::vector<int>()```;</li>
  <li><strong>JavaScript/CoffeeScript/PHP/Haskell:</strong> ```[]```;</li>
</ul>

#ATTENTION!
<strog>The passed array should NOT be changed. Read more <a href="https://en.wikipedia.org/wiki/Side_effect_(computer_science)">here</a>.</strong>

#For example:
```javascript
input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
return [10, -65].
```
```csharp
input int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15} 
return int[] {10, -65}.
```
```java
input int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15} 
return int[] {10, -65}.
```
```cpp
input vector<int> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15} 
return vector<int>  {10, -65}.
```
```haskell

"""


def count_positives_sum_negatives(arr):
    return [sum(1 for el in arr if el > 0), sum(el for el in arr if el < 0)] if arr else []
