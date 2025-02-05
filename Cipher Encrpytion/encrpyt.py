text = input("Enter the text to be encrpyted : ")
distance = int(input("Enter the distance : "))
cipher=""
for i in text:
    e = ord(i) + distance
    if e > ord('z'):
        e = ord('a') + e - ord('z') - 1
    cipher+=chr(e)
print(cipher)
