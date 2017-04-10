"""Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language
https://www.codewars.com/kata/coding-meetup-number-17-higher-order-functions-series-sort-by-programming-language

You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Given the following input array:

```javascript
var list1 = [  
  { firstName: 'Nikau', lastName: 'R.', country: 'New Zealand', continent: 'Oceania', age: 39, language: 'Ruby' },
  { firstName: 'Precious', lastName: 'G.', country: 'South Africa', continent: 'Africa', age: 22, language: 'JavaScript' },
  { firstName: 'Maria', lastName: 'S.', country: 'Peru', continent: 'Americas', age: 30, language: 'C' },
  { firstName: 'Agustin', lastName: 'V.', country: 'Uruguay', continent: 'Americas', age: 19, language: 'JavaScript' }
];
```
```python
list1 = [  
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]
```
```ruby
list1 = [  
  { "first_name"=>"Nikau", "last_name"=>"R.", "contry"=>"New Zealand", "continent"=>"Oceania", "age"=>39, "language"=>"Ruby" },
  { "first_name"=>"Precious", "last_name"=>"G.", "contry"=>"South Africa", "continent"=>"Africa", "age"=>22, "language"=>"JavaScript" },
  { "first_name"=>"Maria", "last_name"=>"S.", "contry"=>"Peru", "continent"=>"Americas", "age"=>30, "language"=>"C" },
  { "first_name"=>"Agustin", "last_name"=>"V.", "contry"=>"Uruguay", "continent"=>"Americas", "age"=>19, "language"=>"JavaScript" }
]
```
```crystal
list1 = [  
  { "first_name"=>"Nikau", "last_name"=>"R.", "contry"=>"New Zealand", "continent"=>"Oceania", "age"=>39, "language"=>"Ruby" },
  { "first_name"=>"Precious", "last_name"=>"G.", "contry"=>"South Africa", "continent"=>"Africa", "age"=>22, "language"=>"JavaScript" },
  { "first_name"=>"Maria", "last_name"=>"S.", "contry"=>"Peru", "continent"=>"Americas", "age"=>30, "language"=>"C" },
  { "first_name"=>"Agustin", "last_name"=>"V.", "contry"=>"Uruguay", "continent"=>"Americas", "age"=>19, "language"=>"JavaScript" }
]
```

Write a function that returns the array sorted alphabetically by the programming language. In case there are some developers that code in the same language, sort them alphabetically by the first name:  

```javascript
[ 
  { firstName: 'Maria', lastName: 'S.', country: 'Peru', continent: 'Americas', age: 30, language: 'C' },
  { firstName: 'Agustin', lastName: 'V.', country: 'Uruguay', continent: 'Americas', age: 19, language: 'JavaScript' },
  { firstName: 'Precious', lastName: 'G.', country: 'South Africa', continent: 'Africa', age: 22, language: 'JavaScript' },
  { firstName: 'Nikau', lastName: 'R.', country: 'New Zealand', continent: 'Oceania', age: 39, language: 'Ruby' }
];
```
```python
[ 
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" }
]
```
```ruby
[ 
  { "first_name"=>"Maria", "last_name"=>"S.", "contry"=>"Peru", "continent"=>"Americas", "age"=>30, "language"=>"C" },
  { "first_name"=>"Agustin", "last_name"=>"V.", "contry"=>"Uruguay", "continent"=>"Americas", "age"=>19, "language"=>"JavaScript" },
  { "first_name"=>"Precious", "last_name"=>"G.", "contry"=>"South Africa", "continent"=>"Africa", "age"=>22, "language"=>"JavaScript" },
  { "first_name"=>"Nikau", "last_name"=>"R.", "contry"=>"New Zealand", "continent"=>"Oceania", "age"=>39, "language"=>"Ruby" }
]
```
```crystal
[ 
  { "first_name"=>"Maria", "last_name"=>"S.", "contry"=>"Peru", "continent"=>"Americas", "age"=>30, "language"=>"C" },
  { "first_name"=>"Agustin", "last_name"=>"V.", "contry"=>"Uruguay", "continent"=>"Americas", "age"=>19, "language"=>"JavaScript" },
  { "first_name"=>"Precious", "last_name"=>"G.", "contry"=>"South Africa", "continent"=>"Africa", "age"=>22, "language"=>"JavaScript" },
  { "first_name"=>"Nikau", "last_name"=>"R.", "contry"=>"New Zealand", "continent"=>"Oceania", "age"=>39, "language"=>"Ruby" }
]
```





Notes:
 
 - The input array will always be valid and formatted as in the example above.
 - The array does not include developers coding in the same language and sharing the same name.
<br>
<br>
<br>
<br>
<br>

This kata is part of the **Coding Meetup** series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: `forEach, filter, map, reduce, some, every, find, findIndex`. Other approaches to solving the katas are of course possible.

Here is the full list of the katas in the **Coding Meetup** series:

<a href="http://www.codewars.com/kata/coding-meetup-number-1-higher-order-functions-series-count-the-number-of-javascript-developers-coming-from-europe">Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-2-higher-order-functions-series-greet-developers">Coding Meetup #2 - Higher-Order Functions Series - Greet developers</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming">Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-4-higher-order-functions-series-find-the-first-python-developer">Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-5-higher-order-functions-series-prepare-the-count-of-languages">Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-6-higher-order-functions-series-can-they-code-in-the-same-language">Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?</a>

<a href="http://www.codewars.com/kata/coding-meetup-number-7-higher-order-functions-series-find-the-most-senior-developer">Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented">Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse">Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-10-higher-order-functions-series-create-usernames">Coding Meetup #10 - Higher-Order Functions Series - Create usernames</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-11-higher-order-functions-series-find-the-average-age">Coding Meetup #11 - Higher-Order Functions Series - Find the average age</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-12-higher-order-functions-series-find-github-admins">Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-13-higher-order-functions-series-is-the-meetup-language-diverse">Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-14-higher-order-functions-series-order-the-food">Coding Meetup #14 - Higher-Order Functions Series - Order the food</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-15-higher-order-functions-series-find-the-odd-names">Coding Meetup #15 - Higher-Order Functions Series - Find the odd names</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-16-higher-order-functions-series-ask-for-missing-details">Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-17-higher-order-functions-series-sort-by-programming-language">Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language</a>
"""


def sort_by_language(arr):
    return sorted(arr, key=lambda x: (x['language'], x['first_name']))
