# Lowest Positive Integers (7th Kyu)
# Create a function that returns the sum of the two lowest positive numbers.

# Solution One
def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    return sort[0] + sort[1]

# Solution Two
def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    return sum(sort[:2])

# Solution Three