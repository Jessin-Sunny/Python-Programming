def teams():
    print("welcome!!!")
    print("which team's match do you want to watch ? :")
    teams=["Germany","Turkey","Poland","North Macedonia","Portugal","Switzerland","Finland","Netherlands",
           "Slovakia","Croatia","Belgium","France","Spain","England","Austria","Czech Republic","Sweden","Hungary",
           "Scotland","Denmark","Italy","Russia","Ukraine","Wales"]
    for i in range(24):
        print(i+1,teams[i])
    p= int(input("choose your option: "))
    x=teams[p]
    #stadium(x)      
teams()

def matches():
    m=['Germany VS France','Italy vs Poland','Austria VS Germany','England VS Italy']
    for i in range(len(m)):
        #print(m[i])
        if 'Germany' in m[i]:
            print(m[i])
        
matches()

    
