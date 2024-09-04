# 8 kyu: Count of positives / sum of negatives
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# My Solution:
def count_positives_sum_negatives(arr):
    if not arr:  # Check if the array is empty or None
        return []
    positive = 0
    negative = 0
    for x in arr:
        if x > 0:
            x += positive
        if x > 0:
            positive += 1  # Count the positive numbers
        elif x < 0:
            negative += x  # Sum the negative numbers
    return [positive, negative]

# Community Solution
def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output
