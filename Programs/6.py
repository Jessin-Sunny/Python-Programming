#(a+b)^2 = a^2 + 2ab + b^2

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

c = (a + b)**2
d = a**2 + 2*a*b + b**2
print("LHS = ", c)
print("RHS = ", d)
if c == d:
    print("Equation holds TRUE")
else:
    print("Equation holds FALSE")
