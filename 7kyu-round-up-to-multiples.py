# 7 kyu: Round up to the next multiple of 5
# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

# My Solution:
def round_to_next5(n):
    return ((n + 4) // 5) * 5

# Community Solution:
def round_to_next5(n):
    return n + (5 - n) % 5