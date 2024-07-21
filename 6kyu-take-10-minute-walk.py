# Take a Ten Minutes Walk (6th Kyu)
# When you press a button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e'])

# My Solution:
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
   
    x, y = 0, 0   
    for step in walk:
        if step == 'n':
            y += 1
        elif step == 's':
            y -=1
        elif step == 'e':
            x -= 1
        elif step == 'w':
            x += 1       
    return x == 0 and y == 0

# Community Solution:
return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# Longer Form
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False

