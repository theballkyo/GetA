from classes.subject import *
from classes.SubjectUI import *
from classes.student import *
from tkinter import ttk
class TeacherUI(SubjectUI):

    def __init__(self, parent):
        self.count_id = 0
        self.SUBJECT_LIST = []
        self.STD_LIST = {}
        self.tk = parent.tk
        self.root = parent.root
        self.initUI()
        self.data_list = []
        self.data_rule = []

    def initUI(self):
        self.root.geometry("600x500")
        self.root.resizable(0, 0)
        self.root.title(' "Get A" : Teacher mode')
        
        self.frame_subject = self.tk.Frame(self.root, bg="White")
        self.frame_subject.place(width=600, height=500, x=0, y=0)
        
        self.btn_std = self.tk.Button(self.frame_subject, text="Make Rule", command=self.make_rule)
        self.btn_std.place(x=200, y=20)
        self.btn_std = self.tk.Button(self.frame_subject, text="New Student", command=self.add_stu)
        self.btn_std.place(x=300, y=20)
        self.listbox = self.tk.Listbox(self.frame_subject, width = 20, height=20)
        self.listbox.place(x=230, y=50)
        self.btn_cal = self.tk.Button(self.frame_subject, text="Generate", command=self.generate)
        self.btn_cal.place(x=270, y=400)

    def generate(self):
        self.gen = self.tk.Toplevel()
        self.gen.title("Result")
        self.gen.geometry("300x250")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        num = 1
        a_grade = int(self.score_A.get())
        bp_grade = int(self.score_Bp.get())
        b_grade = int(self.score_B.get())
        cp_grade = int(self.score_Cp.get())
        c_grade = int(self.score_C.get())
        dp_grade = int(self.score_Dp.get())
        d_grade = int(self.score_D.get())
        print ("Subject : "+(self.sub.get()))
        temp = self.data_list[0][0]
        count = 0
        for j in self.data_list:
            if a_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is A")
                if j[0] == temp:
                    if count == 0:
                        count += 1
                    elif count == 1:
                        a_grade -= 1
                    else:
                        pass
                else:                   
                    a_grade -= 1
            elif bp_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is B+")
                if j[0] == temp:
                    pass
                else:
                    bp_grade -= 1
            elif b_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is B")
                if j[0] == temp:
                    pass
                else:
                    b_grade -= 1
            elif cp_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is C+")
                if j[0] == temp:
                    pass
                else:
                    cp_grade -= 1
            elif c_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is C")
                if j[0] == temp:
                    pass
                else:
                    c_grade -= 1
            elif dp_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is D+")
                if j[0] == temp:
                    pass
                else:
                    dp_grade -= 1
            elif d_grade != 0:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is D")
                if j[0] == temp:
                    pass
                else:
                    d_grade -= 1
            else:
                print ("No."+str(num) +" Name: "+str(j[1])+" Score: "+str(j[0])+" Grade is F")
            temp = j[0]
            num += 1

            self.tk.Message(self.gen, text="Subject :"+self.sub.get(), width=500).grid(row=2, column=0)
        

    def make_rule(self):
        self.new = self.tk.Toplevel()
        self.new.title("Make Rule")
        self.new.geometry("300x300")
        self.new.resizable(0, 0)
        self.new.focus()

        frame = self.tk.Frame(self.new)
        frame.pack()

        self.tk.Message(frame, text="Subject name : ", width=300).grid(row=0, column=0)
        self.sub = self.tk.Entry(frame, width=10)
        self.sub.grid(row=0, column=1, padx=5, pady=5)
        self.sub.focus()
        self.sub.bind("<Return>", self.add_rule)

        self.tk.Message(frame, text="A :", width=30).grid(row=2, column=0)
        self.score_A = self.tk.Entry(frame, width=5)
        self.score_A.grid(row=2, column=1)

        self.tk.Message(frame, text="B+ :", width=30).grid(row=4, column=0)
        self.score_Bp = self.tk.Entry(frame, width=5)
        self.score_Bp.grid(row=4, column=1)

        self.tk.Message(frame, text="B :", width=30).grid(row=6, column=0)
        self.score_B = self.tk.Entry(frame, width=5)
        self.score_B.grid(row=6, column=1)

        self.tk.Message(frame, text="C+ :", width=30).grid(row=8, column=0)
        self.score_Cp = self.tk.Entry(frame, width=5)
        self.score_Cp.grid(row=8, column=1)

        self.tk.Message(frame, text="C :", width=30).grid(row=10, column=0)
        self.score_C = self.tk.Entry(frame, width=5)
        self.score_C.grid(row=10, column=1)

        self.tk.Message(frame, text="D+ :", width=30).grid(row=12, column=0)
        self.score_Dp = self.tk.Entry(frame, width=5)
        self.score_Dp.grid(row=12, column=1)

        self.tk.Message(frame, text="D :", width=30).grid(row=14, column=0)
        self.score_D = self.tk.Entry(frame, width=5)
        self.score_D.grid(row=14, column=1)

        button_ok = self.tk.Button(frame, text='OK', command=self.add_rule)
        button_ok.grid(row=16, column=1)
        buttun_can = self.tk.Button(frame, text='Cancle', command='').grid(row=16, column =2)

    def add_rule(self):
        self.data_rule.append([int(self.score_A.get()), int(self.score_Bp.get()), int(self.score_B.get()), \
                               int(self.score_Cp.get()), int(self.score_C.get()), int(self.score_Dp.get()), int(self.score_D.get())])
    def add_stu(self):
        self.new = self.tk.Toplevel()
        self.new.title("Data new student")
        self.new.geometry("450x150")
        self.new.resizable(0, 0)
        self.new.focus()

        frame = self.tk.Frame(self.new)
        frame.pack()

        self.tk.Message(frame, text="Name : ", width=55).grid(row=0, column=0)
        self.n = self.tk.Entry(frame, width=10)
        self.n.grid(row=0, column=1, padx=5, pady=5)
        self.n.focus()
        self.n.bind("<Return>", self.add_stu)

        self.tk.Message(frame, text="Surname :", width=70).grid(row=0, column=2)
        self.s = self.tk.Entry(frame, width=10)
        self.s.grid(row=0, column=3, padx=5, pady=5)

        
        self.tk.Message(frame, text="Score :", width=500).grid(row=2, column=0)
        self.score = self.tk.Entry(frame, width=5)
        self.score.grid(row=2, column=1)
      

        button_ok = self.tk.Button(frame, text='OK', command=self.add_list)
        button_ok.grid(row=7, column=1)
        buttun_can = self.tk.Button(frame, text='Cancle', command='').grid(row=7, column=2)

    def add_list(self):
        self.data_list.append([int(self.score.get()), self.n.get()+" "+self.s.get()])        
    
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
