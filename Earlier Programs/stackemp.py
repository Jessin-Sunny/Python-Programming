c="y"
emp=[]
while (c.lower()=="y"):
    print("1:")
    ch=int(input("E: "))
    if ch==1:
        e_id=input("eID : ")
        e_na=input("ename : ")
        e=(e_id,e_na)
        emp.append(e)
    elif ch==2:
        if emp==[]:
            print("UNDERFLOW")
        else:
            ex,ey=emp.pop()
            print(ex,ey)
    elif ch==3:
        l=len(emp)
        for i in range(l-1,-1,-1):
            print(emp[i][0],emp[i][1])
    elif ch==4:
        break
    else:
        print("WRONG OUTPUT")
        
