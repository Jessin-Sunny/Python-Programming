def search(x):
    length=len(x)
    for i in range(length):
        if item==x[i]:
            print(item,"Found at index ",i)
            break
    else:
        print(item," not found")
print("Use '[]' for list and '()' for tuple")
lt=eval(input("Enter the list/tuple : "))
item=eval(input("Enter the item to be searched : "))
search(lt)


