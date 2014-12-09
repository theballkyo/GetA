class Subject():

    def __init__(self, parent, name):
        self.name = name
        self.tk = parent.tk
        self.root = parent.root
        # # New Frame
        # self.frame = tk.Frame(root)
        # self.frame.pack()

        # # Create 2 Button
        # self.b = tk.Button(self.frame, text=name, command=self.print_box)
        # self.rm = tk.Button(self.frame, text="X", command=self.remove)

        # # Config grid
        # self.b.grid(row=0, column=0)
        # self.rm.grid(row=0, column=1)

    def teacher_initUI(self):
        # New Frame
        self.frame = self.tk.Frame(self.root)
        self.frame.pack()

        # Create 2 Button
        self.b = self.tk.Button(self.frame, text=self.name, command=self.print_box, width=50)
        self.rm = self.tk.Button(self.frame, text="Remove", command=self.remove)

        # Config grid
        self.b.grid(row=0, column=0, padx=5, pady=5)
        self.rm.grid(row=0, column=1, padx=5, pady=5)

    def print_box(self):
        pass
        # self.g = Grade(self)

    def remove(self):
        self.frame.destroy()

    def get_text(self):
        return self.name
