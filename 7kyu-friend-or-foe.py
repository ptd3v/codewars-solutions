# 7 kyu: Friend or Foe?
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# My Solution:
def friend(x):
    new = []
    for name in x:
        if len(name) == 4:
            new.append(name)
    return new

# Community Solution
def friend(x):
    return [name for name in x if len(name) == 4]

