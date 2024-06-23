# Duplicate Encoder (6th Kyu)
# Each character in the new string is "(" if that character appears only once in the original string, or ")" for more.

# My Solution:
def duplicate_encode(word):
    word = word.lower()
    result=""
    for x in word:
        if word.count(x) >1:
            result += ")"
        else:
            result += "("
    return result

# Community Solution:
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
