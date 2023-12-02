#Display the sum of series
def series1(x,n):
    sum1=0
    for i in range(n+1):
        sum1+=x**i
    print("series1[1+x+x^2+x^3+x^4+......x^n] : ",sum1)
def series2(x,n):
    sum2=0
    sum2_1=0
    sum2_2=0
    for i in range(n+1):
        if i%2==0:
            sum2_1+=x**i
        else:
            sum2_2-=x**i
    sum2=sum2_1+sum2_2
    print("series2[1-x+x^2-x^3+x^4+........x^n] : ",sum2)
def series3(x,n):
    sum3=0
    sum3_1=0
    sum3_2=0
    for i in range(1,n+1):
        if i%2==0 and i%2==1:
            sum3_1+=x**i/i
        """
        else:
            sum3_2-=x**i/i
        """
    sum3=sum3_1+sum3_2
    print("series3[x+x^2/2!-x^3/3!+x^4/4!+...x^n/n!] : ",sum3)
def fact(n):
    i=n
    fact=1
    while(i>=1):
        fact=fact*i
        i=i-1
    return fact
def series4(x,n):
    sum=x
    for i in range(2,n+1):
        sum=sum+((-1)**i)*((x**i)/fact(i))
    print("Series4 : ",sum)
x=int(input("Enter the values of x : "))
n=int(input("Enter the value of n : "))
series1(x,n)
series2(x,n)
series3(x,n)
series4(x,n)
