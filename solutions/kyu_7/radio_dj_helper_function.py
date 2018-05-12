"""Radio DJ helper function
https://www.codewars.com/kata/radio-dj-helper-function

## The Problem

James is a DJ at a local radio station. As it's getting to the top of the hour, he needs to find a song to play that will be short enough to fit in before the news block. He's got a database of songs that he'd like you to help him filter in order to do that.

## What To Do

Create `longestPossible`(`longest_possible` in python and ruby) helper function that takes 1 integer argument which is a maximum length of a song in seconds.

`songs` is an array of objects which are formatted as follows:

```javascript
{artist: 'Artist', title: 'Title String', playback: '04:30'}
```
```python
{'artist': 'Artist', 'title': 'Title String', 'playback': '04:30'}
```
```ruby
{artist: 'Artist', title: 'Title String', playback: '04:30'}
```

You can expect playback value to be formatted exactly like above.

Output should be a title of the longest song from the database that matches the criteria of not being longer than specified time. If there's no songs matching criteria in the database, return `false`.

"""

import datetime
import operator
import time

songs = [
    {'title': 'Keyleigh', 'playback': '03:36', 'artist': 'Marillion'},
    {'title': 'Time', 'playback': '06:48', 'artist': 'Pink Floyd'},
    {'title': 'YYZ', 'playback': '04:27', 'artist': 'Rush'},
    {'title': 'Days To Come', 'playback': '03:50', 'artist': 'Bonobo'},
    {'title': 'Yellow', 'playback': '04:32', 'artist': 'Coldplay'},
    {'title': 'Like Eating Glass', 'playback': '04:22',
     'artist': 'Bloc Party'},
    {'title': 'For Reasons Unknown', 'playback': '03:30',
     'artist': 'The Killers'},
    {'title': 'Teddy Picker', 'playback': '03:25',
     'artist': 'Arctic Monkeys'},
    {'title': 'Surfing With The Alien', 'playback': '04:34',
     'artist': 'Joe Satriani'}
]


def to_seconds(playback):
    t = time.strptime(playback, '%M:%S')
    playback_in_seconds = int(
        datetime.timedelta(
            hours=t.tm_hour,
            minutes=t.tm_min,
            seconds=t.tm_sec
        ).total_seconds())
    return playback_in_seconds

def longest_possible(playback):
    suitable_songs = []
    for song in songs:
        if to_seconds(song['playback']) < playback:
            suitable_songs.append(song)

    if suitable_songs:
        result = max(suitable_songs, key=lambda song: song['playback'])
        return result['title']

    return False
