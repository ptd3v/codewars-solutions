# Jaden Case (7th Kyu)
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.

# Solution One
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# Solution Two
def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)

# Solution Three
import string
toJadenCase = string.capwords
