# Beginner Series #3 Sum of Numbers (7th Kyu)
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.

# Key Functions: Range, Sum

# Solution One
def get_sum(a,b):
    if a > b: # Simple but effective
        a, b = b, a
    # +1 because range does NOT include the last number. 0 indexing.
    return sum(range(a,b+1))

# Solution Two
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

# Community Solution
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
