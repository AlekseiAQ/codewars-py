"""Sum Array with different bases
https://www.codewars.com/kata/sum-array-with-different-bases

You get an array of different numbers to sum up. But there is one problem, those numbers all have different bases.
For example:
```javascript
You get an array of numbers with their base as an input:

[["101",16],["7640",8],["1",9]]
```
```python
You get an array of numbers with their base as an input:

[["101",16],["7640",8],["1",9]]
```

```java
You get an array of BasedNumbers as an input:

public class BasedNumbers{
  String number;
  int base;
}

[{number:"101", base:16}, {number:"7640", base:8}, {number:"1", base:9}]
```
The output should be the sum as an integer value with a base of 10, so according to the example this would be:

4258
```javascript
A few more examples:
[["101",2], ["10",8]] --> 13
[["ABC",16], ["11",2]] --> 2751
```
```python
A few more examples:
[["101",2], ["10",8]] --> 13
[["ABC",16], ["11",2]] --> 2751
```
```java
A few more examples:
[{number:"101", base:2}, {number:"10", base:8}] --> 13
[{number:"ABC", base:16}, {number:"11", base:2}] --> 2751
```
Bases can be between 2 and 36 (2<=base<=36)
"""


def sum_it_up(numbers_with_bases):
    return sum(int(number, base) for number, base in numbers_with_bases)
