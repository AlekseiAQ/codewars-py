"""How many e-mails we sent today?
https://www.codewars.com/kata/how-many-e-mails-we-sent-today

Every day we can send from the server a certain limit of e-mails.

<h1>Task:</h1>
Write a function that will return the integer number of e-mails sent in the percentage of the limit.

Example:
```
limit       - 1000;
emails sent - 101;
return      - 10%; // becouse integer from 10,1 = 10
```

<b>Arguments:</b>
<ul>
  <li>Integer, limit;</li>
  <li>Integer, number of e-mails sent today;</li>
</ul>

<b>When:</b>
<ul>
  <li>the argument ```$sent = 0```, then return the message: "No e-mails sent";</li>
  <li>the argument ```$sent >= $limit```, then return the message: "Daily limit is reached";</li>
  <li>the argument ```$limit is empty```, then default ```$limit = 1000``` emails;</li>
</ul>

<b>Good luck!</b>
"""


def get_percentage(sent, limit=1000):
    if sent == 0:
        return "No e-mails sent"
    if sent >= limit:
        return "Daily limit is reached"
    return "{}%".format(int(sent / limit * 100))
