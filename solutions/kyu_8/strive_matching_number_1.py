"""Strive Matching #1
https://www.codewars.com/kata/strive-matching-number-1

[Strive][1] is a new developer-centric service that is focused on presenting software developers with jobs that excite us. Strive discovers these jobs for developers based on a number of factors.

One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we generally have a rough idea of the minimum salary we would be satisfied with. 

Let's give this a try. We'll create a function `match` which takes a `candidate` and a `job`, which will either return a boolean indicating whether the job is a valid match for the candidate. 

A candidate will have a minimum salary, so it will look like this:

```javascript
let candidate = {
  minSalary: 120000
}
```
```ruby
candidate = {
  'min_salary': 120000
}
```
```python
candidate = {
  'min_salary': 120000
}
```
```csharp
Candidate candidate = 
  new Candidate(MinSalary: 120000);
```

A job will have a maximum salary, so it will look like this: 

```javascript 
let job = {
  maxSalary: 140000
}
```
```ruby
job = { 
  'max_salary': 140000
}
```
```python
job = {
  'max_salary': 140000
}
```
```csharp
Job job = 
  new Job(MaxSalary: 140000);
```

If either the candidate's minimum salary or the job's maximum salary is not present, throw an error. 

For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. However, let's also include 10% wiggle room (deducted from the candidate's minimum salary) in case the candidate is a rockstar who enjoys programming on Codewars in their spare time. The company offering the job may be able to work something out. 

---

Of course, compensation is only one filter that will help lead to our satisfaction. What other factors can [Strive][1] use to discover jobs that will excite developers? 

Continue on with Kata:

- [Strive Matching #2][3]
- [Strive Matching #3][2]

Or join this [Kata's discussion][4] to let us know what you think! 

[4]:http://www.codewars.com/kata/strive-matching-number-1/discuss/javascript
[3]:http://www.codewars.com/kata/strive-matching-number-2
[2]:http://www.codewars.com/kata/strive-matching-number-3
[1]:http://www.strive.co?utm_source=codewars&utm_campaign=striveKata
"""


def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']
