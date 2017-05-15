"""Slaphead
https://www.codewars.com/kata/slaphead

Being a bald man myself, I know the feeling of needing to keep it clean shaven. Nothing worse that a stray hair waving in the wind. 
 
You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them. 

You should return the original string, but with any stray hairs removed. Keep count of them though, as there is a second element you need to return:

0 hairs --> "Clean!"<br>
1 hair --> "Unicorn!"<br>
2 hairs --> "Homer!"<br>
3-5 hairs --> "Careless!"<br>
>5 hairs --> "Hobo!"

So for this head: "------/------" you should return:<br>

["-------------", "Unicorn!"]
"""


from collections import Counter


def bald(s):
    RESULT = {
        0: "Clean!",
        1: "Unicorn!",
        2: "Homer!",
    }
    for r in range(3, 6):
        RESULT[r] = "Careless!"
    result = Counter(s)['/']
    return ['-' * len(s), RESULT.get(result, "Hobo!")]
