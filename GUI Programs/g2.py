from tkinter import *
import math
class CircleArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Area of Circle")
        self.grid()

        self._radiusLabel = Label(self, text = "Radius")
        self._radiusLabel.grid()
        self._radiusVar = DoubleVar()
        self._radiusEntry = Entry(self, textvariable = self._radiusVar)
        self._radiusEntry.grid()

        self._areaLabel = Label(self, text="Area")
        self._areaLabel.grid()
        self._areaVar = DoubleVar()
        self._areaEntry = Entry(self, textvariable = self._areaVar)
        self._areaEntry.grid()

        self._button = Button(self, text = "Compute", command = self._area)
        self._button.grid()

    def _area(self):
        radius = self._radiusVar.get()
        area = math.pi*radius*radius
        self._areaVar.set(area)

def main():
    CircleArea().mainloop()

main()
