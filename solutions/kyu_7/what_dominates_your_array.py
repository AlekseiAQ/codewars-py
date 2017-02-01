"""What dominates your array?
https://www.codewars.com/kata/what-dominates-your-array

A zero-indexed array ```arr``` consisting of n integers is given. The dominator of array ```arr``` is the value that occurs in <b>more</b> than half of the elements of ```arr```.<br/>
For example, consider array ```arr``` such that ```arr = [3,4,3,2,3,1,3,3]```<br/> The dominator of ```arr``` is 3 because it occurs in 5 out of 8 elements of ```arr``` and 5 is more than a half of 8.<br/>
Write a function ```dominator(arr)``` that, given a zero-indexed array ```arr``` consisting of n integers, returns the dominator of ```arr```. The function should return −1 if array does not have a dominator. All values in ```arr``` will be >=0.
"""


from collections import Counter


def dominator(arr):
    if not arr:
        return -1
    k, v = Counter(arr).most_common(1)[0]
    return k if v > len(arr) / 2 else -1
