#sum of odd numbers b/w upper limits and lower limits
ll = int(input("Enter the lower limit: "))
ul = int(input("Enter the upper limit: "))
sums = 0
for i in range(ll,ul+1,1):
    if i%2 != 0:
        sums += i
print("Sum: ",sums)
