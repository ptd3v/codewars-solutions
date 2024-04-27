# Exes and Ohs (7th Kyu)
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.

# Solution One
def xo(s):
    s_lower = s.lower()
    countx = 0
    counto = 0
    for char in s_lower:
        if char == 'x':
            countx += 1
        elif char == 'o':
            counto += 1
    return countx == counto # Returns boolean value without if/else

# Solution Two
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# Community Solution
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
