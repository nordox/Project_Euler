# Program to find the largest palindrome makde
# from the product of two 3-digit numbers
#

x = 999
y = 999
largest = 0

while x > 100:
    # Check if palindrome
    if x*y == int(str(x*y)[::-1]) and x*y > largest:
        largest = x*y
    if y > 100:
        y = y - 1
    else:
        y = 999
        x = x - 1

print x
print y
print [largest]
