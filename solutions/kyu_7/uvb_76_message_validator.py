"""UVB-76 Message Validator
https://www.codewars.com/kata/uvb-76-message-validator

In Russia, there is an army-purposed station named UVB-76 or "Buzzer" (see also https://en.wikipedia.org/wiki/UVB-76). Most of time specific "buzz" noise is being broadcasted, but on very rare occasions, the buzzer signal is interrupted and a voice transmission in Russian takes place. Transmitted messages have always the same format like this:

<b> MDZHB 01 213 SKIF 38 87 23 95 </b>

or:

<b> MDZHB 80 516 GANOMATIT 21 23 86 25 </b>

Message format consists of following parts:
<ul>
 <li> Initial keyword "MDZHB"; </li>
 <li> Two groups of digits, 2 digits in first and 3 in second ones; </li>
 <li> Some keyword of arbitrary length consisting only of uppercase letters; </li>
 <li> Final 4 groups of digits with 2 digits in each group. </li>
 </ul>

Your task is to write a function that can validate the correct UVB-76 message. Function should return "True" if message is in correct format and "False" otherwise.
"""


import re


def validate(message: str) -> bool:
    return bool(re.match(r'^MDZHB \d{2} \d{3} [A-Z]+( \d{2}){4}$', message))
