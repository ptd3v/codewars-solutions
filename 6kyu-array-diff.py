# Array.diff (6th Kyu)
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# My Solution:
def array_diff(a, b):
    ends = []
    for x in a:
        if x not in b:
            ends.append(x)
    return ends

# Community Solution:
def array_diff(a, b):
    return [x for x in a if x not in b]

