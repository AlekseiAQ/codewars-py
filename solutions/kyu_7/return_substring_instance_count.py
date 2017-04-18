"""Return substring instance count
https://www.codewars.com/kata/return-substring-instance-count

Complete the solution so that it returns the number of times the search_text is found within the full_text. 

Usage example:

```ruby
solution('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
solution('aaabbbcccc', 'bbb') # should return 1
```
"""


def solution(full_text, search_text):
    return full_text.count(search_text)
