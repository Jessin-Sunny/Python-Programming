from student import Student
s = Student("Ann", 5)
s.setScore(0, 100)
s.setScore(1, 98)
s.setScore(2, 100)
s.setScore(3, 95)
s.setScore(4, 90)
print(s.getScore(1))
s.getAvg()
print(s)
