# 8 kyu: Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.

# My Solution [List Solution]:
def fake_bin(x):
    b = []
    for n in x:
        if int(n) >= 5:
            b.append ('1')
        if int(n) < 5:
            b.append ('0')
    return ''.join(b)

# String Solution
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

# Community Solution
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)