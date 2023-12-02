N=[12,13,34,56,21,79,98,22,35,38]
s=[]
def PUSH(e):
    for i in e:
        if i%2==0:
            s.append(i)
def DISPLAY():
    l=len(s)
    for i in range(l-1,-1,-1):
        print(s[i],end=" ")
def POP():
    print("POP",s.pop())
PUSH(N)
DISPLAY()
POP()
    
