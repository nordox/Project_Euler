# Program to find the difference between the sum
# of the squares of the first 100 natural numbers
# and the square of the sum
#

def sumsquare(begin, end):
    sum = 0
    square = 0
    for i in range(begin, end+1):
        sum = sum  + i**2
        square = square + i

    square = square**2
    return square - sum

print sumsquare(1, 100)
