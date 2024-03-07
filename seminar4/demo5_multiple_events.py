from tkinter import *
from tkinter.scrolledtext import ScrolledText

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
        self.label_h = Label(self.root, text="Height: ")
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

        # bind event to button
        self.btn.bind("<Button-1>", self.calculate)
        self.entry_h.bind("<Button-1>", self.calculate)
        self.entry_w.bind("<Button-1>", self.calculate)

    def calculate(self, evt):
        # determine which widget triggered the event
        widget = evt.widget
        if widget == self.btn:
            try:
                h = float(self.entry_h.get())
                w = float(self.entry_w.get())
                bmi = w / (h ** 2)
            except Exception as e:
                self.info['text'] = e
                self.info['fg'] = "red"
            else:
                self.result_bmi['text'] = f"{bmi:.2f}"
                if bmi < 25:
                    self.info['text'] = "Normal"
                    self.info['fg'] = "green"
        else:
            self.info['text'] = "Enter your height and weight"
            self.info['fg'] = "black"
            self.result_bmi['text'] = "..."


if __name__ == '__main__':
    app = App()
    