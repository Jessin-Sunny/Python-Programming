import pickle
def Createfile():
    fobj=open("Book.dat","ab")
    Bookno=int(input("Enter Book Number : "))
    Bookname=input("Enter Bookname : ")
    Author=input("Enter Author name : ")
    Price=eval(input("Enter price : "))
    rec=[Bookno,Bookname,Author,Price]
    pickle.dump(rec,fobj)
    fobj.close()
def readfile():
    fobj=open("Book.dat","rb")
    try:
        while True :
            r=pickle.load(fobj)
            print(r)
    except EOFError :
        pass
