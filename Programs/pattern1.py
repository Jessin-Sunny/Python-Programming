"""
Pattern
A
A B
A B C
A B C D

"""
rows = int(input("How many rows (max 26) ? : "))
start = ord('A')
for i in range(1,rows + 1):
    for j in range(0,i): 
        print(chr(start + j),end=" ");
    print()
