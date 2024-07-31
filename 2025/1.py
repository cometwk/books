import math

def solve(n):
    R5 = math.sqrt(5)
    A = ((1+R5)/2)**(n+2)
    B = ((1-R5)/2)**(n+2)
    p = (1 / ((2**n) * R5)) * (A-B)
    return 1 - p

p = solve(4)
print(p)

