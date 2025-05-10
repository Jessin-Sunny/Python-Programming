#e^x = (1 + x + (x^2/2!) + (x^3/3!) + .... )
from math import factorial
n = int(input("How many terms ? : "))
x = int(input("Enter the value of x: "))
sums = 0
for i in range(0,n):
    y = factorial(i)
    d = x**i
    sums += d/y

print("e^%d:%6.2f" %(x, sums))
