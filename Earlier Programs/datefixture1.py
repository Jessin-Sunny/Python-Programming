dat=input("Enter Starting Date(yyyy-mm-dd) : ")
fin=input("Enter Final Date(yyyy-mm-dd) :")
time=["16:00","18:00"]
exp=[]

while True:
    hol=input("Enter Date to be excepted from the Fixture(yyyy-mm-dd) : ")
    ch=input("Do you want to continue (y/n) ? : ")
    exp.append(hol)
    if ch.lower()== 'n' :
        break
month30=[04,06,09,11]
month31=[01,03,05,07,08,10,12]
if int(dat[0:5]%4)==0:
    feb=29
else:
    feb=28
l=[]
if int(dat[6:8]) in month30:
    for i in range(int(dat[-2:]),31):
        if i not in int(exp[-2:]):
            l.append(i)       
    if len(l)==18:
        break
    else:
        q=int(dat[6:8]+1)
        zj=1
        while True:
            if zj not in int(exp[-2:]):
                l.append(zj)
            if len(l==18):
                break
elif int(dat[6:8]) in month31:
    for i in range(int(dat[-2:]),32):
        if i not in int(exp[-2:]):
            l.append(i)
    if len(l)==18:
        break
    else:
        monthno=int(dat[-2:])+1
        q=int(dat[6:8]+1)
        zj=1
        while True:
            if int()
                l.append(zj)
            if len(l==18):
                break
else:
    for i in range(int(dat[-2:]),feb+1):
        if i not in int(exp[-2:]):
            l.append(i)
    if len(l)==18:
        break
    else:
        q=int(dat[6:8]+1)
        zj=1
        while True:
            if zj not in int(exp[-2:]):
                l.append(zj)
            if len(l==18):
                break
        
    
        
    


