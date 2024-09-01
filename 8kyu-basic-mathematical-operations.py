# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.

# My Solution:
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        print ("Unrecognized Operator. Abort.")

# Community Solution
def basic_op(operator, value1, value2):
    return eval(f'{value1} {operator} {value2}')
