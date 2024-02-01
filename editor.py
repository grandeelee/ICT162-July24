import tkinter as tk
from tkinter import filedialog, colorchooser, Scale, HORIZONTAL, ROUND
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk


# image editor class based on tkinter
class ImageEditor:
    def __init__(self, root):
        self._root = root
        self._root.geometry("1000x600")
        self._root.title("Image Editor")
        self._root.config(bg="white")

        # view
        self.left_frame = tk.Frame(self._root, width=200, height=600, bg="white")
        self.left_frame.pack(side="left", fill="both")

        self.canvas = tk.Canvas(self._root, width=750, height=600)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.open_button = tk.Button(self.left_frame, text="Add Image", bg="white")
        self.open_button.pack(side="top", pady=5, padx=3, fill="x")

        self.crop_button = tk.Button(self.left_frame, text="Crop Image", bg="white")
        self.crop_button.pack(side="top", pady=5, padx=3, fill="x")

        self.rotate_button = tk.Button(self.left_frame, text="Rotate Image", bg="white")
        self.rotate_button.pack(side="top", pady=5, padx=3, fill="x")

        self.flip_button = tk.Button(self.left_frame, text="Flip Image", bg="white")
        self.flip_button.pack(side="top", pady=5, padx=3, fill="x")

        self.text_button = tk.Button(self.left_frame, text="Add Text", bg="white")
        self.text_button.pack(side="top", pady=5, padx=3, fill="x")

        self.color_button = tk.Button(
            self.left_frame, text="Change Pen Color", bg="white"
        )
        self.color_button.pack(side="top", pady=5, padx=3, fill="x")

        self.pen_size_frame = tk.Frame(
            self.left_frame, bg="white", border=1, relief="solid"
        )
        self.pen_size_frame.pack(pady=5, padx=3, fill="x")

        self.pen_size_label = tk.Label(self.pen_size_frame, text="Pen Size", bg="white")
        self.pen_size_label.pack(side="top", pady=5, padx=3, fill="x")

        self.pen_size_slider = Scale(
            self.pen_size_frame, from_=1, to=10, orient=HORIZONTAL, bg="white"
        )
        self.pen_size_slider.pack(side="top", pady=5, padx=5, fill="x")

        self.filer_frame = tk.Frame(
            self.left_frame, bg="white", border=1, relief="solid"
        )
        self.filer_frame.pack(pady=5, padx=3, fill="x")

        self.filter_label = tk.Label(self.filer_frame, text="Select Filter", bg="white")
        self.filter_label.pack(side="top", pady=5, padx=3, fill="x")
        self.filter_combobox = ttk.Combobox(
            self.filer_frame,
            values=["None", "Black and White", "Blur", "Emboss", "Sharpen", "Smooth"],
        )
        self.filter_combobox.pack(side="top", pady=5, padx=3, fill="x")

        self.clear_button = tk.Button(self.left_frame, text="Clear", bg="#FF9797")
        self.clear_button.pack(side="top", pady=5, padx=3, fill="x")

        self.save_button = tk.Button(self.left_frame, text="Save Image", bg="white")
        self.save_button.pack(side="top", pady=5, padx=3, fill="x")

        # controller
        self.open_button.bind("<Button-1>", self.add_image)
        self.crop_button.bind("<Button-1>", self.crop_action)
        self.filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: self.apply_filter(self.filter_combobox.get()))
        
        self.pen_size_slider.bind("<ButtonRelease-1>", self.draw_action)

    def run(self):
        self._root.mainloop()

    def add_image(self, evt):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = Image.open(self.filename)

        self.edited_image = self.original_image.copy()
        self.display_image(self.edited_image)

    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        ideal_ratio = 600 / 750
        ratio = image.height / image.width

        if ratio > ideal_ratio:
            new_width = int(600 / ratio)
            new_height = 600

        else:
            new_width = 750
            new_height = int(750 * ratio)

        self.ratio = image.width / new_width

        self.new_image = image.resize((new_width, new_height))

        self.new_image = ImageTk.PhotoImage(self.new_image)
        self.canvas.image = self.new_image
        self.canvas.create_image(800 / 2, 600 / 2, image=self.new_image)

    def crop_action(self, evt):
        self.rectangle_id = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)

    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def crop(self, event):
        if self.rectangle_id:
            self.canvas.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.canvas.create_rectangle(
            self.crop_start_x,
            self.crop_start_y,
            self.crop_end_x,
            self.crop_end_y,
            width=1,
        )

    def end_crop(self, event):
        if (
            self.crop_start_x <= self.crop_end_x
            and self.crop_start_y <= self.crop_end_y
        ):
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif (
            self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y
        ):
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif (
            self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y
        ):
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        filtered_image = self.edited_image.crop((start_x, start_y, end_x, end_y))
        self.display_image(filtered_image)

    def apply_filter(self, filter):
        image = self.edited_image.copy()
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height))
        if filter == "Black and White":
            image = ImageOps.grayscale(image)
        elif filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)
        elif filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)
        self.display_image(image)

    def draw_action(self, event):
        self.color_code = ((255, 0, 0), '#ff0000')
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.canvas.bind("<ButtonPress>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []

    def draw(self, event):
        self.draw_ids.append(self.canvas.create_line(self.x, self.y, event.x, event.y, width=2, fill=self.color_code[-1], capstyle=ROUND, smooth=True))

        self.x = event.x
        self.y = event.y

root = tk.Tk()
app = ImageEditor(root)
app.run()


# left_frame = tk.Frame(root, width=200, height=600, bg="white")
# left_frame.pack(side="left", fill="y")

# canvas = tk.Canvas(root, width=750, height=600)
# canvas.pack()

# image_button = tk.Button(left_frame, text="Add Image",
#                          command=add_image, bg="white")
# image_button.pack(pady=15)

# color_button = tk.Button(
#     left_frame, text="Change Pen Color", command=change_color, bg="white")
# color_button.pack(pady=5)

# pen_size_frame = tk.Frame(left_frame, bg="white")
# pen_size_frame.pack(pady=5)

# pen_size_1 = tk.Radiobutton(
#     pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="white")
# pen_size_1.pack(side="left")

# pen_size_2 = tk.Radiobutton(
#     pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
# pen_size_2.pack(side="left")
# pen_size_2.select()

# pen_size_3 = tk.Radiobutton(
#     pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="white")
# pen_size_3.pack(side="left")

# clear_button = tk.Button(left_frame, text="Clear",
#                          command=clear_canvas, bg="#FF9797")
# clear_button.pack(pady=10)

# filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
# filter_label.pack()
# filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur",
#                                              "Emboss", "Sharpen", "Smooth"])
# filter_combobox.pack()


# filter_combobox.bind("<<ComboboxSelected>>",
#                      lambda event: apply_filter(filter_combobox.get()))


# canvas.bind("<B1-Motion>", draw)

# root.mainloop()


"""
def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="./")
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height))
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')
    

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height))
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

"""
