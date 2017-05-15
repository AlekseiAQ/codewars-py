"""Ordering  the words!
https://www.codewars.com/kata/ordering-the-words

<h3>Description:</h3>

Given a string, you need to write a method that order every letter in this string in ascending order.


Also, you should validate that the given string is not empty or null. If so, the method should return: 
```java
"Invalid String!";
```
```python
"Invalid String!"
```
```ruby
"Invalid String!"
```
```javascript
"Invalid String!"
```

<h3>Examples</h3>
```java
new Ordering().orderWord("hello world") => " dehllloorw"
new Ordering().orderWord("bobby") => "bbboy"
new Ordering().orderWord("") => "Invalid String!"
```
```python
order_word("hello world") => " dehllloorw"
order_word("bobby") => "bbboy"
order_word("") => "Invalid String!"
```
```ruby
order_word("hello world") => " dehllloorw"
order_word("bobby") => "bbboy"
order_word("") => "Invalid String!"
```
```javascript
orderWord("hello world") => " dehllloorw"
orderWord("bobby") => "bbboy"
order_word("") => "Invalid String!"
```

<h4>Notes</h4>
• the given string can be lowercase and uppercase.<br />
• the string could include spaces or other special characters like '# ! or ,'

<strong>Good luck! Hope you enjoy it</strong>
"""


def order_word(s):
    return "".join(sorted(s)) if s else "Invalid String!"
