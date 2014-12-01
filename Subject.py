class Subject():
    def __init__(self, root):
        self.root = root

    def print_box(self):
        top = Toplevel()
        self.e = Entry(top)
        self.e.pack()

        button_ok = Button(top, text='OK', command=self.add_subject)
        button_ok.pack()
    def add_subject(self):
        print (self.e.get())
        self.b = Button(self.root, text=self.e.get())
        self.b.pack()

    
