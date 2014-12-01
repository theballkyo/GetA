from classes.grade import *

class Subject():
    def __init__(self, tk, root, name):

        self.name = name
        self.tk = tk
        self.root = root
        # New Frame
        self.buttonframe = tk.Frame(root)
        self.buttonframe.pack()

        # Create 2 Button
        self.b = tk.Button(self.buttonframe, text=name, command=self.print_box)
        self.rm = tk.Button(self.buttonframe, text="X", command=self.remove)

        # Config grid
        self.b.grid(row=0, column=0)
        self.rm.grid(row=0, column=1)

    def print_box(self):
        self.g = Grade(self)

    def remove(self):
        self.buttonframe.destroy()

    def get_text(self):
        return self.b["text"]

