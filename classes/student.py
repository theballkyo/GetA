from classes.student_class.subject import *

class Student:

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
        self.top.geometry("300x200")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.tk.Message(frame, text="Subject Name : ").grid(row=0, column=0)
        self.e = self.tk.Entry(frame, width=10)
        self.e.grid(row=0, column=1, padx=5, pady=5)
        self.e.focus()
        #self.e.bind("<Return>", self.add_subject)
        
        self.tk.Message(frame, text="Weight :", width=50).grid(row=0, column=2)
        self.weight = self.tk.Entry(frame, width=3)
        self.weight.grid(row=0, column=3, padx=5, pady=5)

        self.tk.Message(frame, text="Score", width=50).grid(row=1, column=1)
        self.tk.Message(frame, text="Max", width=50).grid(row=1, column=2)
        
        self.tk.Message(frame, text="Exam :", width=50).grid(row=2, column=0)
        self.s_exam = self.tk.Entry(frame, width=5)
        self.s_exam.grid(row=2, column=1)
        self.b_exam = self.tk.Entry(frame, width=5)
        self.b_exam.grid(row=2, column=2)

        self.tk.Message(frame, text="Project :", width=50).grid(row=3, column=0)
        self.s_project = self.tk.Entry(frame, width=5)
        self.s_project.grid(row=3, column=1)
        self.b_project = self.tk.Entry(frame, width=5)
        self.b_project.grid(row=3, column=2)

        self.tk.Message(frame, text="Homework :", width=80).grid(row=4, column=0)
        self.s_hw = self.tk.Entry(frame, width=5)
        self.s_hw.grid(row=4, column=1)
        self.b_hw = self.tk.Entry(frame, width=5)
        self.b_hw.grid(row=4, column=2)

        self.tk.Message(frame, text="Other :", width=50).grid(row=5, column=0)
        self.s_other = self.tk.Entry(frame, width=5)
        self.s_other.grid(row=5, column=1)
        self.b_other = self.tk.Entry(frame, width=5)
        self.b_other.grid(row=5, column=2)
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=6, column=1)
        buttun_clo = self.tk.Button(frame, text='Close', command=self.top.destroy).grid(row=6, column=2)

    def set_e_text(self, text):
        """ Set Entry Text """
        self.e.delete(0, len(self.e.get()))
        self.e.insert(0,text)
        return True

    def add_subject(self, event=""):
        """ New subject """
        if len(self.SUBJECT_LIST) > 20:
            self.tk.messagebox.showinfo(message="Subjects is maximum", title="Error !")
            self.top.destroy()
            return False

        name = self.e.get()
        if name == "":
            self.tk.messagebox.showinfo(message="Please enter subject name.", title="Error !")
            # self.top.destroy()
            # self.new_subject()
            self.e.focus()
            return False

        # New object subject
        btn = Subject(self.tk, self.root, name)
        self.SUBJECT_LIST.append(btn)
        self.tk.messagebox.showinfo(message="Success - " + str(name), title="Success")
        self.set_e_text("")
        self.get_subject()
        self.e.focus()

    def get_subject(self):
        """ Get all subjects """
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")

