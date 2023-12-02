R={"OM":76,"JAI":45,"BOB":89,"ALI":65,"ANU":90,"TOM":82}
S=[]
C="Y"
def PUSH():
    for i in R:
            if R[i]>75:
                S.append(i)
    print("PUSH OPERATION SUCCESSFULL")
def POPDISPLAY():
    while S!=[]:
            print(S.pop(),end=" ")
while (C=="Y"):
    print("1:PUSH")
    print("2:POP AND DISPLAY")
    print("3:EXIT")
    ch=int(input("Enter your choice : "))
    if ch==1:
        PUSH()
    elif ch==2:
        POPDISPLAY()
    elif ch==3:
        break
    else:
        print("WRONG OUTPUT")
