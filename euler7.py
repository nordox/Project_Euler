# Program to find the nth prime number
#

# Original way
# Not optimized
# def isprime(x):
#     for i in range(2, x/2+1):
#         if x%i == 0:
#             return 1
#     return 0
# 
# count = 1
# i = 3
# while i <= 1000000:
#     if isprime(i) == 0:
#         count = count + 1
#         if count == 10001:
#             print i
#             break
#     i = i + 2

# New way
# Optimized
def sieve(x):
    # Create an array of booleans initialized to "True"
    # Create an empty array to store the primes
    a = [True]*x
    val = []
    # Iterate from 2 to the upper bound
    # We start at 2 as that is the smallest prime number
    for i in range(2, x):
        # Array value will be true if it is prime
        # Append the prime to the array
        if a[i] == True:
            val.append(i)
            # Set all multiples of the prime number to False
            for j in range(2*i, x, i):
                a[j] = False
    return val

x = sieve(200000)
# Print (n-1) to find nth prime number
print x[10000]
