# 8 kyu: Find the first non-consecutive number
# If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not.

# My Solution:
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] +1:
            return arr[i]
    return None

# Community Solution
def first_non_consecutive(a):
    for i, x in enumerate(a, a[0]):
        if i != x:
            return x
