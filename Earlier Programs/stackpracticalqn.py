#Books=[(BookNumber,name of the book,cost of the book)]
Books=[]
def PUSH(Books,N):
    for i  in range(N):
        bno=int(input("Enter the Book NO : "))
        bname=input("Enter the Book name : ")
        cost=int(input("Enter the Cost : "))      
        Books.append((bno,bname,cost))
        print("\nSUCCESSFULLY ADDED\n")
def Display():
    l=len(Books)
    if l<1:
        print("No elements are there in stack")
    else:
        for i in Books:
            print(i[0],i[1],i[2])
while True:
    print("1:PUSH")
    print("2:DISPLAY")
    print("3:EXIT")
    ch=int(input("Enter your choice : "))
    if ch==1:
        N=int(input("Enter the number of books to be added : "))
        PUSH(Books,N)
    elif ch==2:
        Display()
    elif ch==3:
        break
    else:
        print("invalid choice")
        
        
    
    
