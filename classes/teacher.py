from classes.student_class.subject import *

class Teacher():

    def __init__(self, parent):
        self.SUBJECT_LIST = []
        self.tk = parent.tk
        self.root = parent.root
        self.frame = parent.frame
        self.initUI()
        # self.member = int(input())
        # self.data = []
        # self.a = int(input())
        # self.bp = int(input())
        # self.b = int(input())
        # self.cp = int(input())
        # self.c = int(input())
        # self.dp = int(input())
        # self.d = int(input())
        # for i in range(self.member):
        #     self.data.append([int(input()), i+1])
        # self.data.sort(reverse = True)

    def initUI(self):
        #self.frame = self.tk.Frame(self.top)
        #self.frame.pack()

        # self.tk.Message(self.frame, text="Subject Name : ").grid(row=0, column=0)

        self.btn_std = self.tk.Button(self.frame, text="New Student")
        self.btn_std.grid(row=1, column=0)
        self.btn_sbj = self.tk.Button(self.frame, text="New Subject", command=self.new_subject_ui)
        self.btn_sbj.grid(row=2, column=0)

        # self.e = self.tk.Entry(self.frame, width=10)
        # self.e.grid(row=0, column=1, padx=5, pady=5)
        # self.e.focus()
    
    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("200x150")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        # self.tk.Message(frame, text="Subject Name : ").grid(row=0, column=0)
        self.e = self.tk.Entry(frame, width=10)
        self.e.grid(row=0, column=1, padx=5, pady=5)
        self.e.focus()
        #self.e.bind("<Return>", self.add_subject)
        
        self.tk.Message(frame, text="Score").grid(row=1, column=0)
        self.in_score = self.tk.Entry(frame, width=5)
        self.in_score.grid(row=1, column=1, padx=5, pady=5)
        self.base
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)

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

    def result(self):
        for i in range(len(self.data)):
            print ("No."+ str(self.data[i][1])+" Score : "+str(self.data[i][0])),
            if self.a != 0:
                print ("Grade is A")
                self.a -= 1
            elif self.bp != 0:
                print ("Grade is B+")
                self.bp -= 1
            elif self.b != 0:
                print ("Grade is B")
                self.b -= 1
            elif self.cp != 0:
                print ("Grade is C+")
                self.cp -= 1
            elif self.c != 0:
                print ("Grade is C")
                self.c -= 1
            elif self.dp != 0:
                print ("Grade is D+")
                self.dp -= 1
            elif self.d != 0:
                print ("Grade is D")
                self.d -= 1
            else:
                print ("Grade is F")


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

    def get_subject(self):
        """ Get all subjects """
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")