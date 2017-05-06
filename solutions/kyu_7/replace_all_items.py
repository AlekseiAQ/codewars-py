"""Replace all items
https://www.codewars.com/kata/replace-all-items

Write function `replaceAll` (Python: `replace_all`) that will replace all occuriencies of an item with another.

__Python__: The function has to work for strings and lists.

Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]

```swift
replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2) // [2,2,2]
```
"""


def replace_all(obj, find, replace):
    if isinstance(obj, str):
        return obj.replace(find, replace)
    else:
        return [replace if x == find else x for x in obj]
