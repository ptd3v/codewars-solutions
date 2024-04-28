# Shortest Word (7th Kyu)
# Given a string of words, return the length of the shortest word(s).

# Solution One
s = ("bitcoin take over the world maybe who knows perhaps")
words = s.split()
print(s)
print(words)
print(words.min())

def find_short(s):
    words = s.split()
    return words.min()
    
    #return l # l: shortest word length

# Solution Two


# Community Solution