"""How much coffee do you need?
https://www.codewars.com/kata/how-much-coffee-do-you-need

Everybody know that you passed to much time awake during night time...

Your task here is to define how much coffee you need to stay awake after your night. 
You will have to complete a function that take an array of events in arguments, according to this list you will return the number of coffee you need to stay awake during day time. **Note**: If the count exceed 3 please return 'You need extra sleep'.

The list of events can contain the following:

- You come here, to solve some kata ('cw').

- You have a dog or a cat that just decide to wake up too early ('dog' | 'cat').

- You just watch a movie ('movie').

- Other events can be present and it will be represent by arbitrary string, just ignore this one.

Each event can be downcase/lowercase, or uppercase. If it is downcase/lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.

"""


from collections import Counter


def how_much_coffee(events):
    c = Counter(events)
    r = sum(c[event] for event in ['cw', 'cat', 'dog', 'movie']) +\
        sum(c[event] * 2 for event in ['CW', 'CAT', 'DOG', 'MOVIE'])
    return 'You need extra sleep' if r > 3 else r
