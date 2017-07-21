"""Simple Encryption #1 - Alternating Split
https://www.codewars.com/kata/simple-encryption-number-1-alternating-split

For building the encrypted string:<br/>Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.<br/>
Do this n times!

Examples:
```
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
```

Write two methods:
```csharp
string Encrypt(string text, int n)
string Decrypt(string encryptedText, int n)
```
```cpp
std::string encrypt(std::string text, int n)
std::string decrypt(std::string encryptedText, int n)
```
```java
String encrypt(final String text, final int n)
String decrypt(final String encryptedText, final int n)
```
```javascript
function encrypt(text, n)
function decrypt(encryptedText, n)
```
```coffeescript
encrypt = (text, n) ->
decrypt = (encryptedText, n) ->
```
```python
def encrypt(text, n)
def decrypt(encrypted_text, n)
```
```ruby
def encrypt(text, n)
def decrypt(encrypted_text, n)
```
```php
function encrypt($text, $n)
function decrypt($text, $n)
```

For both methods:<br/>
If the input-string is null or empty return exactly this value!<br/>
If n is <= 0 then return the input text.<br/>

This kata is part of the Simple Encryption Series:<br>
<a href="https://www.codewars.com/kata/simple-encryption-number-1-alternating-split" taget=_blank>Simple Encryption #1 - Alternating Split</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-2-index-difference" taget=_blank>Simple Encryption #2 - Index-Difference</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around" taget=_blank>Simple Encryption #3 - Turn The Bits Around</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-4-qwerty" taget=_blank>Simple Encryption #4 - Qwerty</a><br>

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""


from itertools import zip_longest


def decrypt_iteration(text):
    middle_point = int(len(text) / 2)
    return ''.join(a + b for a, b in list(zip_longest(text[middle_point:],
                                                      text[:middle_point],
                                                      fillvalue='')))


def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    while n:
        n -= 1
        encrypted_text = decrypt_iteration(encrypted_text)
    return encrypted_text


def encrypt_iteration(text):
    return text[1::2] + text[::2]


def encrypt(text, n):
    if n < 1:
        return text
    while n:
        n -= 1
        text = encrypt_iteration(text)
    return text
