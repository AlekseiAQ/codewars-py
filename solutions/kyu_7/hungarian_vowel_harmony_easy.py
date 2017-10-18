"""Hungarian Vowel Harmony (easy)"""


def dative(word):
    for letter in word[::-1]:
        if letter in "eéiíöőüű":
            return word + "nek"
        elif letter in "aáoóuú":
            return word + "nak"
