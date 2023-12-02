def armstrong(x):
    for n in x:
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
        
def length(y):
    print("Largest Number : ",max(y))
    print("The smallest number : ",min(y))

l=eval(input("Enter the list : "))
armstrong(l)
length(l)
