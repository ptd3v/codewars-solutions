# Shortest Word (7th Kyu)
# Given a string of words, return the length of the shortest word(s).

# Solution One
def find_short(s):
    return min(len(word) for word in s.split())

# Solution Two
def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length

# Community Solution
def find_short(s):
    return min(map(len, s.split(' ')))

# Random test code
s = ("bitcoin take over the world maybe who knows perhaps")
words = s.split()
print(s)
print(words)
print(words.min())

def find_short(s):
    words = s.split()
    return words.min()
