class Subject():
    def __init__(self, tk, name):
        self.name = name
        self.tk = tk

    def print_box(self):
        top = self.tk.Toplevel()
        self.e = Entry(top)
        self.e.pack()

        button_ok = self.tk.Button(top, text='OK', command=self.add_subject)
        button_ok.pack()
    def add_subject(self):
        print (self.e.get())
        self.b = Button(self.root, text=self.e.get())
        self.b.pack()

    
