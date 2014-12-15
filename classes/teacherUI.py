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
        self.check_mode = 0
        self.check_score = []

    def initUI(self):
        """       UI window       make rule - for calculate grade in base on group score mode
        if you dont want to use make rule mode just add student and click generate"""
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
        self.btn_del = self.tk.Button(self.frame_subject, text="Delete", command=self.del_std)
        self.btn_del.place(x=270, y=400)
        self.btn_cal = self.tk.Button(self.frame_subject, text="Generate", command=self.select_gen)
        self.btn_cal.place(x=270, y=430)

        self.root.mainloop

    def del_std(self):
        index = int(self.listbox.curselection()[0])
        del(self.data_list[index])
        self.listbox.delete("anchor")

    def select_gen(self):
        """       Select Generate Mode       normal mode & Group score mode """
        if self.check_mode == 0:
            self.generate_normal()
        else:
            self.gen_grade()
            
    def generate_normal(self):
        """This Funtion for calculate grade in normal mode"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        # self.data_list.sort(reverse = True)
        num = 1
        spc = 60
        for j in sorted(self.data_list, reverse=True):
            self.tk.Label(self.gen, text=str(num), fg="White",bg="black").place(x=15, y = spc)
            self.tk.Label(self.gen, text=str(j[1]), fg="White", bg="black").place(x=150, y = spc)
            self.tk.Label(self.gen, text=str(j[0]), fg="White", bg="black").place(x=290, y = spc)

            if j[0] >= 80:
                self.tk.Label(self.gen, text="A", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 75:
                self.tk.Label(self.gen, text="B+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 70:
                self.tk.Label(self.gen, text="B", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 65:
                self.tk.Label(self.gen, text="C+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 60:
                self.tk.Label(self.gen, text="C", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 55:
                self.tk.Label(self.gen, text="D+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 50:
                self.tk.Label(self.gen, text="D", fg="White", bg="black").place(x=400, y = spc)
            else:
                self.tk.Label(self.gen, text="F", fg="White", bg="black").place(x=400, y = spc)
            num += 1
            spc += 20
        score_board = self.tk.Label(self.gen, text="Score Board", fg="White",bg="black")
        score_board.place(x=150, y=10)

        sequence = self.tk.Label(self.gen, text="No.", fg="White",bg="black")
        sequence.place(x=10,y=40)

        name = self.tk.Label(self.gen, text="Name", fg="White", bg="black")
        name.place(x=170, y = 40)

        score = self.tk.Label(self.gen, text="Score", fg="White", bg="black")
        score.place(x=300, y = 40)

        grade = self.tk.Label(self.gen, text="Grade", fg="White", bg="black")
        grade.place(x=400, y = 40)

    def gen_grade(self):
        """This Funtion for select a list of member that get grade ...."""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("400x450")
        self.gen.resizable(0, 0)

        self.tk.Label(self.gen, text="List Grade of "+self.name_sub, fg="White", bg="black").place(x=160, y = 5)
        
        button_A = self.tk.Button(self.gen, text='A', command=self.list_a)
        button_A.place(x = 180, y = 60)

        button_Bp = self.tk.Button(self.gen, text='B+', command=self.list_bp)
        button_Bp.place(x = 180, y = 100)

        button_B = self.tk.Button(self.gen, text='B', command=self.list_b)
        button_B.place(x = 180, y = 140)

        button_Cp = self.tk.Button(self.gen, text='C+', command=self.list_cp)
        button_Cp.place(x = 180, y = 180)

        button_C = self.tk.Button(self.gen, text='C', command=self.list_c)
        button_C.place(x = 180, y = 220)

        button_Dp = self.tk.Button(self.gen, text='D+', command=self.list_dp)
        button_Dp.place(x = 180, y = 260)

        button_D = self.tk.Button(self.gen, text='D', command=self.list_d)
        button_D.place(x = 180, y = 300)

        button_F = self.tk.Button(self.gen, text='F', command=self.list_f)
        button_F.place(x = 180, y = 340)

    def calculate_group(self):
        """This Funtion for calculate score in Group score mode"""
        self.data_list.sort(reverse = True)
        num = 1
        spc = 30
        xbar = sum(self.check_score)/len(self.check_score)
        total = 0
        for i in self.check_score:
            total += (i - xbar)**2
        sd = float('%.2f' % (total/len(self.check_score))**0.5)
        self.get_a = []
        self.get_bp = []
        self.get_b = []
        self.get_cp = []
        self.get_c = []
        self.get_dp = []
        self.get_d = []
        self.get_f = []
        cut_a = sd*self.a_sd + xbar
        cut_bp = sd*self.bp_sd + xbar
        cut_b = sd*self.b_sd + xbar
        cut_cp = sd*self.cp_sd + xbar
        cut_c = sd*self.c_sd + xbar
        cut_dp = sd*self.dp_sd + xbar
        cut_d = sd*self.d_sd + xbar
        for i in self.data_list:
            if i[0] > cut_a:
                self.get_a.append(i)
            elif i[0] > cut_bp:
                self.get_bp.append(i)
            elif i[0] > cut_b:
                self.get_b.append(i)
            elif i[0] > cut_cp:
                self.get_cp.append(i)
            elif i[0] > cut_c:
                self.get_c.append(i)
            elif i[0] > cut_dp:
                self.get_dp.append(i)
            elif i[0] > cut_d:
                self.get_d.append(i)
            else:
                self.get_f.append(i)
         

    def list_a(self):
        """        Funtion for show resault a member that get grade a"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade A", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_a:
            spc += 20
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)
            
        
    def list_bp(self):
        """        Funtion for show resault a member that get grade b+"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade B+", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_bp:
            spc += 20
            num += 1
            self.tk.Label(self.gen, text="No."+ str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)
            
        
        
    def list_b(self):
        """       Funtion for show resault a member that get grade b"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade B", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_b:
            spc += 20
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)

    def list_cp(self):
        """       Funtion for show resault a member that get grade c+"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade C+", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_cp:
            num += 1
            spc += 20
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)
    def list_c(self):
        """       Funtion for show resault a member that get grade c"""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade C", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_c:
            spc += 20
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)

    def list_dp(self):
        """       Funtion for show resault a member that get grade d+ """
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade D+", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_dp:
            num += 1
            spc += 20
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)

    def list_d(self):
        """       Funtion for show resault a member that get grade d """
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="No."+str(num)+"List name of Grade D", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_d:
            num += 1
            spc += 20
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)
    def list_f(self):
        """        Funtion for show resault a member that get grade f """
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        self.data_list.sort(reverse = True)
        spc = 30
        num = 0
        self.calculate_group()
        self.tk.Label(self.gen, text="List name of Grade F", fg="White", bg="black").place(x=180, y = 10)
        for i in self.get_f:
            num += 1
            spc += 20
            self.tk.Label(self.gen, text="No."+str(num)+" "+i[1] + " Score is " +str(i[0]), fg="White", bg="black").place(x=10, y = spc)
            
    def make_rule(self):
        """This Funtion for get data for calculate in Group Score mode"""
        self.new = self.tk.Toplevel()
        self.new.title("Make Rule")
        self.new.geometry("500x300")
        self.new.resizable(0, 0)
        self.new.focus()

        frame = self.tk.Frame(self.new)
        frame.pack()

        self.tk.Message(frame, text="Subject name : ", width=300).grid(row=0, column=0)
        self.sub = self.tk.Entry(frame, width=10)
        self.sub.grid(row=0, column=1, padx=5, pady=5)
        self.sub.focus()
        self.sub.bind("<Return>", self.add_rule)

        self.tk.Message(frame, text="Grade A SD:", width=100).grid(row=2, column=0)
        self.sd_A = self.tk.Entry(frame, width=5)
        self.sd_A.grid(row=2, column=1)

        self.tk.Message(frame, text="Grade B+ SD:", width=100).grid(row=4, column=0)
        self.sd_Bp = self.tk.Entry(frame, width=5)
        self.sd_Bp.grid(row=4, column=1)

        self.tk.Message(frame, text="Grade B SD:", width=100).grid(row=6, column=0)
        self.sd_B = self.tk.Entry(frame, width=5)
        self.sd_B.grid(row=6, column=1)

        self.tk.Message(frame, text="Grade C+ SD:", width=100).grid(row=8, column=0)
        self.sd_Cp = self.tk.Entry(frame, width=5)
        self.sd_Cp.grid(row=8, column=1)

        self.tk.Message(frame, text="Grade C SD:", width=100).grid(row=10, column=0)
        self.sd_C = self.tk.Entry(frame, width=5)
        self.sd_C.grid(row=10, column=1)

        self.tk.Message(frame, text="Grade D+ SD:", width=100).grid(row=12, column=0)
        self.sd_Dp = self.tk.Entry(frame, width=5)
        self.sd_Dp.grid(row=12, column=1)

        self.tk.Message(frame, text="Grade D SD:", width=100).grid(row=14, column=0)
        self.sd_D = self.tk.Entry(frame, width=5)
        self.sd_D.grid(row=14, column=1)

        button_ok = self.tk.Button(frame, text='Add', command=self.add_rule)
        button_ok.grid(row=16, column=1)
        buttun_can = self.tk.Button(frame, text='Finish', command=self.new.destroy).grid(row=16, column =2)

    def add_rule(self):
        '''
        This Funtion for get input and save it for use
        '''
        self.name_sub = str(self.sub.get())
        self.a_sd = float(self.sd_A.get())
        self.bp_sd = float(self.sd_Bp.get())
        self.b_sd = float(self.sd_B.get())
        self.cp_sd = float(self.sd_Cp.get())
        self.c_sd = float(self.sd_C.get())
        self.dp_sd = float(self.sd_Dp.get())
        self.d_sd = float(self.sd_D.get())
        self.check_mode = 1
        
        self.tk.messagebox.showinfo(message="Add Completed")
        self.reset_rule("")
    def add_stu(self):
        '''
        This Funtion is UI of Student input
        '''
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
      
        self.score.bind("<Return>", self.add_list)

        button_ok = self.tk.Button(frame, text='Add', command=self.add_list)
        button_ok.grid(row=7, column=1)
        buttun_can = self.tk.Button(frame, text='Finish', command=self.new.destroy).grid(row=7, column=2)

    def reset_rule(self, text):
        '''
        Reset a Entrybox in rule mode
        '''
        self.sub.delete(0, len(self.sub.get()))
        self.sub.insert(0,text)
        self.sd_A.delete(0, len(self.sd_A.get()))
        self.sd_A.insert(0,text)
        self.sd_Bp.delete(0, len(self.sd_Bp.get()))
        self.sd_Bp.insert(0,text)
        self.sd_B.delete(0, len(self.sd_B.get()))
        self.sd_B.insert(0,text)
        self.sd_Cp.delete(0, len(self.sd_Cp.get()))
        self.sd_Cp.insert(0,text)
        self.sd_C.delete(0, len(self.sd_C.get()))
        self.sd_C.insert(0,text)
        self.sd_Dp.delete(0, len(self.sd_Dp.get()))
        self.sd_Dp.insert(0,text)
        self.sd_D.delete(0, len(self.sd_D.get()))
        self.sd_D.insert(0,text)
    def reset_stu(self, text):
        '''
        Reset a Entrybox in student add mode
        '''
        self.n.delete(0, len(self.n.get()))
        self.n.insert(0,text)
        self.s.delete(0, len(self.s.get()))
        self.s.insert(0,text)
        self.score.delete(0, len(self.score.get()))
        self.score.insert(0,text)

    def add_list(self, event=""):
        self.check_score.append(int(self.score.get()))
        self.data_list.append([int(self.score.get()), self.n.get()+" "+self.s.get()])
        self.listbox.insert("end", self.n.get()+" "+self.s.get())
        self.tk.messagebox.showinfo(message="Add Completed")
        self.new.focus()
        self.n.focus()
        self.reset_stu("")
    
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

 
    def get_subject(self):
        """ Get all subjects """
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")
