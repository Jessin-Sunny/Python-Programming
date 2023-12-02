#Display sum of digits and reverse of an integer number
def sum(x):
    s=0
    for i in str(x):
        s+=int(i)
    print("The sum of digits : ",s)
    
def reverse(y):
    rev=0
    while(y>0):
        a=y%10
        rev=rev*10+a
        y=y//10
    print("The reverse of number : ",rev)
a=int(input("Enter a number(integer) : "))
sum(a)
reverse(a)
