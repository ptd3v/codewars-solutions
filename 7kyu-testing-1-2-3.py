# 7Kyu: Testing 1-2-3
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# My Solution:
def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, start=1)]

# Community Solution
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]