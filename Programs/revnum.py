num = int(input("Enter a number : "))
tnum = num
rev = 0
while(tnum > 0):
    digit = tnum % 10
    rev = rev * 10 + digit
    tnum = tnum//10
if(num == rev):
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")
