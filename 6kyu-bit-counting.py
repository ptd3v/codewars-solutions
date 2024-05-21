# Bit Counting (6th Kyu)
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

# My Solution:
def count_bits(n):
    return bin(n).count('1')

# Community Solution
def count_bits(n):
    return n.bit_count()

# Note: This problem is a little simple with Python compared to C.