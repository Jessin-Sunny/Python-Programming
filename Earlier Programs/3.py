def vowcons(x):
    vow=0
    cons=0
    for i in x.lower():
        if i in 'aeiou':
            vow+=1
        else:
            cons+=1
    print("The number of vowels : ",vow)
    print("The number of consonants : ",cons)
def upplowcase(y):
    upp=0
    low=0
    for a in y:
        if a.islower()==True:
            low+=1
        if a.isupper()==True:
            upp+=1
    print("The number of uppercase characters : ",upp)
    print("The number of lowercase characters : ",low)
def split(st,sp):
    print(st.split(sp))

def remove(k):
    strg=k.lower()
    newstr=" "
    for i in strg:
        if i not in newstr:
            newstr=newstr+i
    print("After removing the characters that are repeated in ",k)
    print("string becomes",newstr)

string=input("Enter the string : ")
vowcons(string)
upplowcase(string)
splitchar=input("Enter the character to split the string with this character : ")
split(string,splitchar)
remove(string)

    
