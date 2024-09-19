# 8 kyu: Triple Trouble
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups.

# My Solution:
def triple_trouble(one, two, three):
    result = ''
    for i in range(len(one)):
        result += one[i] + two[i] + three[i]
    return result

# Community Solution
def triple_trouble(one, two, three):
    ans = ''
    for i in range(len(one)):
        ans+=one[i]
        ans+=two[i]
        ans+=three[i]
    return ans