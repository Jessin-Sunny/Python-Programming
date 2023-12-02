def push():
    c="y"
    while c.lower()=='y':
        a=input("Enter any number : ")
        s.append(a)
        c=input("Do you want to add more numbers ?(y/n): ")        
def pop():
    if s==[]:
        print("UNDERFLOW")
        print("Stack is empty")
    else:
        print("Deleted element is : ",s.pop())
def display():
    l=len(s)
    for i in range(l-1,-1,-1):
        print(s[i])
s=[]
c="y"
while (c.lower()=="y"):
    print("1 : POP")
    print("2 : PUSH")
    print("3 : DISPLAY")
    ch=int(input("Enter your choice : "))
    if ch==1:
        pop()
    elif ch==2:
        push()
    elif ch==3:
        display()
    else:
        print("Invalid Choice!!!")
    c=input("Do you want to continue or not ?(y/n): ")
    
    
