def min_max(l):
    n = len(l)
    if n == 0:
        print("List is empty")
    else:
        minimum = l[0]
        maximum = l[0]
        for i in range(n):
            if l[i] < minimum:
                minimum = l[i]
            if l[i] > maximum:
                maximum = l[i]
    return minimum,maximum

l = list()
n = int(input("How many numbers ? : "))
print("Enter the numbers")
for i in range(n):
    num = int(input())
    l.append(num)
(minimum,maximum) = min_max(l)
print("Minimum value : ",minimum)
print("Maximum value: ",maximum)
