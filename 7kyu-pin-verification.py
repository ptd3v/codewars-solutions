# 7 kyu: PIN Verification
# Verify that the PIN codes provided are either 4 or 6 characters and contain now symbols.

# My Solution:
def validate_pin(pin):
    for x in pin:
        if x < '0' or x > '9':  # This checks if each character is a digit
            return False
    if len(pin) == 4 or len(pin) == 6:  # Checks the length of the pin
        return True
    return False  # Necessary to return False if the pin is not of length 4 or 6


# Community Solution
def validate_pin(pin):
    # Check if all characters in pin are digits
    if not pin.isdigit():
        return False
    
    # Check if length is either 4 or 6
    if len(pin) == 4 or len(pin) == 6:
        return True
    
    return False