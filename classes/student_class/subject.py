from classes.student_class.score import *

class Subject():
    def __init__(self, tk, root, name, listbox):
    
        self.score = 0
        
        self.name = name
        self.tk = tk
        self.root = root
        self.listbox = listbox
        # New Frame
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        listbox.insert("end", name)
        b = self.tk.Button(self.root, text="Delete",
                   command=lambda listbox=listbox: listbox.delete("anchor")).pack()
        # Create 2 Button   
        #self.b = tk.Button(self.frame, text=name, command=self.print_box)
        #self.rm = tk.Button(self.frame, text="X", command=self.remove)

        # Config grid
        #self.b.grid(row=0, column=0)
        #self.rm.grid(row=0, column=1)

    def print_box(self):
        self.g = Score(self)

    def remove(self):
        self.frame.destroy()

    def get_text(self):
        return self.b["text"]

    def set_score(self, score):
        self.score = score

    def set_base(self, base):
        self.base = base
