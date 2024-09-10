# 7 kyu: Money, Money, Money
# Mr. Scrooge has a sum of money 'P' that he wants to invest.
# Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

# My Solution:
def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:                          # Continue until the principal meets or exceeds the desired amount
        earned_interest = principal * interest          # Calculate the interest earned
        tax_amount = earned_interest * tax              # Calculate the tax on the interest
        principal += earned_interest - tax_amount       
        years += 1                                      # Increment the year count
    
    return years

# Community Solution
def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years
