from tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Hello World")
        self.root.geometry('400x200')
        self.root.resizable(False, False)
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    