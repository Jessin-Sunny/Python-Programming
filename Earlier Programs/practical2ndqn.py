import mysql.connector as msql
def createdatabase():
    con=msql.connect(host="localhost",user="root",passwd="jessin")
    cur=con.cursor()
    cur.execute("create database practicalcs")
    print("DATABASE IS CREATED")
    con.close()
#createdatabase()
def createtable_emp():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    cur.execute("create table emp\
               (empno INT PRIMARY KEY,\
               empname VARCHAR(30),\
               job VARCHAR(30),\
               mgr int,\
               hiredate date,\
               sal int,\
               comm int,\
               deptno int)")
    print("TABLE emp IS CREATED")
    con.close()
#createtable_emp()
def createtable_dept():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute("use practicalcs")
    cur.execute("create table dept\
               (deptno INT PRIMARY KEY,\
               dname VARCHAR(30),\
               loc VARCHAR(30))")
    print("TABLE dept IS CREATED")
    con.close()

#createtable_dept()
def insertdata_emp():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute('set autocommit=1')
    cur.execute("use practicalcs")
    while True:
        empno=int(input("Enter the empno : "))
        empname=input("Enter the empname : ")
        job=input("Enter the job : ")
        mgr=input("Enter the mgr : ")
        hiredate=input("Enter the hiredate : ")
        sal=int(input("Enter the salary : "))
        comm=input("Enter the commision : ")
        deptno=input("Enter the deptno : ")
        qry="insert into emp values({},'{}','{}',{},'{}',{},{},{})"
        cur.execute(qry.format(empno,empname,job,mgr,hiredate,sal,comm,deptno))
        print("DATA INSERTED SUCCESSFULLY")
        
        ch=input("Do you want to continue ?(y/n) : ")
        if(ch.lower()=="n"):
            break
    con.close()
#insertdata_emp()
def insertdata_dept():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    cur.execute('set autocommit=1')
    cur.execute("use practicalcs")
    while True:
        deptno=int(input("Enter the deptno : "))
        dname=input("Enter the deptname : ")
        loc=input("Enter the location : ")
       
        qry="insert into dept values({},'{}','{}')"
        cur.execute(qry.format(deptno,dname,loc))
        print("DATA INSERTED SUCCESSFULLY")
        
        ch=input("Do you want to continue ?(y/n) : ")
        if(ch.lower()=="n"):
            break
    con.close()
#insertdata_dept()
def delete():
     con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
     cur=con.cursor()
     r=int(input("Enter the empno of employee to be deleted : "))
     qry='delete from emp where empno={}'
     
     cur .execute(qry.format(r))
     con.commit()
     print("RECORD IS DELETED")
     con.close()
def modify():
     con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
     cur=con.cursor()
     r=int(input("Enter the empno of employee whose HRA to be modified : "))
     m=int(input("Enter the new HRA : "))
     q="update emp set HRA={} where empno={}"
     cur.execute(q.format(m,r))
     con.commit()
     print("RECORD IS MODIFIED")
def addHRA():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    qry="alter table emp add HRA int Default 2000"
    cur.execute(qry)
    con.commit()
    print("COLUMN HRA IS ADDED")
def display_mc():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    qry="Select empno, empname, job, dname from emp natural join dept where job in ('Manager','Clerk')"
    cur.execute(qry)
    rs=cur.fetchall()
    print(80*'=')
    print('%12s%12s%12s%12s'%('empno', 'empname', 'job', 'dname'))
    print(80*'=')
    for i in rs:
        for j in range(len(i)):
            print('{:>12}'.format(i[j]),end=' ')
        print()
    print(80*'=')   
    con.close()
#display_mc()
def display_comm():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    qry="Select empname, job, sal, comm from emp\
    where comm is NOT NULL order by sal desc"
    cur.execute(qry)
    rs=cur.fetchall()
    print(80*'=')
    print('%12s%12s%12s%12s'%('empname','job', 'sal', 'comm'))
    print(80*'=')
    for i in rs:
        for j in range(len(i)):
            try:
                print('{:>12}'.format(i[j]),end=' ')
            except:
                print('{:>12}'.format("NULL"),end=' ')
        print()
    print(80*'=')   
    con.close()   
def display_minmax():
    con=msql.connect(host="localhost",user="root",passwd="jessin",database="practicalcs")
    cur=con.cursor()
    qry="Select min(sal), max(sal), sum(sal), avg(sal), count(job) from emp"
    cur.execute(qry)
    rs=cur.fetchall()
    print(80*'=')
    print('%12s%12s%16s%12s%20s'%('min(sal)','max(sal)','sum(sal)','avg(sal)','count(job)'))
    print(80*'=')
    for i in rs:
        for j in range(len(i)):
            print('{:>12}'.format(i[j]),end=' ')
        print()
    print(80*'=')
    con.close() 
print("1 : For adding a column HRA with default value 2000")
print("2 : For modifying HRA with empno")
print("3 : For displaying name, job and annual salary of employees whose comm is assigned in descending order of salary")
print("4 : For deleting the record of employee with empno")
print("5 : For displaying empno, name, job and department name who are either a manger or a clerk")
print("6 : For displaying minimum and maximum, sum and average of salary along with number of records in job")
print("7 : EXIT")
while True:
    ch=int(input("\nEnter your choice : "))
    if ch==1:
          addHRA()
    elif ch==2:
        modify()
    elif ch==3:
        display_comm()
    elif ch==4:
        delete()
    elif ch==5:
        display_mc()
    elif ch==6:
        display_minmax()
    elif ch==7:
        break
    else:
        print("INVALID CHOICE!!!")
        continue

