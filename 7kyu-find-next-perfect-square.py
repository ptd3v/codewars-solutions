# 7 kyu: Find the next perfect square!
# You might know some pretty large perfect squares. But what about the NEXT one?

# My Solution:
def find_next_square(sq):
    sqrt = sq ** 0.5
    
    # Return the next square if sq is a square, -1 otherwise
    if sqrt == int(sqrt):
        nxt = (sqrt + 1) ** 2
        return int(nxt) 
    return -1

# Community Solution
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
