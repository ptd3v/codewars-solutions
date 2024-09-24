# 7 kyu: Two Oldest Ages
# It should take an array of numbers as its argument and return the two highest numbers within the array.

# My Solution:
def two_oldest_ages(ages):
    sort = sorted(ages)
    return [sort[-2],sort[-1]]

# Community Solution
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

print (chr(sum(range(ord(min(str(not())))))))