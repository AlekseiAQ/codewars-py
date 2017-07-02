"""Smallest unused ID
https://www.codewars.com/kata/smallest-unused-id

Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the <b>smallest unused ID</b> for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!
"""


def next_id(arr):
    arr = set(arr)
    t = 0
    while t in arr:
        t += 1
    return t
