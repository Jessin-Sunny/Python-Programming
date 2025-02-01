import math
x = int(input("Enter a number : "))
estimate = 1.0
tolerance = 0.000001

while True:
    estimate = (estimate + x/estimate)/2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break
print("Programmer's estimated value : ",estimate)
print("Square Root : ",math.sqrt(x))
