# Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.

# My Solution:
def positive_sum(arr):
    new = []
    for x in arr:
        if x > 0:
            new.append(x)
    return sum(new)

# Community Solution
def positive_sum(arr):
    return sum(x for x in arr if x > 0)