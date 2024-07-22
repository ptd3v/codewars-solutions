# Replace With Alphabet Position (6th Kyu)
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# My Solution
def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            # ord('a') is 97, so we subtract 96 to get 'a' = 1, 'b' = 2, etc.
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)

# Community Solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# Humerous solution:
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos_map = {letter: str(index) for index, letter in enumerate(alphabet, start=1)}

    inds = []
    for x in text.lower():
        if x in alphabet:
            inds.append(alphabet[x])
    return ' '.join(([str(x) for x in inds]))
