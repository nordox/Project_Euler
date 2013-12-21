# Program to find the pythagorian triplet such that a^2 + b^2 = c^2
# and a*b*c = 1000

def pythag(upper_bound):
    # Go through all values of a from 1 to the upper bound
    for a in range(1, upper_bound):
        b = 1000
        # Check all values of b such that b > a
        # Solve the formula for c and and multiply
        # all values together to recieve ans
        while b > a:
            if a**2 + b**2 == (1000-a-b)**2:
                print a*b*(1000-a-b)
            b = b - 1

pythag(1000)
