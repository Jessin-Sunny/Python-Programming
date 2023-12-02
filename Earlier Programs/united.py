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
    print(x)
    #stadium(x)      
teams()

##def matches():
##    m=['Germany VS France','Italy vs Poland','Austria VS Germany','England VS Italy']
##    for i in range(len(m)):
##        print(i)
##        """
##        for j in len(i):
##            if 'Germany' in j:
##                print(i)
##"""
###matches()
import random




grpA=["a","b","c","d" ]
grpB=["e","f","g","h"]
grpC=["i","j","k","l"]
grpD=["m","n","o","p"]
list1=[grpA,grpB,grpC,grpD]
list2 = []
dict1={}

for i in list1:
    for j in i:
        k=i.index(j)
        for S in range(4):
            if S!=k and ( not ( ((j,i[S]) in list2) or ((i[S],j) in list2 )) ) :
                list2.append((j,i[S]))
print(len(list2))
print(list2)

initialDate= 10
month="June"
listDate=[]
for i in range ( initialDate,initialDate+9) :
    listDate.append(i)

    


##for i in range ( 0,len(list),6) :
##    list3.append(list2[i:i+6])
##ini=0
##final=2
##
##for i in range (16) :
##    dict1[list2[ini][0]]=list2[ini:final+1]
##    ini=ini+3
##    final=final+3
##            
##print(list2)
##print("_"*34)
##print(dict1)
##
initialDate= 10
month="June"
listDate=[]
for i in range ( initialDate,initialDate+9) :
    listDate.append(i)
    
list2=[('Netherlands', 'Germany'), ('Netherlands', 'Belgium'), ('Netherlands', 'Czech Republic'), ('Germany', 'Belgium'), ('Germany', 'Czech Republic'), ('Belgium', 'Czech Republic'), ('Hungary', 'Scotland'), ('Hungary', 'Austria'), ('Hungary', 'Sweden'), ('Scotland', 'Austria'), ('Scotland', 'Sweden'), ('Austria', 'Sweden'), ('France', 'Slovakia'), ('France', 'Denmark'), ('France', 'Portugal'), ('Slovakia', 'Denmark'), ('Slovakia', 'Portugal'), ('Denmark', 'Portugal'), ('Wales', 'Finland'), ('Wales', 'Poland'), ('Wales', 'Spain'), ('Finland', 'Poland'), ('Finland', 'Spain'), ('Poland', 'Spain'), ('North Macedonia', 'Turkey'), ('North Macedonia', 'Russia'), ('North Macedonia', 'Ukraine'), ('Turkey', 'Russia'), ('Turkey', 'Ukraine'), ('Russia', 'Ukraine'), ('Italy', 'Croatia'), ('Italy', 'England'), ('Italy', 'Switzerland'), ('Croatia', 'England'), ('Croatia', 'Switzerland'), ('England', 'Switzerland')]
