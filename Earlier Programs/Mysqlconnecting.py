import mysql.connector as sqlcon
mydb=sqlcon.connect(host="localhost",user="root",passwd="jessin")
sqlcursor=mydb.cursor()
"""
sqlcursor.execute("Create DATABASE F2021")
sqlcursor.execute("Show DATABASES")
for i in sqlcursor:
    print(i)
sqlcursor.execute("use F2021")
sqlcursor.execute("cREATE TABLE student(rollno int(3) primary key,name varchar(20),age int(2))")
sqlcursor.execute("Desc student")
for i in sqlcursor :
    print(i)
sqlcursor.execute("Show Tables")
for i in sqlcursor :
    print(i)



while 1==1:
    ch=int(input("-1 exit : "))
    if ch==-1:
        break
    rollno=int(input("rollno : "))
    age=int(input("Enter age : "))
    name=input("Enter name : ")
    sqlcursor.execute("insert into student values('"+str(rollno)+"','"+name+"','"+str(age)+"')")
    mydb.commit()
"""
sqlcursor.execute("use F2021")
sqlcursor.execute("SELECT * FROM STUDENT")
data=sqlcursor.fetchall()
cout=sqlcursor.rowcount
print(data)
dat=sqlcursor.fetchone()
print(dat)
