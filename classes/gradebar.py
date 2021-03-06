from tkinter import *

class Progressbar():

    obj_progress = False

    def __init__(self, root, max_width, max_height, score):
        bar = Label(root)
        bar.place(x=60,y=30)
        self.canvas = Canvas(bar, width=max_width-2, height=max_height)
        self.canvas.pack()
        self.color = self.get_color(score)
        self.canvas_rec = self.canvas.create_rectangle(2, 2, max_width, max_height, fill=self.color, outline="black")
        self.max_width = max_width
        self.max_height = max_height

    def get_color(self, total_score):
        if total_score == 0:
            color = "light grey"
        elif total_score >= 80:
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
            color = "brown"
        elif total_score < 50:
            color = "dark red"
        return color
    
    def update(self, progress):
        self.canvas.itemconfig(self.canvas_rec, fill=self.get_color(progress))
        self.progress = min(max(progress, 0), 100)
        self.canvas.delete(self.obj_progress)
        pixel_height = self.max_height - ((self.progress * self.max_height))/100.0
        if self.progress >= 0:
            self.obj_progress = self.canvas.create_rectangle(3, 3, self.max_width, pixel_height, fill='lightgrey', outline='black')


