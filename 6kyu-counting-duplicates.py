# 6 kyu Counting Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 

# My Solution:
def duplicate_count(text):
    result = []
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            result.append(text)
    return len(result)

# Community Solution
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c)>1])