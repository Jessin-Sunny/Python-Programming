def gcd(x,y):
    gcd=1
    if x % y==0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd=k
            break
    print("Greatest common divisor : ",gcd)
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter the first integer : "))
num2=int(input("Enter the second integer : "))
gcd(num1,num2)
print("The least common multiple : ",lcm(num1,num2))
