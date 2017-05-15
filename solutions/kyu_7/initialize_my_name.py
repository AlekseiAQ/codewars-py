"""Initialize my name
https://www.codewars.com/kata/initialize-my-name

Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

For example,

```
'Jack Ryan' => 'Jack Ryan'
'Lois Mary Lane' => 'Lois M. Lane'
'Dimitri' => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
```
"""


def initializeNames(name):
    """ initialize_names == PEP8 (forced mixedCase by CodeWars) """
    names = name.split()
    names[1:-1] = map(lambda n: n[0] + '.', names[1:-1])
    return ' '.join(names)
