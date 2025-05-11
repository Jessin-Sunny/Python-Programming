from tkinter import *

class ButtonDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Button Demo")
        self.grid()
        self._label = Label(self, text = "Hello")
        self._label.grid()
        self._button = Button(self, text = "Click Me", command = self._switch)
        self._button.grid()

    def _switch(self):
        if self._label["text"] == "Hello":
            self._label["text"] = "GoodBye"
        else:
            self._label["text"] = "Hello"

def main():
    ButtonDemo().mainloop()

main()
