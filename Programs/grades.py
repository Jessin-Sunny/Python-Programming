marks = int(input("Enter your marks : "))
if marks > 135 and marks <=150:
    grade = 'S'
elif marks > 120 and marks <=135:
    grade = 'A+'
elif marks > 120 and marks <=135:
    grade = 'A+'
elif marks > 105 and marks <=120:
    grade = 'A'
elif marks > 90 and marks <=105:
    grade = 'B+'
elif marks > 75 and marks <=90:
    grade = 'B'
elif marks > 60 and marks <=75:
    grade = 'C+'
elif marks > 45 and marks <=60:
    grade = 'C'
elif marks > 40 and marks <=45:
    grade = 'D'
else:
    grade = 'F'
print("Grade : ",grade)
