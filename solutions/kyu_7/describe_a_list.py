"""Describe a list 
https://www.codewars.com/kata/describe-a-list

Write function describeList which tells if the list is empty or contains only one element or more.
"""


def describeList(l):
    """ describe_list == PEP8 (forced mixedCase by CodeWars) """
    return 'longer' if len(l) > 1 else 'singleton' if l else 'empty'
