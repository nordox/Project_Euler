# Program to find the smallest positive number
# that is evenly divisible by all the numbers
# from 1 to 20
#

## Old way of doing it (working)
## Takes a long time

# def divider( x ):
#     i = 1
#     while i < 20:
#         if x%i == 0:
#             i = i + 1
#         else:
#             i = 1
#             x = x + 1
#     return x
# 
# print divider(2520)
# 2 2 2 3 5 2 3 7 2 2 2 3 3 2 5 11 2 2 3 13 2 7 3 5 2 2 2 2 17 2 3 3 19 2 2 5

## New way of doing it (optimized)

# Primality test
def isprime(x):
    for i in range(2, x/2+1):
        if x%i == 0:
            return 1

    return 0

# Function to find the smallest positive number evenly
# divisible by all numbers (1, 20)
def divider(begin, end):
    x = 1
    val = 1
    # Iterate through base in range [begin, end]
    for i in range (begin, end+1):
        # Iterate through exponents [begin, end]
        for x in range(begin, end+1):
            # Check if (base^exponent) is in range [begin, end]
            # and make sure the base is prime
            if i**x >= end and isprime(i) == 0:
                # Multiply (base^exponent) to the main value
                val = val * (i**(x-1))
                break
    return val

print divider(1, 20)
