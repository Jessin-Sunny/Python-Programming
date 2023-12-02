#string is a palindrome or not;converting the case of characters
def palindrome(x):
    length=len(x)
    mid=length//2
    rev=-1
    for a in range(mid):
        if x[a]==x[rev]:
            rev-=-1
        else:
            print(x," is not palindrome")
            break
    else:
        print(x," is a palindrome")

string=input("Enter the string : ")
new_string=string.upper()
palindrome(new_string)
