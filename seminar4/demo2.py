from tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Hello World")
        self.root.geometry('400x200')
        self.root.resizable(False, False)
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):

   
        # create widgets
        self.label_h = Label(self.root, text="Height: ", width=10)
        self.label_w = Label(self.root, text="Weight: ")
        self.label_bmi = Label(self.root, text="BMI: ")
        self.btn = Button(self.root, text="Calculate")

        self.entry_h = Entry(self.root)
        self.entry_w = Entry(self.root)
        self.result_bmi = Label(self.root, text="...")
        self.info = Label(self.root, text="Enter your height and weight")


        # place widgets using grid
        self.label_h.grid(row=0, column=0)
        self.label_w.grid(row=1, column=0)
        self.label_bmi.grid(row=2, column=0)
        self.btn.grid(row=3, column=0)
        self.entry_h.grid(row=0, column=1)
        self.entry_w.grid(row=1, column=1)
        self.result_bmi.grid(row=2, column=1)
        self.info.grid(row=3, column=1)

        # # place widgets using pack
        # self.label_h.pack(side=TOP)
        # self.entry_h.pack(side=TOP)
        # self.label_w.pack(side=TOP)
        # self.entry_w.pack(side=TOP)
        # self.label_bmi.pack(side=TOP)
        # self.result_bmi.pack(side=TOP)
        # self.btn.pack(side=TOP)
        # self.info.pack(side=TOP)




if __name__ == '__main__':
    app = App()
    