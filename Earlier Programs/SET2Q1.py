R={"OM":76,"JAI":45,"BOB":89,"ALI":65,"ANU":90,"TOM":82}
s=[]
def PUSH():
    for i in R:
        if R[i]>75:
            s.append(i)
def POP():
    print("The elemented poped(deleted) is ",s.pop())
def DISPLAY():
    l=len(s)
    for i in range(l-1,-1,-1):
        print(s[i]  ,end=" ")             
PUSH()
DISPLAY()
POP()
