# Find The Parity Outlier (6th Kyu)
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

# My Solution:
def find_outlier(integers):
    odd = [x for x in integers if x %2 != 0]
    even = [x for x in integers if x %2 == 0]
    return odd[0] if len(odd) == 1 else even[0]

# Community Solution:
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]