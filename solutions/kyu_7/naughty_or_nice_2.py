"""Naughty or Nice?
https://www.codewars.com/kata/naughty-or-nice-2

In this kata, you will write a function that receives an array of string and returns a string that is either ```'naughty'``` or ```'nice'```.
Strings that start with the letters ```b```, ```f```, or ```k``` are ```naughty```. Strings that start with the letters ```g```, ```s```, or ```n``` are ```nice```. Other strings are neither naughty nor nice.

If there is an equal amount of bad and good actions, return ```'naughty'```

Examples:

```python
bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
whatListAmIOn(bad_actions)
#-> 'naughty'
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
whatListAmIOn(good_actions)
#-> 'nice'
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
whatListAmIOn(actions)
#-> 'naughty'
```
```ruby
bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
what_list_am_i_on(bad_actions)
#-> 'naughty'
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
what_list_am_i_on(good_actions)
#-> 'nice'
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
what_list_am_i_on(actions)
#-> 'naughty'
```
```php
$bad_actions = ["broke someone's window", "fought over a toaster", "killed a bug"];
what_list_am_i_on($bad_actions); // => "naughty"
$good_actions = ["got someone a new car", "saved a man from drowning", "never got into a fight"];
what_list_am_i_on($good_actions); // => "nice"
$actions = ["broke a vending machine", "never got into a fight", "tied someone's shoes"];
what_list_am_i_on($actions); // => "naughty"
```
```crystal
bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
what_list_am_i_on(bad_actions)
#-> 'naughty'
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
what_list_am_i_on(good_actions)
#-> 'nice'
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
what_list_am_i_on(actions)
#-> 'naughty'
```
"""


def whatListAmIOn(actions):
    """ what_list_am_i_on == PEP8 (forced mixedCase by CodeWars) """
    naughty = sum(word[0] in 'bfk' for word in actions)
    nice = sum(word[0] in 'gsn' for word in actions)
    return "naughty" if naughty >= nice else 'nice'
