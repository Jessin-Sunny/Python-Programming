def list1():
    list=[]
    new_list=[]
    element=int(input("Enter the elements in the list : "))
    for i in range(element):
        num=int(input("Enter the number : "))
        list.append(num)
    for j in range(element):
        s=0
        a=list[j]
        length=len(str(list[i]))
        while a>0:
            d=a%10
            k=d**length
            s=s+k
            a=a//10
        if list[j]==s:
            new_list.append(list[j])
        print("The largest number : ",max(new_list))
        print("The smallest number : ",min(new_list))
list1()
