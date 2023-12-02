#Displaying armstrong numbers in a range
def armsrange(x,y):
    for num in range(l1,l2+1):
        sum=0
        temp=num
        while temp>0:
            digit=temp%10
            sum+=digit**3
            temp=temp//10
            if num==sum:
                print(sum)           
l1=int(input("Enter the starting range : "))
l2=int(input("Enter the ending range : "))
armsrange(l1,l2)
