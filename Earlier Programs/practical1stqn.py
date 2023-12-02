import mysql.connector as msql
def createtable():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    try:
        cur.execute("use practicalcs")
        cur.execute("Create table Garment\
            (GCODE int(5) primary key,\
            Description varchar(20),\
            PRICE int(5),\
            FCODE varchar(3),\
            READYDATE date)")
        print("TABLE Garment IS CREATED")
        cur.execute("Create table Fabric\
            (FCODE char(3) primary key,\
            Description varchar(15))")
        print("TABLE Fabric IS CREATED")
    except:
        print("Table Garment and Fabric Exists!!!\n")
def insergar():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    print("Insert Records in Table Garments")
    try:
        while True:
            gcd=input("Enter GCODE : ")
            des=input("Enter Description : ")
            pr=input("Enter Price : ")
            fcd=input("Enter FCODE : ")
            rea=input("Enter ReadyDate : ")
            qry="Insert into Garment values({},'{}',{},'{}','{}')"
            cur.execute(qry.format(gcd,des,pr,fcd,rea))
            con.commit()
            ch=input("Add more records(y/n) : ")
            if ch.lower()!='y':
                break
    except:
        print("Error in Garment table")
def viewgar():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    cur.execute("Select * from garment")
    rs=cur.fetchall()
    print(70*'=')
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'
          .format('GCODE','Description','Price','FCODE','ReadyDate'))
    print(70*'=')
    for row in rs:
          for coln in range(len(row)):
              print("%-15s"%row[coln],end='')
          print()
    print(70*'=')
    print("Number of records=",cur.rowcount)
def insertfab():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    print("Insert records in Table Fabric..")
    try:
        while True:
            fcd=input("Enter FCODE : ")
            typ=input("Enter Type : ")
            qry='Insert into fabric values("{}","{}")'
            cur.execute(qry.format(fcd,typ))
            con.commit()
            ch=input("Add more records(y/n): ")
            if ch.lower()!='y':
                break
    except:
        print("Error in Fabric table")
def viewfab():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    cur.execute("Select * from fabric")
    rs=cur.fetchall()
    print(' '*5,20*'=')
    print('%12s%12s'%('FCODE','TYPE'))
    print(' '*5,20*'=')
    for row in rs:
        for coln in range(len(row)):
            print('{:>12}'.format(row[coln]),end='')
        print()
    print(' '*5,20*'=')
    print(' '*5,"Number of records=",cur.rowcount)
def modifygar():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    gcd=input("Enter GCODE to be modify price : ")
    qry="Select * from garment where gcode={}"
    cur.execute(qry.format(gcd))
    rs=cur.fetchall()
    if rs:
        pri=input("Enter the new price : ")
        qry="Update garment set price={} where gcode={}"
        cur.execute(qry.format(pri,gcd))
        con.commit()
        print("\nSuccessfully Updated...")
    else:
        print("\nRecord not found!!!")
def deletegar():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    gcd=input("Enter GCODE TO delete : ")
    qry="Select * from garment where gcode={}"
    cur.execute(qry.format(gcd))
    rs=cur.fetchall()
    if rs:
        qry="Delete from garment where gcode={}"
        cur.execute(qry.format(gcd))
        con.commit()
        print("\nSuccessfully Deleted...")
    else:
        print("\nRecord not found!!!")
msg="\n\
1. Create Tables\n\
2. View Garment and Fabric\n\
3. Insert in Garment\n\
4. Insert in Fabric\n\
5. Modify Price in Garment\n\
6. Delete a record in Garment\n\
7. Exit"
while True:
    print(msg)
    ch=int(input("Enter your choice : "))
    if ch==1:
        createtable()
    elif ch==2:
        viewgar()
        viewfab()
    elif ch==3:
        insergar()
    elif ch==4:
        insertfab()
    elif ch==5:
        modifygar()
    elif ch==6:
        deletegar()
    elif ch==7:
        break
    else:
        print("Invalid Choice")
          
    
            
