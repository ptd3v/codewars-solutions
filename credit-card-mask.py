# Credit Card Mask (7th Kyu)
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Solution One
def maskify(cc):
    masked = ''
    for i in range(len(cc)):
        if i < len(cc) - 4: # if NOT the last four digits (if i < 12 - 4.)
            masked += '#' # Masks 0,1,2,3,4,5,6,7,8. Not 9,10,11,12.
        else:
            masked += cc[i] # if the last four digits
    return masked

# Solution Two
def maskify(cc):
    # Hash all numbers except the last 4. Append the last 4 digits of the original.
    return '#' * max(0, len(cc) - 4) + cc[-4:]

# Community Solution
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))
