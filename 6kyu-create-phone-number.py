# Create Phone Number (6th Kyu)
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Functions Required: String Formatting (f string).List Indexing/Slicing.

# Solution One
return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# Alternative:
num_str = ''.join(map(str, n))                              # Convert the list of numbers to a single string
return f"({num_str[:3]}) {num_str[3:6]}-{num_str[6:]}"      # Format the string to match the phone number format

# Community Solution:
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
