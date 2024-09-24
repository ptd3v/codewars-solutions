# 8 kyu: Multiple of index Solution
# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
# Note: This kyu made me mad and was easily the worst problem I've came across in over a year.

# My Solution:
def multiple_of_index(arr):
    result = []
    for i in range(len(arr)):
        j = arr[i]
        if (i == 0 and j == 0) or (i != 0 and j % i == 0):
            result.append(j)
    return result

# Community Solution
def multiple_of_index(arr):
    return [j for i, j in enumerate(arr) if (i == 0 and j == 0) or (i != 0 and j % i == 0)]