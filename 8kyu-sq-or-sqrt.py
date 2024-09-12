# 8 kyu: To square(root) or not to square(root)
# Write a method, that will get an integer array as parameter and will process every number from this array.

# My Solution:
def square_or_square_root(arr):
    result = []
    for x in arr:
        root = int(x ** 0.5)
        if root * root == x:
            result.append(root)
        else:
            result.append(x**2)
    return result

# Community Solution
def square_or_square_root(arr):
    pass
