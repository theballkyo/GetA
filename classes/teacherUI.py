from classes.subject import *
from classes.SubjectUI import *
from classes.student import *
class TeacherUI(SubjectUI):

    def __init__(self, parent):
        self.count_id = 0
        self.SUBJECT_LIST = []
        self.STD_LIST = {}
        self.tk = parent.tk
        self.root = parent.root
        self.initUI()

    def initUI(self):
        self.root.geometry("600x500")
        self.root.resizable(0, 0)
        self.root.title(' "Get A" : Student Mode')
        
        self.frame_subject = self.tk.Frame(self.root, bg="Blue")
        self.frame_subject.place(width=300, height=250, x=0, y=0)

        self.frame_edit = self.tk.Frame(self.root, width=400, height=300, bg="Red")
        self.frame_edit.place(width=300, height=250, x=300, y=0)

        self.frame_result = self.tk.Frame(self.root, width=800, height=300, bg="Yellow")
        self.frame_result.place(width=600, height=250, x=0, y=250)

        self.btn_std = self.tk.Button(self.frame_subject, text="New Student", command=self.new_std_ui)
        self.btn_std.grid(row=1, column=0, padx=5, pady=5)
        self.btn_sbj = self.tk.Button(self.frame_subject, text="New Subject", command=self.new_subject_ui)
        self.btn_sbj.grid(row=2, column=0, padx=5, pady=5)

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
    
    def new_std_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new Student")
        self.top.geometry("250x50")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.e = self.tk.Entry(frame)
        self.e.grid(row=0, column=0, padx=5, pady=15)
        self.e.focus()
        self.e.bind("<Return>", self.add_std)

        button_ok = self.tk.Button(frame, text='OK', command=self.add_std)
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

        self.name = self.e.get()
        if self.name == "":
            self.tk.messagebox.showinfo(message="Please enter subject name.", title="Error !")
            # self.top.destroy()
            # self.new_subject()
            self.e.focus()
            return False

        # New object subject
        self.sbj = Subject(self)
        # sbj.teacher_initUI()
        SubjectUI(self).teacher_initUI()

        self.SUBJECT_LIST.append(self.sbj)
        self.tk.messagebox.showinfo(message="Success - " + str(self.name), title="Success")
        self.set_e_text("")
        self.get_subject()
        self.e.focus()

    def add_std(self, event=""):
        self.name = self.e.get()
        self.STD_LIST[self.count_id] = self.name
        self.count_id += 1
        self.tk.messagebox.showinfo(message="Success - " + str(self.name), title="Success")
        self.set_e_text("")
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

    def cal_grade(self):
        pass
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

    def get_subject(self):
        """ Get all subjects """
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")