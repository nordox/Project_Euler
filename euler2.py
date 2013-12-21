# Program to find the sum of the
# even Fibonacci terms below 4 mil
#

prev = 1
cur = 1
temp = 0
summer = 0

# Ensure the sequence term does not exceed 4mil
while cur <= 4000000:
    # Set current and previos terms
    temp = cur
    cur = cur + prev
    prev = temp
    # Check if term is even - add to sum if it is
    if cur%2 == 0:
        summer = summer + cur

print summer
