"""
input : (x1, y1) & (x2, y2)
output : distance b/w these points
"""
import math
x1 = int(input("Enter the value of x1 : "))
y1 = int(input("Enter the value of y1 : "))
x2 = int(input("Enter the value of x2 : "))
y2 = int(input("Enter the value of y2 : "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance : ",d)
