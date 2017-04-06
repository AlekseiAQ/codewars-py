"""Generate user links
https://www.codewars.com/kata/generate-user-links

# Generate user links
Your task is to create userlinks for the url, you will be given a username and must return a valid link.

## Example
```
generate_link('matt c')
http://www.codewars.com/users/matt%20c
```

### reference
use this as a reference [encoding](http://www.w3schools.com/tags/ref_urlencode.asp)
"""


from urllib.parse import quote


def generate_link(user):
    return 'http://www.codewars.com/users/' + quote(user)
