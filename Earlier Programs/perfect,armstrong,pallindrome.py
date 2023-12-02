def perfect(n):
    s1=0
    for i in range(1,n):
        if (n%i==0):
            s1+=i
    if (s1==n):
        print(n," is a perfect number")
    else:
        print(n," is not a perfect number")
        
def armstrong(n):
    s=0
    a=n
    while(n>0):
        d=n%10
        s+=d**3
        n=n//10
    if a==s:
        print(a," is a Armstrong number")
    else:
        print(a," is not Armstrong number")
        
def pallindrome(n):
    a=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if(a==r):
       print(a," is pallindrome")
    else:
        print(a," not pallindrome")
        
n=int(input("Enter the number : "))
perfect(n)
armstrong(n)
pallindrome(n)

