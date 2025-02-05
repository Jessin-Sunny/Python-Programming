"""
Count the number of odd even numbers in a list
"""
n = int(input("How many numbers ? : "))
l = list()
odd_count = 0
even_count = 0
print("Enter the numbers : ",end="")
for i in range(0,n):
    l.append(int(input()))
    if(l[i] % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
print("Count of even numbers",even_count)
print("Count of odd numbers",odd_count)
