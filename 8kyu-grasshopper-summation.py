# 8 Kyu: Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num.

# My Solution:
def summation(num):
    count = 0
    for i in range(1, num + 1):
        count += i
    return count

# Community Solution
def summation(num):
    return sum(range(num + 1))
