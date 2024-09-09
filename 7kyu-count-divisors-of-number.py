# 7 kyu: Count the divisors of a number
# Count the number of divisors of a positive integer n.

# My Solution:
def divisors(n):
    count = 0
    for x in range(1, n+1):
        if n % x == 0:
            count += 1
    return count

# Community Solution
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0])