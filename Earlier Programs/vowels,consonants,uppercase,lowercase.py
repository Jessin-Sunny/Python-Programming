#vowels,consonants,uppercase,lowercase
def vowcons(x):
    vow=0
    cons=0
    for i in str1:
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

str1=input("Enter a string : ")
new_str=str1.lower()
vowcons(new_str)
upplowcase(str1)
