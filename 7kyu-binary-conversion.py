# 7 Kyu: Binary Addition
# Implement a function that adds two numbers together and returns their sum in binary. 

# My Solution:
def add_binary(a,b):
    return(format(a + b, 'b'))  # 'b' and format, makes it a binary string.

# Community Solution
def add_binary(a,b):
    return bin(a + b)[2::]      # Bin() adds 0b, [2::]  ignores them.