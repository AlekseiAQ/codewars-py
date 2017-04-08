"""Numerical Palindrome #1
https://www.codewars.com/kata/numerical-palindrome-number-1

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

<p>2332
<br>110011
<br>54322345


For a given number ```num```, write a function to test if it's a numerical palindrome or not and return a boolean (true if it is and false if not). Return "Not valid" if the input is not an integer or less than 0. 

<h2><u>Other Kata in this Series:</u></h2> 
<b>Numerical Palindrome #1</b>
<br><a href="https://www.codewars.com/kata/numerical-palindrome-number-1-dot-5">Numerical Palindrome #1.5</a>
<br><a href="https://www.codewars.com/kata/58de819eb76cf778fe00005c">Numerical Palindrome #2</a>
<br><a href="https://www.codewars.com/kata/58df62fe95923f7a7f0000cc">Numerical Palindrome #3</a>
<br><a href="https://www.codewars.com/kata/58e2708f9bd67fee17000080">Numerical Palindrome #3.5</a>
<br><a href="https://www.codewars.com/kata/58df8b4d010a9456140000c7">Numerical Palindrome #4</a>
<br><a href="https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a">Numerical Palindrome #5</a>

"""


def palindrome(num):
    if isinstance(num, int) and num > 0:
        return(str(num) == str(num)[::-1])
    return "Not valid"
