# 8Kyu: Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# My Solution:
def make_negative( number ):
    if number > 0:
        return - + number
    return number

# Community Solution
def make_negative( number ):
    return -abs(number)

