num = input("Enter a number : ")
sums = 0
order = len(num)
num = int(num)
tnum = num
while(tnum > 0):
    digit = tnum %10
    sums = sums + digit**(order)
    tnum = tnum // 10
if(num == sums):
    print(num," is an Armstrong Number")
else:
    print(num," is not an Armstrong Number")
