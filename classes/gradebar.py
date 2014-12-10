from tkinter import *

class Progressbar():

    obj_progress = False

    def __init__(self, root, max_width, max_height, color):
        self.canvas = Canvas(root, width=max_width-2, height=max_height)
        self.canvas.pack()
        self.color = color
        self.canvas.create_rectangle(2, 2, max_width, max_height, fill=self.color, outline="black")
        self.max_width = max_width
        self.max_height = max_height

    def update(self, progress):
        self.progress = min(max(progress, 0), 100)
        self.canvas.delete(self.obj_progress)
        pixel_height = self.max_height - ((self.progress * self.max_height))/100.0
        if self.progress >= 0:
            self.obj_progress = self.canvas.create_rectangle(3, 3, self.max_width, pixel_height, fill='lightgrey', outline='black')

total_score = int(input())
bar = LabelFrame(master, text="Grade Bar", padx=5, pady=5)
bar.pack(padx=10, pady=10)
if total_score >= 80:
    color = "green"
elif total_score >= 75:
    color = "green yellow"
elif total_score >= 70:
    color = "yellow"
elif total_score >= 65:
    color = "gold"
elif total_score >= 60:
    color = "dark orange"
elif total_score >= 55:
    color = "red"
elif total_score >= 50:
    color = "indian red"
elif total_score < 50:
    color = "brown"
bar = Progressbar(bar, 20, 400, color)
bar.update(total_score)

