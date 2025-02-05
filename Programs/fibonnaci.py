n = int(input("How many terms ? : "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(c)    
