"""Time Converter: hours, minutes, seconds and milliseconds
https://www.codewars.com/kata/time-converter-hours-minutes-seconds-and-milliseconds

Given a time in a time format class, return it without year, month and day.

It should return a string including milliseconds with 3 decimals.

Example:
```ruby
Time.new(2016, 2, 8, 16, 42, 59)
#Should return: 
"16:42:59,000"
```
```python
datetime(2016, 2, 8, 16, 42, 59)
#Should return: 
"16:42:59,000"
```
```javascript
new Date(2016, 2, 8, 16, 42, 59)
//Should return: 
"16:42:59,000"
```
"""


def convert(time):
    return "{:02}:{:02}:{:02},{:03}".format(
        time.hour, time.minute, time.second, time.microsecond // 1000)
