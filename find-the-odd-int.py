# Find the odd int (6th Kyu)
# Given an array of integers, find the one that appears an odd number of times.

# Key Functions: 

# Solution One
def find_it(seq):
    for i in seq:
        x = seq.count(i)
        if x % 2 == 0:
            continue
        return i

# Community Solution
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

