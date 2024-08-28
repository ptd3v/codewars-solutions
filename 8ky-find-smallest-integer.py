# 8 kyu: Find the smallest integer in the array
# Given an array of integers your solution should find the smallest integer.

# My Solution:
def find_smallest_int(arr):
    smallest = arr[0]
    for x in arr[1:]:
        if x < smallest:
            smallest = x
    return smallest

# Community Solution
def findSmallestInt(arr):
    return min(arr)

def findSmallestInt(arr):
    arr.sort()
    return arr[0]