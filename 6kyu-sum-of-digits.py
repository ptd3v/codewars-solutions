# Sum of Digits (6th Kyu)
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.

# My Solution:
def digital_root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n

# Community Solution
def digital_root(n):
	return n % 9 or n and 9