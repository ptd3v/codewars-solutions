# 7 kyu: Odd or Even?
# Given a list of integers, determine whether the sum of its elements is odd or even.

# My Solution:
def odd_or_even(arr):
    x = sum(arr)
    if x % 2 == 0:
        return "even"
    return "odd"

# Community Solution
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
