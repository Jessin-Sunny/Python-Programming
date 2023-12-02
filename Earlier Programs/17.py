#swapping elements at even postion with elements at odd position and vice versa
def swap(x):
    s=len(x)
    if s%2!=0:
        s=s-1
    for i in range(0,s,2):
        l[i],l[i+1]=l[i+1],l[i]
    print("List after swapping : ",l)        

l=eval(input("Enter the list : "))
print("List before swapping : ",l)
swap(l)
