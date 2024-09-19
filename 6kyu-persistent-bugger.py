# Persistent Bugger (6th Kyu)
# Take in a positive parameter num and return its multiplicative persistence.

# My Solution
def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count

# Community Solution
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
