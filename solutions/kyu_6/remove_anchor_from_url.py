"""Remove anchor from URL
https://www.codewars.com/kata/remove-anchor-from-url

Complete the function/method so that it returns the url with anything after the anchor (#) removed. 

Examples:

```javascript
// returns 'www.codewars.com'
removeUrlAnchor('www.codewars.com#about')

// returns 'www.codewars.com?page=1' 
removeUrlAnchor('www.codewars.com?page=1') 

```

```coffeescript
# returns 'www.codewars.com'
removeUrlAnchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1' 
removeUrlAnchor('www.codewars.com?page=1') 

```

```ruby
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1' 
remove_url_anchor('www.codewars.com?page=1') 
```
```python
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1' 
remove_url_anchor('www.codewars.com?page=1') 
```
"""


def remove_url_anchor(url):
    return url.split('#')[0]
