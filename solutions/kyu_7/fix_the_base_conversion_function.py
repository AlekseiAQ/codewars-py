"""Fix the base conversion function!
https://www.codewars.com/kata/fix-the-base-conversion-function

Poor Cade has got his number conversions mixed up again!

Fix his ```convert_num()``` function so it correctly converts a base-10 ```int```eger, 
to the selected of ```bin```ary or ```hex```adecimal.

```#The output should be a string at all times```

```python
convert_num(number, base):
    if 'base' = hex:
        return int(number, 16)
    if 'base' = bin:
        return int(number, 2)
    return (Incorrect base input)
```
Please note, invalid ```number``` or ```base``` inputs will be tested.
In the event of an invalid ```number/base``` you should return:
```python
"Invalid number input"
or
"Invalid base input"
```
For each respectively.

Good luck coding! :D
"""


def convert_num(number, base):
    try:
        if base == 'hex':
            return hex(number)
        if base == 'bin':
            return bin(number)
        return 'Invalid base input'
    except TypeError:
        return 'Invalid number input'
