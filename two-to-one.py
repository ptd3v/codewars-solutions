# Two to One (7th Kyu)
# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Functions Required: "".join, Sorted(), Set(), 

# Solution One
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

# Solution Two
def longest(s1, s2):
    distinct = set(s1+s2) # sets are distinct values! 
    distinctSorted = sorted(distinct) # turn into sorted list
    return ''.join(distinctSorted) # concatenate to string with 'join'
