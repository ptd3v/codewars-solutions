# 8 kyu: Multiplication table for number
# Your goal is to return multiplication table for number that is always an integer from 1 to 10.

# My Solution:
def multi_table(number):
    result = ''
    for x in range(1, 11):
        result += f'{x} * {number} = {x * number}\n'
    return result.rstrip()

# Community Solution
def multi_table(number):
    return '\n'.join(f'{x} * {number} = {x * number}' for x in range(1, 11))
