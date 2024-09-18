# 8 kyu: Add Length
# What if we need the length of the words separated by a space to be added at the end of that same word.

# My Solution:
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]

# Community Solution
def add_length(str_):
	return [i+' '+str(len(i)) for i in str_.split()]