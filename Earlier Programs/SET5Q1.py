def AddCustomer(Customer):
    for i in Customer:
        CStack.append(i)
def Display():
    l=len(CStack)
    for i in range(l-1,-1,-1):
        print(CStack[i])
def DeleteCustomer():
    print("DELETED : ",CStack.pop())
CStack=[]
def firstadd():
    Customer=[]
    while True:
        print("1:ENTER")
        print("2:EXIT")
        ch=int(input("Choice : "))
        if ch==1:
            c=input("Enter Customer : ")
            Customer.append(c)
        else:
            break
    AddCustomer(Customer)
firstadd()
        

Display()
DeleteCustomer()
