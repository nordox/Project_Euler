# Program to find the sum of
# all the multiples below a 
# certain number
#

def mult( x ):
    if x%3 == 0 or x%5 == 0:
        return x
    else:
        return 0

x = 0
for i in range(1, 1000):
    x = x + mult( i )

print x
