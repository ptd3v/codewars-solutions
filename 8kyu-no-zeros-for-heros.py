# 8 kyu:No zeros for heros
# Numbers ending with zeros are boring. Get rid of them. Only the ending ones.

# My Solution:
def no_boring_zeros(n):
    return int(str(n).rstrip('0')) if n != 0 else 0

# Community Solution