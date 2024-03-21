import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class soupGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Slurp Soup")

        self.soups = { 'C':['Clam Chowder',9.9,50], 'M':['Mushroom',7.9, 50], 'T':['Tomato',5.9,50],'P':['Pumpkin',5.9,50], 'O':['Oxtail',9.9,50]}

        self.soups = dict(sorted(self.soups.items()))

        self.radio_mode = tk.StringVar(value="r")
        # model
        self.code_label = ttk.Label(self.root, text="Soup Code:")
        self.code_entry = ttk.Entry(self.root)

        self.qty_label = ttk.Label(self.root, text="Quantity:")
        self.qty_entry = ttk.Entry(self.root)

        self.radio_frame = ttk.Frame(self.root)
        self.radio_purchase = ttk.Radiobutton(self.radio_frame, text="Purchase", variable=self.radio_mode, value="p")
        self.radio_replenish = ttk.Radiobutton(self.radio_frame, text="Replenish", variable=self.radio_mode, value="r")

        self.btn_frame = ttk.Frame(self.root)
        self.btn_display = ttk.Button(self.btn_frame, text="Display Soup")
        self.btn_display.bind("<Button-1>", self.display)
        self.btn_submit = ttk.Button(self.btn_frame, text="Submit")
        self.btn_submit.bind("<Button-1>", self.submit)

        self.txt = ScrolledText(self.root, height=10, width=50, state='disabled')

        # view
        self.radio_purchase.grid(row=0, column=0)
        self.radio_replenish.grid(row=0, column=1)

        self.btn_display.grid(row=0, column=0)
        self.btn_submit.grid(row=0, column=1)

        self.code_label.grid(row=1, column=0, sticky="E")
        self.code_entry.grid(row=1, column=1)

        self.qty_label.grid(row=2, column=0, sticky="E")
        self.qty_entry.grid(row=2, column=1)

        self.radio_frame.grid(row=3, column=1)
        self.btn_frame.grid(row=4, column=1)

        self.txt.grid(row=5, columnspan=3)

        self.root.mainloop()

    # controller
    def display(self, evt):
        self.txt['state'] = 'normal'
        self.txt.delete('1.0', 'end')

        if self.radio_mode.get() == 'p':
            for soup in self.soups.values():
                if soup[-1] > 0:
                    self.txt.insert("end", f"{soup[0]}: {soup[-1]}\n")

        if self.radio_mode.get() == 'r':
            for soup in self.soups.values():
                if soup[-1] < 50:
                    self.txt.insert("end", f"{soup[0]}: {soup[-1]}\n")

        self.txt['state'] = 'disabled'

    def submit(self, evt):
        code = self.code_entry.get()
        if not code in ["C", "M", "T", "O", "P"]:
            self.error_display('please enter code in ["C", "M", "T", "O", "P"]')
        try:
            qty = int(self.qty_entry.get())
        except ValueError:
            self.error_display("please enter integer value")
        else:
            if self.radio_mode.get() == "p":
                soup = self.soups.get(code)
                if soup:
                    self.soups[code][2] = max(0, soup[2] - qty)
                    self.display(evt)

            elif self.radio_mode.get() == "r":
                soup = self.soups.get(code)
                if soup:
                    self.soups[code][2] = min(50, soup[2] + qty)
                    self.display(evt)

        
    def error_display(self, msg):
        self.txt['state'] = 'normal'
        self.txt.delete('1.0', 'end')
        self.txt.insert("end", msg + '\n')
        self.txt['state'] = 'disabled'        

if __name__ == "__main__":
    app = soupGui()