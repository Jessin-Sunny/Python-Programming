def updatedetails(stn,sl,su,ll,ls,c):
    ##stn='Belgium'
    ##sl=2000
    ##su=0
    ##ll=0
    ##ls=0
    ##c=0
    n=sl+su+ll+ls+c
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="jessin")
    mycursor=mydb.cursor()
    mycursor.execute("USE PROJECT")
    mycursor.execute("SELECT * FROM SEATING")
    for i in mycursor:
        print(i)
    mycursor.execute("UPDATE SEATING SET shortlower=shortlower-{} WHERE StadiumName='{}'".format(sl,stn))
    mycursor.execute("UPDATE SEATING SET shortupper=shortupper-{} WHERE StadiumName='{}'".format(su,stn))
    mycursor.execute("UPDATE SEATING SET longlower=longlower-{} WHERE StadiumName='{}'".format(ll,stn))
    mycursor.execute("UPDATE SEATING SET longshorter=longshorter-{} WHERE StadiumName='{}'".format(ls,stn))
    mycursor.execute("UPDATE SEATING SET Club=Club-{} WHERE StadiumName='{}'".format(c,stn))
    mydb.commit()
    print()
    mycursor.execute("SELECT * FROM SEATING")
    for i in mycursor:
        print(i)
    mydb.close()
