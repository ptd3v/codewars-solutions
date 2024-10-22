# 7 kyu: Find the middle element
# As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

# My Solution:
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

# Community Solution
def gimme(arr):
    return (len(arr)-(arr.index(max(arr)))) - arr.index(min(arr))

