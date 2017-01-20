"""Processes
https://www.codewars.com/kata/processes

In this task you have to code process planner.

You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of _[process\_name, start\_thing, end\_thing]_). You must return  names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

If start already equals end, return [], since no path is required.

Example: 

```javascript
var test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

processes('field', 'bread', test_processes); // should return ['gather', 'mill', 'bake']
processes('field', 'ferrari', test_processes); // should return []
processes('field', 'field', test_processes); // should return [], since no processes are needed
```
```python
test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
processes('field', 'ferrari', test_processes) # should return []
processes('field', 'field', test_processes) # should return [], since no processes are needed
```
```coffeescript
test_processes = [
    ['gather', 'field', 'wheat']
    ['bake', 'flour', 'bread']
    ['mill', 'wheat', 'flour']
]

processes 'field', 'bread', test_processes # should return ['gather', 'mill', 'bake']
processes 'field', 'ferrari', test_processes # should return []
processes 'field', 'field', test_processes # should return [], since no processes are needed
```

Good luck!
"""


def processes(start, end, processes):
    path = []
    while start != end:
        tmp_start = start
        for process, from_res, to_res in processes:
            if start == from_res:
                if path and process == path[-1]:
                	continue
                start = to_res
                path.append(process)
        if tmp_start == start:
            return []
    return path

# rain          ice statue
# ['collect', 'rain', 'water']
# ['freeze', 'water', 'ice']
# ['melt', 'ice', 'water']
# ['boil', 'ice', 'steam']
# ['carve', 'ice', 'ice statue']]
