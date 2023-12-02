#Number is a prime no or not
def prime(x):
    value=False
    if x>1:
        for i in range(2,x):
            if x%i==0:
                value=True
                break
    if value:
        print(x," is not a prime number")
    else:
        print(x," is a prime number")
n=int(input("Enter a number : "))
prime(n)
        
