# 7 kyu: Printer Errors
# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors.

# My Solution:
def printer_error(s):
    errors = 0
    total = len(s)
    for x in s:
        if x > 'm':
            errors += 1
    return str(errors) + '/' + str(total)

# Community Solution
def printer_error(s):
    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))