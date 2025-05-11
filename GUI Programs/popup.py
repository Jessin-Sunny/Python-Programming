from tkinter import *
from tkinter import messagebox

class DialogDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Pop Up")
        self.grid()
        self._b1 = Button(self, text = "Info", command = self._info)
        self._b1.grid()
        self._b2 = Button(self, text = "Warning", command = self._warns)
        self._b2.grid()
        self._b3 = Button(self, text = "Error", command = self._error)
        self._b3.grid()
        self._b4 = Button(self, text = "Yes/No", command = self._yesno)
        self._b4.grid()
        self._b5 = Button(self, text = "Ok/Cancel", command = self._okcancel)
        self._b5.grid()

    def _info(self):
        messagebox.showinfo(message = "Hi there!!", parent = self)
    def _warns(self):
        messagebox.showinfo(message = "Warning!!!!", parent = self)
    def _error(self):
        messagebox.showerror(message = "Try again", parent = self)
    def _yesno(self):
        messagebox.askyesno(message = "Do you love Football ? ", parent = self)
    def _okcancel(self):
        messagebox.askokcancel(message = "Do you want to exit ? ", parent = self)

def main():
    DialogDemo().mainloop()

main()
