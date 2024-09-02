# 8 kyu: Abbreviate a Two Word Name
# Write a function to convert a name into initials. 

# My Solution:
def abbrev_name(name):
    x, y = name.split()
    for x in name:
        return x[0].upper() + '.' + y[0].upper()
    
# List Comprehension (Optimal):
def abbrev_name(name):
    return '.'.join([x[0].upper() for x in name.split()])