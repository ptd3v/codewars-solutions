# 7 kyu: Find the capitals
# Return an ordered list containing the indices of all capital (uppercase) letters in the string.

# My Solution:
def capitals(word):
    result = []
    for i, x in enumerate(word):
        if x.isupper():
            result.append(i)
    return result

# Community Solution
def capitals(word):
    return [i for i, x in enumerate(word) if x.isupper()]