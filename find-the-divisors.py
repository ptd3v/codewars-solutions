# 7 kyu: Find the divisors!
# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.

# My Solution:
def divisors(n):
    if n <= 1:
        return "Number must be greater than 1"
    
    notprime = []
    for x in range(2, n):
        if n % x == 0:
            notprime.append(x)
            
    if not notprime:
        return str(n) + " is prime"
    
    return notprime

# Community Solution
def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)
