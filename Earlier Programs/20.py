def dictionary(n):
    dict1={}
    name=""
    rollno=0
    mark=0
    for i in range(n):
        rollno=int(input("Enter the rollno : "))
        name=input("Enter the name of student : ")
        mark=float(input("Enter the mark of student : "))
        dict1[rollno]=[name,mark]
    print(dict1)
    for j in dict1:
        if dict1[j][1]>75:
            print(dict1[j][0])

n=int(input("Enter the number of students : "))
dictionary(n)
