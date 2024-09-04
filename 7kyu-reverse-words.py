# 7 kyu: Reverse words
# Complete the function that accepts a string parameter, and reverses each word in the string.

# My Solution:
def reverse_words(text):
    words = text.split(' ')
    reversed = [word[::-1] for word in words]
    return ' '.join(reversed)

# Community Solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))