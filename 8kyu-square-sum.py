# 8 Kyu: Square(n) Sum
# Complete the square sum function so that it squares each number passed into it.

# My Solution:
def square_sum(numbers):
    num = []
    for x in numbers:
            num.append(x**2)
    return sum(num)

# Community Solution
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
