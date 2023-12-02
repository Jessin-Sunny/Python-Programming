def w():
    f=open("ttyy.txt","w")
    f.write("Hi\n")
    f.write("Me\n")
    f.close()
def r():
    f=open("ttyy.txt","r")
    q=f.read()
    w=f.tell()
    l=len(q)
    print(q)
    print(l)
    print(w)
w()
r()
    
