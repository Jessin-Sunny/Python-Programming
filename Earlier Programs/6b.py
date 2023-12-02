N=[12,13,34,56,21,79,98,22,35,38]
S=[]
def PUSH():
    for i in N:
        if i%2==0:
            S.append(i)
def POPDISPLAY():
    while S!=[]:
        print(S.pop(),end=" ")
PUSH()
POPDISPLAY()
    
