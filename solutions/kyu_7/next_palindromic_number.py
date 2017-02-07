"""Next Palindromic Number.
https://www.codewars.com/kata/next-palindromic-number

There were and still are many problem in CW about palindrome numbers and palindrome strings. We suposse that you know which kind of numbers they are. If not, you may search about them using your favourite search engine.

In this kata you will be given a positive integer, ```val``` and you have to create the function ```next_pal()```(```nextPal``` Javascript) that will output the smallest palindrome number higher than ```val```.

Let's see:
```python
For Python
next_pal(11) == 22

next_pal(188) == 191

next_pal(191) == 202

next_pal(2541) == 2552
```
```javascript
For Javascript
nextPal(11) == 22

nextPal(188) == 191

nextPal(191) == 202

nextPal(2541) == 2552
```
```csharp
For C#
Kata.NextPal(11) == 22

Kata.NextPal(188) == 191

Kata.NextPal(191) == 202

Kata.NextPal(2541) == 2552
```
```ruby
For Ruby
next_pal(11) == 22

next_pal(188) == 191

next_pal(191) == 202

next_pal(2541) == 2552
```
```coffeescript
For CoffeeScript
nextPal(11) == 22

nextPal(188) == 191

nextPal(191) == 202

nextPal(2541) == 2552
```
```haskell
For Haskell
nextPal 11 == 22

nextPal 188 == 191

nextPal 191 == 202

nextPal 2541 == 2552
```

You will be receiving values higher than 10, all valid.

Enjoy it!!
"""


def next_pal(val):
    while True:
        val += 1
        if str(val)[::-1] == str(val):
            return val
