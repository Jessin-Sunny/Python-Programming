"""
Pattern
1
12
123
1234
"""
rows = int(input("How many rows (max 9) ? : "))
start = 1
for i in range(1,rows + 1):
    for j in range(0,i): 
        print(start + j,end=" ");
    print()
