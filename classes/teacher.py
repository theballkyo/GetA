class Teacher():

    def __init__(self, parent):
        self.SUBJECT_LIST = []
        self.mode = parent.mode
        self.parent = parent
        self.tk = parent.tk
        self.root = parent.root
        
        self.initUI()

    def initUI(self):
        # Highschool
        if self.mode == 1:
            new = self.tk.Button(self.root, text='New Subject',
                                        command = self.new_subject_ui)
            new.pack()
        # University
        else:
            pass

    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("250x50")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.e = self.tk.Entry(frame)
        self.e.grid(row=0, column=0, padx=5, pady=15)
        self.e.focus()
        self.e.bind("<Return>", self.add_subject)
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=0, column=1)
        buttun_clo = self.tk.Button(frame, text='Close', command=self.top.destroy).grid(row=0, column=2)

