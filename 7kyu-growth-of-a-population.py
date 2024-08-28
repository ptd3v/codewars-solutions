# 7 kyu: Growth of a Population
# In a small town the population is p0 = 1000 at the beginning of a year. 

# My Solution:
def nb_year(p0, percent, aug, p):
    years = 0
    growth_rate = percent / 100
    
    while p0 < p:
        p0 += int(p0 * growth_rate) + aug
        years += 1
    
    return years

# Community Solution
def nb_year(p0, percent, aug, p):
    percent = percent / 100
    i = 0
    while p0 < p:
        p0 += percent * p0 + aug
        i += 1
    return i