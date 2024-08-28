# 7 kyu: Categorize New Member
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.

# My Solution:
def open_or_senior(data):
    results=[]
    for x,y in data:
        if x >= 55 and y > 7:
            results.append("Senior")
        else:
            results.append("Open")
    return results

# Community Solution
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

