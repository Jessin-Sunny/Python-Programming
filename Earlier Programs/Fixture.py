def fixture(l):
    import random
    c=list.copy(l)
    n=[0,1,2,3]
    try:
        while True:
            x=random.choice(n)
            n.remove(x)
            y=random.choice(n)
            if y==x:
                continue
##            for i in c:
            print("Match1 : ",c[x] ,"vs", c[y])
    except:
        pass

def group():
    import random
    teams=["Germany","Turkey","Poland","North Macedonia","Portugal","Switzerland","Finland","Netherlands",
           "Slovakia","Croatia","Belgium","France","Spain","England","Austria","Czech Republic","Sweden","Hungary",
           "Scotland","Denmark","Italy","Russia","Ukraine","Wales"]
    grpA=[]
    grpB=[]
    grpC=[]
    grpD=[]
    grpE=[]
    grpF=[]
    g=[grpA,grpB,grpC,grpD,grpE,grpF]
    l=list.copy(teams)
    try:
        while True:
            x=random.choice(l)
            y=random.choice(g)
            if len(y)<4:
                y.append(x)
                l.remove(x)
    except:
        pass
    #print(grpA)print(grpB)print(grpC)print(grpD)print(grpE)print(grpF)
    list1=[grpA,grpB,grpC,grpD,grpE,grpF]
    list2 = []
    dict1={}

    for i in list1:
        for j in i:
            k=i.index(j)
            for S in range(4):
                if S!=k and ( not ( ((j,i[S]) in list2) or ((i[S],j) in list2 )) ) :
                    list2.append((j,i[S]))
    print(list2)
    print(len(list2))
"""
    ini=0
    final=2

    for i in range (16) :
        dict1[list2[ini][0]]=list2[ini:final+1]
        ini=ini+3
        final=final+3
   """             
"""
    w=[]
    x=1
    for i in range(len(list2)):
            if 'Germany' in list2[i]:
                print(x,list2[i][0], "VS",list2[i][1])
                w.append((list2[i][0], "VS",list2[i][1]))
                x=x+1
##    x=1
##    for i in w:
##        print(x,i)
##        x=x+1
##    ch=int(input("Choose Option : "))
##    if ch==1:
"""
group()
   


    
    
    
    
