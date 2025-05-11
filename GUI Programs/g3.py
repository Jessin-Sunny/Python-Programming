from tkinter import *

class ImageDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image Display")
        self.grid()
        self._image = PhotoImage(file = "smokey.gif")
        self._imageLabel = Label(self, image = self._image, text = "Smokey the cat")
        self._imageLabel.grid()
        self._textLabel = Label(self, text = "Smokey the cat")
        self._textLabel.grid()

def main():
    ImageDemo().mainloop()

main()
