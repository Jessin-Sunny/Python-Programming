def no(x,y,z):
    if x>y>z:
        print(x," is the largest number")
        print(z," is the smallest number")
    elif x>z>y:
        print(x," is the largest number")
        print(y," is the smallest number")
    elif z>y>x:
        print(z," is the largest number")
        print(x," is the smallest number")
    elif z>x>y:
        print(z," is the largest number")
        print(y," is the smallest number")
    elif y>x>z:
        print(y," is the largest number")
        print(z," is the smallest number")
    elif y>z>x:
        print(y," is the largest number")
        print(x," is the smallest number")
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
no(a,b,c)
