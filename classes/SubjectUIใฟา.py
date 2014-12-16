class SubjectUI():
    def __init__(self, parent):
        self.name = parent.name
        self.tk = parent.tk
        self.root = parent.root
        self.STD_LIST = parent.STD_LIST
        self.frame_subject = parent.frame_subject
        self.SUBJECT_LIST = parent.SUBJECT_LIST
        self.sbj = parent.sbj
        self.id = len(parent.SUBJECT_LIST)

    def teacher_initUI(self):
        # New Frame
        self.frame = self.tk.Frame(self.frame_subject)
        self.frame.grid()

        # Create 2 Button
        self.b = self.tk.Button(self.frame, text=self.name, command=self.add_score, width=20)
        self.rm = self.tk.Button(self.frame, text="Remove", command=self.remove)

        # Config grid
        self.b.grid(row=0, column=0, padx=5, pady=5)
        self.rm.grid(row=0, column=1, padx=5, pady=5)

    def student_initUI(self):
        """ Create UI for add new subject """
        # New Frame
        self.frame = self.tk.Frame(self.root)
        self.frame.pack()

        # Create 2 Button
        self.b = self.tk.Button(self.frame, text=self.name, command=self.print_box, width=50)
        self.rm = self.tk.Button(self.frame, text="Remove", command=self.remove)

        # Config grid
        self.b.grid(row=0, column=0, padx=5, pady=5)
        self.rm.grid(row=0, column=1, padx=5, pady=5)
       
    def add_score(self):
        self.top = self.tk.Toplevel()
        self.top.title("Add score")
        self.top.geometry("200x150")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.tk.Message(frame, text="Subject Name : " + self.name).grid(row=0, column=0)
        for id,std in self.STD_LIST.items():
            self.sbj.add_std(id, std)

        self.sbj.get_std()
