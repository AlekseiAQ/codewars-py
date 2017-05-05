"""Broken sequence
https://www.codewars.com/kata/broken-sequence

You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.

In short: an **invalid sequence** (a string with non numeric character) must return 1, an **already complete (or empty) sequence** must return 0; a **broken sequence** with more than one number missing should return the lowest missing number; otherwise return the missing number.

**Note that the input may be with random order.**

E.g.
```java
new BrokenSequence().findMissingNumber("1 3 2 5") // returns 4, because 4 is missing
```
```java
new BrokenSequence().findMissingNumber("1 2 3 4") // returns 0, because the sequence isn't broken
```
```java
new BrokenSequence().findMissingNumber("1 5") // returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4
```
```java
new BrokenSequence().findMissingNumber("2 1 4 3 a") // returns 1, because it's an invalid sequence. in this case, it's invalid because contain a non numerical character
```
```python
find_missing_number("1 3 2 5") # returns 4, because 4 is missing
```
```python
find_missing_number("1 2 3 4") # returns 0, because the sequence isn't broken
```
```python
find_missing_number("1 5") # returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4
```
```python
find_missing_number("2 1 4 3 a") # returns 1, because it's an invalid sequence. in this case, it's invalid because contain a non numerical character
```
```ruby
find_missing_number("1 3 2 5") # returns 4, because 4 is missing
```
```ruby
find_missing_number("1 2 3 4") # returns 0, because the sequence isn't broken
```
```ruby
find_missing_number("1 5") # returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4
```
```ruby
find_missing_number("2 1 4 3 a") # returns 1, because it's an invalid sequence. in this case, it's invalid because contain a non numerical character
```
```javascript
findMissingNumber("1 3 2 5") // returns 4, because 4 is missing
```
```javascript
findMissingNumber("1 2 3 4") // returns 0, because the sequence isn't broken
```
```javascript
findMissingNumber("1 5") // returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4
```
```javascript
findMissingNumber("2 1 4 3 a") // returns 1, because it's an invalid sequence. in this case, it's invalid because contain a non numerical character
```
"""


def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = set(int(a) for a in sequence.split())
    except ValueError:
        return 1
    for b in range(1, max(sequence) + 1):
        if b not in sequence:
            return b
    return 0
