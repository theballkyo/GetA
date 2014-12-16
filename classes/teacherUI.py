class TeacherUI():

    def __init__(self, parent):
        self.count_id = 0
        self.SUBJECT_LIST = []
        self.STD_LIST = {}
        self.tk = parent.tk
        self.root = parent.root
        self.parent = parent
        self.data_list = []
        self.data_rule = []
        self.check_mode = 0
        self.check_score = []
        self.initUI()
        
    def initUI(self):
        """       UI window       make rule - for calculate grade in base on group score mode
        if you dont want to use make rule mode just add student and click generate"""
        self.root.geometry(self.parent.find_center(500, 620))
        self.root.resizable(0, 0)
        self.root.title(' "Get A" : Teacher mode')
        
        bg_image = self.tk.PhotoImage(file= 'imgs/TeacherUI.gif')
        self.frame_subject = self.tk.Label(self.root, image=bg_image)
        self.frame_subject.place(x=0, y=0)

        set_sd_btn = self.tk.PhotoImage(file= 'imgs/set_sd.gif')
        self.btn_std = self.tk.Button(self.frame_subject,bg='white', relief='flat',image=set_sd_btn, command=self.make_rule)
        self.btn_std.place(x=70, y=79)

        reset_sd_btn = self.tk.PhotoImage(file= 'imgs/reset_sd.gif')
        self.reset_btn = self.tk.Button(self.frame_subject, bg= 'white', relief='flat',image=reset_sd_btn, command=self.mode_reset)
        self.reset_btn.place(x=78, y=155)

        add_std_btn = self.tk.PhotoImage(file= 'imgs/tch_add_std.gif')
        self.btn_std = self.tk.Button(self.frame_subject,bg='white', relief='flat',image=add_std_btn, command=self.add_stu)
        self.btn_std.place(x=330, y=77)

        self.lb_frame = self.tk.Frame(self.frame_subject)
        self.lb_frame.place(x=200, y=82)
        self.listbox = self.tk.Listbox(self.lb_frame, width = 18, height=20)
        self.listbox.pack(side='left', fill='both')

        scrollbar = self.tk.Scrollbar(self.lb_frame)
        scrollbar.pack(side='right', fill='y')
        scrollbar.config(command=self.listbox.yview)

        del_btn = self.tk.PhotoImage(file= 'imgs/tch_del_btn.gif')
        self.btn_del = self.tk.Button(self.frame_subject, bg='white', relief='flat',image=del_btn, command=self.del_std)
        self.btn_del.place(x=200, y=410)

        gen_btn = self.tk.PhotoImage(file= 'imgs/gen_btn.gif')
        self.btn_cal = self.tk.Button(self.frame_subject, bg='white', relief='flat',image=gen_btn, command=self.select_gen)
        self.btn_cal.place(x=175, y=481)

        back_btn = self.tk.PhotoImage(file= 'imgs/tch_back.gif')
        self.back_btn = self.tk.Button(self.frame_subject, bg='white', relief='flat',image=back_btn, command=self.parent.back)
        self.back_btn.place(x=70, y=493)
        self.root.mainloop()

    def mode_reset(self):
        '''reset mode'''
        self.check_mode = 0
        self.get_a = []
        self.get_bp = []
        self.get_b = []
        self.get_cp = []
        self.get_c = []
        self.get_dp = []
        self.get_d = []
        self.get_f = []
        
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
        self.gen = self.tk.Toplevel()
        self.gen.title("Result")
        self.gen.geometry("450x600")
        self.gen.resizable(0, 0)
        # self.data_list.sort(reverse = True)

        score_board_bg = self.tk.PhotoImage(file='imgs/score_board.gif')
        self.sb = self.tk.Label(self.gen, image=score_board_bg)
        self.sb.pack()

        num = 1
        spc = 120
        for j in sorted(self.data_list, reverse=True):
            self.tk.Label(self.sb, text=str(num), fg="White",bg="black").place(x=60, y = spc)
            self.tk.Label(self.sb, text=str(j[1]), fg="White", bg="black").place(x=120, y = spc)
            self.tk.Label(self.sb, text=str(j[0]), fg="White", bg="black").place(x=290, y = spc)

            if j[0] >= 80:
                self.tk.Label(self.sb, text="A", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 75:
                self.tk.Label(self.sb, text="B+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 70:
                self.tk.Label(self.sb, text="B", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 65:
                self.tk.Label(self.sb, text="C+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 60:
                self.tk.Label(self.sb, text="C", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 55:
                self.tk.Label(self.sb, text="D+", fg="White", bg="black").place(x=400, y = spc)
            elif j[0] >= 50:
                self.tk.Label(self.sb, text="D", fg="White", bg="black").place(x=400, y = spc)
            else:
                self.tk.Label(self.sb, text="F", fg="White", bg="black").place(x=400, y = spc)
            num += 1
            spc += 20
        self.gen.mainloop()

    def gen_grade(self):
        """This Funtion for select a list of member that get grade ...."""
        self.gen = self.tk.Toplevel(bg = "Black")
        self.gen.title("Result")
        self.gen.geometry("400x100")
        self.gen.resizable(0, 0)
        self.tk.Label(self.gen, text="Student's Grade of "+self.name_sub, fg="White", bg="black", font=('times',18)).pack(side='top')
        
        button_A = self.tk.Button(self.gen, text='A',width=5, bg="green", command=self.list_a)
        button_A.place(x = 40, y = 50)

        button_Bp = self.tk.Button(self.gen, text='B+',width=5,bg="green yellow", command=self.list_bp)
        button_Bp.place(x = 80, y = 50)

        button_B = self.tk.Button(self.gen, text='B',width=5, bg="yellow", command=self.list_b)
        button_B.place(x = 120, y = 50)

        button_Cp = self.tk.Button(self.gen, text='C+',width=5, bg='gold', command=self.list_cp)
        button_Cp.place(x = 160, y = 50)

        button_C = self.tk.Button(self.gen, text='C',width=5, bg='dark orange', command=self.list_c)
        button_C.place(x = 200, y = 50)

        button_Dp = self.tk.Button(self.gen, text='D+',width=5, bg='red', command=self.list_dp)
        button_Dp.place(x = 240, y = 50)

        button_D = self.tk.Button(self.gen, text='D',width=5, bg='brown', command=self.list_d)
        button_D.place(x = 280, y = 50)

        button_F = self.tk.Button(self.gen, text='F',width=5, bg='dark red', command=self.list_f)
        button_F.place(x = 320, y = 50)

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
        self.tk.Label(self.gen, text="Student who get Grade A",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_a:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "   Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')
            
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
        self.tk.Label(self.gen, text="Student who get Grade B+",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_bp:
            num += 1
            self.tk.Label(self.gen, text="No."+ str(num)+"     "+i[1] + "   Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')
            
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
        self.tk.Label(self.gen, text="Student who get Grade B",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_b:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "    Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')

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
        self.tk.Label(self.gen, text="Student who get Grade C+",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_cp:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "     Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')

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
        self.tk.Label(self.gen, text="Student who get Grade C",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_c:
            spc += 20
            self.tk.Label(self.gen, text="No."+str(num)+"       "+i[1] + "     Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')

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
        self.tk.Label(self.gen, text="Student who get Grade D+",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_dp:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "     Score :   " +str(i[0]), fg="White", bg="black").pack(side='top')

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
        self.tk.Label(self.gen, text="Student who get Grade D",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_d:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "     Score  :   " +str(i[0]), fg="White", bg="black").pack(side='top')

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
        self.tk.Label(self.gen, text="Student who get Grade F",font=('times',18), fg="White", bg="black").pack(side='top')
        for i in self.get_f:
            num += 1
            self.tk.Label(self.gen, text="No."+str(num)+"      "+i[1] + "     Score  :   " +str(i[0]), fg="White", bg="black").pack(side='top')
            
    def make_rule(self):
        """This Funtion for get data for calculate in Group Score mode"""
        self.new = self.tk.Toplevel()
        self.new.title("Set SD")
        self.new.geometry("205x300")
        self.new.resizable(0, 0)
        self.new.focus()

        bg_make_rule = self.tk.PhotoImage(file= 'imgs/make_rule.gif')
        frame = self.tk.Label(self.new, image = bg_make_rule)
        frame.pack()

        self.sub = self.tk.Entry(frame, width=11)
        self.sub.place(x=125, y=35)
        self.sub.focus()

        self.sd_A = self.tk.Entry(frame, width=5)
        self.sd_A.place(x=100, y=75)

        self.sd_Bp = self.tk.Entry(frame, width=5)
        self.sd_Bp.place(x=100, y=100)

        self.sd_B = self.tk.Entry(frame, width=5)
        self.sd_B.place(x=100, y=125)

        self.sd_Cp = self.tk.Entry(frame, width=5)
        self.sd_Cp.place(x=100, y=150)

        self.sd_C = self.tk.Entry(frame, width=5)
        self.sd_C.place(x=100, y=175)

        self.sd_Dp = self.tk.Entry(frame, width=5)
        self.sd_Dp.place(x=100, y=200)

        self.sd_D = self.tk.Entry(frame, width=5)
        self.sd_D.place(x=100, y=225)
        self.sd_D.bind("<Return>", self.add_rule)

        button_ok = self.tk.Button(frame, text='Add',bg='#fcfbcf', command=self.add_rule)
        button_ok.place(x=50, y=260)
        button_can = self.tk.Button(frame, text='Cancle',bg='#fcfbcf', command=self.new.destroy)
        button_can.place(x=120, y=260)

        self.new.mainloop()
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
        self.new.destroy()
    def add_stu(self):
        '''
        This Funtion is UI of Student input
        '''
        self.new = self.tk.Toplevel()
        self.new.title("Data new student")
        self.new.geometry("300x219")
        self.new.resizable(0, 0)
        self.new.focus()

        add_stu_bg = self.tk.PhotoImage(file='imgs/add_stu.gif')
        frame = self.tk.Label(self.new, image=add_stu_bg)
        frame.pack()

        self.n = self.tk.Entry(frame, width=20)
        self.n.place(x=160, y=58)
        self.n.focus()

        self.s = self.tk.Entry(frame, width=20)
        self.s.place(x=160, y=95)

        
        self.score = self.tk.Entry(frame, width=8)
        self.score.place(x=190, y=131)
      
        self.score.bind("<Return>", self.add_list)

        button_ok = self.tk.Button(frame, text='Add',bg='#fcfbcf',width=8, command=self.add_list)
        button_ok.place(x=70 ,y=175)
        button_can = self.tk.Button(frame, text='Finish',bg='#fcfbcf',width=8, command=self.new.destroy)
        button_can.place(x=185 ,y=175)
        self.new.mainloop()
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
        self.data_list.append([int(self.score.get()), self.n.get()+"  "+self.s.get()])
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
