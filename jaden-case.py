# Jaden Case (7th Kyu)
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.

# Solution One

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())