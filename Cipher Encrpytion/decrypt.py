cipher = input("Enter the text to be encrpyted : ")
distance = int(input("Enter the distance : "))
text=""
for i in cipher:
    e = ord(i) - distance
    if e < ord('a'):
        e = ord('z') + e - ord('a') + 1
    text+=chr(e)
print(text)
