Arr=[1,2,3,4,5,6]
s=[]
def PUSH():
    for i in Arr:
        if i%2!=0:
            x=i*2
            s.append(x)
        else:
            x=i**2
            s.append(x)
def DISPLAY():
    l=len(s)
    if l<1:
        print("STACK EMPTY")
    else:
        for i in range(l-1,-1,-1):
            print(s[i],end=" ")
PUSH()
DISPLAY()
        
    
