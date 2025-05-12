class Car(object):
    def __init__(self, rno = 0000000, color = "", mileage = 0, year = 0000):
        self._rno = rno
        self._color = color
        self._mileage = mileage
        self._year = year

    def getrno(self):
        print("Registration No: ",self._rno)
    def getcolor(self):
        print("Color: ", self._color)
    def getmileage(self):
        print("Mileage: ", self._mileage)
    def getyear(self):
        print("Year: ",self._year)

    def setrno(self, rno):
        self._rno = rno
    def setcolor(self, color):
        self._color = color
    def setmileage(self, mileage):
        self._mileage = mileage
    def setyear(self, year):
        self._year = year
        
    def __str__(self):
        return "Registration No: " + str(self._rno) + "\nColor : " + self._color \
               + "\nMileage: " + str(self._mileage) + "\nYear: " + str(self._year)


c1 = Car()
c1.setrno(8521365)
c1.setcolor("blue")
c1.setmileage(20)
c1.setyear(2022)
c1.getrno()
c1.getcolor()
c1.getmileage()
c1.getyear()
print(c1)
        
        
