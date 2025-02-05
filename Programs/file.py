f = open("first.txt","w")
f.write("hello\nThank You\n")
f.close()

f = open("first.txt","r")
str1 = f.read()
f.close()
print(str1)
