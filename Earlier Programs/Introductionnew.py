print("\tWELCOME TO FORZA")
print("="*50)
print("1 : USER")
print("2 : ADMINISTRATOR")
print("3 : EXIT\n ")
ch=int(input("Enter your choice : "))
if ch==1:
    print("1 : To display STADIUM DETAILS")
    print("2 : To display TEAM DETAILS")
    print("3 : To display MATCH FIXTURES")
    print("4 : To book a SEAT")
    print("5 : To display SCOREBOARD\n")
    u=int(input("Enter your choice : "))
    if u==1:
        pass
        from user import stadium
    elif u==2:
        pass
        from user import team
    elif u==3:
        pass
        #user.fixture()
    elif u==4:
        pass
        #user.reservation()
    elif u==5:
        pass
        #user.scoreboard()
    else:
        print("Invalid Choice!!!")
elif ch==2:
    #import administrator
    c=input("Enter your password : ")
    x="kickoff123"
    if c==x:
        print("\n1 : To create match fixtures")
        print("2 : To see stadium booking status")
        print("3 : TO create scoreboard\n")
        a=int(input("Enter your choice : "))
        if a==1:
            pass
            #administrator.fixture()
        elif a==2:
            pass
            #administrator.booking()
        elif a==3:
            pass
            #administrator.scoreboard()
        else:
            print("Invalid Choice!!!")
    else:
        print("Incorrect Password!!!\n")
elif ch==3:
    print("Thank You")
else:
    print("Invalid Choice!!!")
    
