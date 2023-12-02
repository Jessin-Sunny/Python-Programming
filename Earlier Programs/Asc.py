#Display inputted 3 numbers in ascending order
def asc(x,y,z):
    if x>y>z:
        print("The Numbers in ascending order ")
        print(z," ",y," ",x)
    elif x>z>y:
        print("The Numbers in ascending order ")
        print(y," ",z," ",x)
    elif z>y>x:
        print("The Numbers in ascending order ")
        print(x," ",y," ",z)
    elif z>x>y:
        print("The Numbers in ascending order ")
        print(y," ",x," ",z)
    elif y>x>z:
        print("The Numbers in ascending order ")
        print(z," ",x," ",y)
    elif y>z>x:
        print("The Numbers in ascending order ")
        print(x," ",z," ",y)
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
asc(a,b,c)


