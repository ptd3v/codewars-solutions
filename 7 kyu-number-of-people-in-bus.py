# 7 kyu: Number of People in the Bus
# There is a bus moving in the city which takes and drops some people at each bus stop.

# My Solution:
def number(bus_stops):
    total = 0
    for on, off in bus_stops:
        total += on - off
    return total

# List Comprehension
def number(bus_stops):
    return sum(on - off for on,off in bus_stops)

# Community Solution
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
