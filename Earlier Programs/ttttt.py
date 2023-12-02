def create():
    f=open("hello.txt","w")
    f.write("Hello Python\n")
    f.write("Me\n")
    f.write("Hi\n")
def view():
    f=open("hello.txt","r")
    r=f.read()
    print(r)
    print(len(r))
create()
view()
