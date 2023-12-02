#Displaying prime numbers in a range
def primeno(x,y):
    j=0
    for i in range(x,y+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)

l1=int(input("Enter the starting range : "))
l2=int(input("Enter the ending range : "))
print("The prime numbers between ",l1," and ",l2," are : ")
primeno(l1,l2)
