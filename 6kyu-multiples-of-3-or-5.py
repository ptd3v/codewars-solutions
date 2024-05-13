# Multiples of 3 or 5 (6th Kyu)
# Return the sum of all the multiples of 3 or 5 below the number passed in.

# Key Functions: for(), if(), range, +=.

# Solution One
def solution(number):
    sum = 0
    for i in range(0, number):
        if i %3 == 0 or i %5 == 0:
            sum += i
    return sum

# Community Solution
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

