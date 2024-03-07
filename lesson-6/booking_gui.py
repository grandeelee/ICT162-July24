from tkinter import *
from tkinter.scrolledtext import ScrolledText
from flight import Flight
from datetime import datetime

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Flight Booking System")
        self.root.geometry('400x200')
        self.root.resizable(False, False)
        self.flights = [Flight("SQ123", "LA", datetime(2021, 12, 25, 4, 15), 500), Flight("SQ121", "DPS", datetime(2021, 12, 25, 4, 15), 200)]
        self.options = [f"{f.flightNo} {f.destination}" for f in self.flights]
        self.create_widgets()
        self.root.mainloop()
        
    
    def create_widgets(self):
        self.option = StringVar()
        self.option.set(self.options[0])
        self.label = Label(self.root, text="Select flight: ")
        self.drop = OptionMenu(self.root, self.option, *self.options)
        self.btn = Button(self.root, text="Book")
        self.display = ScrolledText(self.root, width=40, height=10)

        # place widgets using grid
        self.label.grid(row=0, column=0)
        self.drop.grid(row=0, column=1)
        self.btn.grid(row=0, column=2)
        self.display.grid(row=2, column=0, columnspan=3)

        # bind event to button
        self.btn.bind("<Button-1>", self.book)

    def book(self, evt=None):
        flight = self.option.get()
        self.display.insert(END, f"Booked {flight}\n")

if __name__ == '__main__':
    app = App()