#Find HCF of two numbers without recursion
#find multiples
#among them findout largest multiple
#better approach in backward

def getHCF(x, y):
    minimum = min(x,y)
    if (x%minimum == 0) and (y%minimum == 0):
        return minimum
    for i in range(minimum//2,1,-1):
        if(x%i == 0) and (y%i == 0):
            return i

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
print("HCF = ", getHCF(x, y))
