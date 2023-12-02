#Display the smaller/larger number
def num(x,y):
    if x>y:
        print(x," is the larger number")
        print(y," is the smaller number")
    elif x==y:
        print("Both numbers are same")
    else:
        print(x," is the smaller number")
        print(y," is the largest number")
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
num(a,b)
        
    


