#Fibonacci series
def fibseries(x):
    first=0
    second=1
    print(first,end=",")
    print(second,end=",")
    for i in range(1,x-1):
        third=first+second
        print(third,end=",")
        first,second=second,third
N=int(input("Enter the number of elements : "))
fibseries(N)
