class Subject():

    def __init__(self, parent, name):
        self.name = name
        self.tk = parent.tk
        self.root = parent.root

        self.weight = 0
        self.exam_mid = 0
        self.final = 0
        self.project = 0
        self.hw = 0
        self.other = 0
        self.score = 0

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

    def student_initUI(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("300x220")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.tk.Message(frame, text="Subject Name : ").grid(row=0, column=0)
        self.e = self.tk.Entry(frame, width=10)
        self.e.grid(row=0, column=1, padx=5, pady=5)
        self.e.focus()
        self.e.bind("<Return>", self.add_subject)
        
        self.tk.Message(frame, text="Weight :", width=50).grid(row=0, column=2)
        self.weight = self.tk.Entry(frame, width=3)
        self.weight.grid(row=0, column=3, padx=5, pady=5)

        self.tk.Message(frame, text="Score", width=50).grid(row=1, column=1)
        self.tk.Message(frame, text="Max", width=50).grid(row=1, column=2)
        
        self.tk.Message(frame, text="Midterm :", width=80).grid(row=2, column=0)
        self.s_exam_mid = self.tk.Entry(frame, width=5)
        self.s_exam_mid.grid(row=2, column=1)
        self.b_exam_mid = self.tk.Entry(frame, width=5)
        self.b_exam_mid.grid(row=2, column=2)

        self.tk.Message(frame, text="Final :", width=50).grid(row=3, column=0)
        self.s_exam_final = self.tk.Entry(frame, width=5)
        self.s_exam_final.grid(row=3, column=1)
        self.b_exam_final = self.tk.Entry(frame, width=5)
        self.b_exam_final.grid(row=3, column=2)

        self.tk.Message(frame, text="Project :", width=50).grid(row=4, column=0)
        self.s_project = self.tk.Entry(frame, width=5)
        self.s_project.grid(row=4, column=1)
        self.b_project = self.tk.Entry(frame, width=5)
        self.b_project.grid(row=4, column=2)

        self.tk.Message(frame, text="Homework :", width=80).grid(row=5, column=0)
        self.s_hw = self.tk.Entry(frame, width=5)
        self.s_hw.grid(row=5, column=1)
        self.b_hw = self.tk.Entry(frame, width=5)
        self.b_hw.grid(row=5, column=2)

        self.tk.Message(frame, text="Other :", width=50).grid(row=6, column=0)
        self.s_other = self.tk.Entry(frame, width=5)
        self.s_other.grid(row=6, column=1)
        self.b_other = self.tk.Entry(frame, width=5)
        self.b_other.grid(row=6, column=2)
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=7, column=1)
        buttun_clo = self.tk.Button(frame, text='Close', command=self.top.destroy).grid(row=7, column=2)


    def print_box(self):
        pass
        # self.g = Grade(self)

    def remove(self):
        self.frame.destroy()

    def get_text(self):
        return self.name
