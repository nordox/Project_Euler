# Program to find the prime
# factors of a number
#

a = []
i = 2
n = 600851475143
while i <= n:
    if n%i == 0:
        a.append(i)
        n = n/i
    i = i + 1

print a
