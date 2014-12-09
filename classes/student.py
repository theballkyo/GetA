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
            new_subject = self.tk.Button(self.root, text='New Subject',
                                        command = self.new_subject)
            new_subject.pack()
        # University
        else:
            pass
        
    def new_subject(self):
        """ Show new windows add new subject """
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

