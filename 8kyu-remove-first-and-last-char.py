# 8 kyu: Remove First and Last Character
# Your goal is to create a function that removes the first and last characters of a string.

# My Solution:
def remove_char(s):
    return s[1:-1]      # String Slicing

# Community Solution
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]