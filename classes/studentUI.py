from classes.subject import *
from classes.gradebar import *
from classes.gradebar import *

class StudentUI:

    def __init__(self, parent):
        self.SUBJECT_LIST = []
        self.mode = parent.mode
        self.parent = parent
        self.tk = parent.tk
        self.root = parent.root
        self.STD_LIST = {0: "test"}
        self.initUI()
        self.lb_sel_i = -1
        #self.root.mainloop()
        
    def initUI(self):
        self.root.geometry(self.parent.find_center(600, 500))
        self.root.resizable(0, 0)
        self.root.title(' "Get A" : Student Mode')

        bg_image = self.tk.PhotoImage(file= 'classes/Bg_2.gif')
        self.background = self.tk.Label(self.root,image = bg_image)
        self.background.place(x=0, y=0)
        
        frame_subject_image = self.tk.PhotoImage(file= 'classes/frame_edit.gif')
        self.frame_subject = self.tk.Label(self.background, image=frame_subject_image)
        self.frame_subject.place(width=250, height=200, x=35, y=30)

        frame_edit_image = self.tk.PhotoImage(file= 'classes/frame_edit.gif')
        self.frame_edit = self.tk.Label(self.background, image=frame_edit_image)
        self.frame_edit.place(width=250, height=200, x=310, y=30)

        frame_result_image = self.tk.PhotoImage(file= 'classes/frame_result.gif')
        self.frame_result = self.tk.Label(self.background, image=frame_result_image)
        self.frame_result.place(width=530, height=190, x=35, y=240)
        
        bar_image = self.tk.PhotoImage(file= 'classes/gradebar.gif')
        self.bar_frame = self.tk.Label(self.frame_result, image=bar_image)
        self.bar_frame.place(width=30, height=130, x=25, y=35)
        self.progress = Progressbar(self.frame_result, 20, 130, 100)
        self.progress.update(0)

        self.lb_frame = self.tk.Frame(self.frame_subject)
        self.lb_frame.place(x=10, y=20)
        self.listbox = self.tk.Listbox(self.lb_frame, width=18, height = 9, bg='#fcf179')
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        scrollbar = self.tk.Scrollbar(self.lb_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.listbox.yview)
        
        new_sbj_image = self.tk.PhotoImage(file= 'classes/new_sbj_btn.gif')
        new = self.tk.Button(self.frame_subject, image=new_sbj_image,bg='#0e451f',relief='flat',command = self.new_subject_ui)
        new.place(x=145, y=30)

        del_btn_image = self.tk.PhotoImage(file= 'classes/del_btn.gif')
        b = self.tk.Button(self.frame_subject,image=del_btn_image, bg='#0e451f', relief='flat' , command=self.del_sbj)
        b.place(x=145, y=120)

        edit_frame_image = self.tk.PhotoImage(file= 'classes/edit_frame.gif')
        self.edit_score = self.tk.Label(self.frame_edit, bg='#0e451f',image = edit_frame_image,width=148, height=178)
        self.edit_score.place(x=10, y=5)

        self.e_s_exam_mid = self.tk.Entry(self.edit_score, width=3)
        self.e_s_exam_mid.place(x=100,y=55)
        self.e_s_exam_final = self.tk.Entry(self.edit_score, width=3)
        self.e_s_exam_final.place(x=100,y=80)
        self.e_s_project = self.tk.Entry(self.edit_score, width=3)
        self.e_s_project.place(x=100,y=102)
        self.e_s_hw = self.tk.Entry(self.edit_score, width=3)
        self.e_s_hw.place(x=100,y=126)
        self.e_s_other = self.tk.Entry(self.edit_score, width=3)
        self.e_s_other.place(x=100,y=148)
        self.e_s_other.bind("<Return>", self.s_edit)

        edit_btn_image = self.tk.PhotoImage(file= 'classes/edit_btn.gif')
        self.edit_btn = self.tk.Button(self.frame_edit,image=edit_btn_image,bg='#0e451f',relief='flat', command=self.s_edit)
        self.edit_btn.place(x=160, y=15)

        gpa_btn_image = self.tk.PhotoImage(file= 'classes/gpa_btn.gif')
        self.gpa_btn = self.tk.Button(self.frame_edit,image=gpa_btn_image,bg='#0e451f',relief='flat' ,command=self.get_gpa)
        self.gpa_btn.place(x=160, y=80)
        self.gpa_label = self.tk.Label(self.frame_edit, text='' ,width=7, height=2, bg='#ff99cc', relief='ridge')
        self.gpa_label.place(x=173,y=147)

        grade_frame_image = self.tk.PhotoImage(file= 'classes/grade_frame.gif')
        self.grade_frame = self.tk.Label(self.frame_result, image=grade_frame_image, bg='#0e451f')
        self.grade_frame.place(x=100, y=15)

        hint_image = self.tk.PhotoImage(file= 'classes/hint.gif')
        self.hint_frame = self.tk.Label(self.frame_result, image=hint_image, bg='#0e451f')
        self.hint_frame.place(x=300, y=15)

        back_btn = self.tk.PhotoImage(file= 'classes/std_back.gif')
        self.back_btn = self.tk.Button(self.background,image=back_btn,bg='#0e451f',relief='flat', command=self.parent.back)
        self.back_btn.place(x=35, y=432)
        
        self.root.mainloop()
        
    def del_sbj(self):
        index = int(self.listbox.curselection()[0])
        del(self.SUBJECT_LIST[index])
        self.listbox.delete("anchor")
    def s_edit(self):
        # index = int(self.listbox.curselection()[0])
        index = self.lb_sel_i
        if index == -1:
            return False
        print ('index',index)
        self.SUBJECT_LIST[index].s_exam_mid = self.e_s_exam_mid.get()
        self.SUBJECT_LIST[index].s_final = self.e_s_exam_final.get()
        self.SUBJECT_LIST[index].s_project = self.e_s_project.get()
        self.SUBJECT_LIST[index].s_hw = self.e_s_hw.get()
        self.SUBJECT_LIST[index].s_other = self.e_s_other.get()
        self.calculate()
        self.hint()

    def get_gpa(self):
        lis_score_weight = []
        weight_all = 0
        for subject in self.SUBJECT_LIST:
            print(subject.weight, subject.grade)
            lis_score_weight.append(int(subject.weight)*subject.grade)
            weight_all += int(subject.weight)
        print (sum(lis_score_weight)/weight_all)
        self.gpa_label.config(text='{:.2f}'.format(sum(lis_score_weight)/weight_all))

    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("320x250")
        self.top.resizable(0, 0)
        self.top.focus()

        add_sbj_bg = self.tk.PhotoImage(file='classes/add_sbj.gif')
        frame = self.tk.Label(self.top, image=add_sbj_bg)
        frame.pack()

        self.e = self.tk.Entry(frame, width=11)
        self.e.place(x=130, y=27)
        self.e.focus()
        
        self.weight = self.tk.Entry(frame, width=3)
        self.weight.place(x=275, y=27)

        
        self.s_exam_mid = self.tk.Entry(frame, width=5)
        self.s_exam_mid.place(x=130, y=93)
        self.b_exam_mid = self.tk.Entry(frame, width=5)
        self.b_exam_mid.place(x=202, y=93)


        self.s_exam_final = self.tk.Entry(frame, width=5)
        self.s_exam_final.place(x=130, y=118)
        self.b_exam_final = self.tk.Entry(frame, width=5)
        self.b_exam_final.place(x=202, y=118)


        self.s_project = self.tk.Entry(frame, width=5)
        self.s_project.place(x=130, y=143)
        self.b_project = self.tk.Entry(frame, width=5)
        self.b_project.place(x=202, y=143)


        self.s_hw = self.tk.Entry(frame, width=5)
        self.s_hw.place(x=130, y=168)
        self.b_hw = self.tk.Entry(frame, width=5)
        self.b_hw.place(x=202, y=168)


        self.s_other = self.tk.Entry(frame, width=5)
        self.s_other.place(x=130, y=193)
        self.b_other = self.tk.Entry(frame, width=5)
        self.b_other.place(x=202, y=193)
        self.b_other.bind("<Return>", self.add_subject)
        
        button_ok = self.tk.Button(frame, text='Add',fg='white',bg='#0e451f', command=self.add_subject)
        button_ok.place(x=258, y=170)
        buttun_clo = self.tk.Button(frame, text='Finish',fg='white',bg='#0e451f', command=self.top.destroy)
        buttun_clo.place(x=253, y= 205)
        self.top.mainloop()

    def set_e_text(self, text):
        """ Set Entry Text """
        self.e.delete(0, len(self.e.get()))
        self.e.insert(0,text)
        self.weight.delete(0, len(self.weight.get()))
        self.weight.insert(0,text)
        self.s_exam_mid.delete(0, len(self.s_exam_mid.get()))
        self.s_exam_mid.insert(0,text)
        self.b_exam_mid.delete(0, len(self.b_exam_mid.get()))
        self.b_exam_mid.insert(0,text)
        self.s_exam_final.delete(0, len(self.s_exam_final.get()))
        self.s_exam_final.insert(0,text)
        self.b_exam_final.delete(0, len(self.b_exam_final.get()))
        self.b_exam_final.insert(0,text)
        self.s_project.delete(0, len(self.s_project.get()))
        self.s_project.insert(0,text)
        self.b_project.delete(0, len(self.b_project.get()))
        self.b_project.insert(0,text)
        self.s_hw.delete(0, len(self.s_hw.get()))
        self.s_hw.insert(0,text)
        self.b_hw.delete(0, len(self.b_hw.get()))
        self.b_hw.insert(0,text)
        self.s_other.delete(0, len(self.s_other.get()))
        self.s_other.insert(0,text)
        self.b_other.delete(0, len(self.b_other.get()))
        self.b_other.insert(0,text)
        return True

    def get_subject(self):
        """ Get all subjects """
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
            print (i, self.SUBJECT_LIST[i].s_exam_mid)
        print ("------------------------------------")

    def calculate(self):
        '''
        x.calculate_grade()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Calculate what grade do you get

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        '''
        grade = 0
        i = self.lb_sel_i
        self.total_score = int(self.SUBJECT_LIST[i].s_exam_mid) + int(self.SUBJECT_LIST[i].s_final) + int(self.SUBJECT_LIST[i].s_project) \
                         + int(self.SUBJECT_LIST[i].s_hw) + int(self.SUBJECT_LIST[i].s_other)
        self.total_score = int(self.total_score)
        
        if self.total_score >= 80:
            grade += 4.0
            grade_img = self.tk.PhotoImage(file= 'classes/a.gif')
        elif self.total_score >= 75:
            grade += 3.5
            grade_img = self.tk.PhotoImage(file= 'classes/b+.gif')
        elif self.total_score >= 70:
            grade += 3.0
            grade_img = self.tk.PhotoImage(file= 'classes/b.gif')
        elif self.total_score >= 65:
            grade += 2.5
            grade_img = self.tk.PhotoImage(file= 'classes/c+.gif')
        elif self.total_score >= 60:
            grade += 2.0
            grade_img = self.tk.PhotoImage(file= 'classes/c.gif')
        elif self.total_score >= 55:
            grade += 1.5
            grade_img = self.tk.PhotoImage(file= 'classes/d+.gif')
        elif self.total_score >= 50:
            grade += 1.0
            grade_img = self.tk.PhotoImage(file= 'classes/d.gif')
        elif self.total_score < 50:
            grade_img = self.tk.PhotoImage(file= 'classes/f.gif')

        self.grade_frame.config(image=grade_img)
        self.grade_frame.image = grade_img 
        #self.tk.Label(self.grade_frame, text='Total Score =  '+str(self.total_score)).place(x=25, y=120)

        self.progress.update(self.total_score)

        self.SUBJECT_LIST[i].grade = float(grade)
        
    def hint(self):
        '''
        x.hint()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Find What part of score that you must do  for make your grade better

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        '''
        cal_hint = []
        i = self.lb_sel_i
        if int(self.SUBJECT_LIST[i].s_exam_mid) == 0 :
            cal_hint.append([((int(self.SUBJECT_LIST[i].m_exam_mid) - int(self.SUBJECT_LIST[i].s_exam_mid))*(int(self.SUBJECT_LIST[i].m_exam_mid) / 100)), ("Midterm")])
        if int(self.SUBJECT_LIST[i].s_final) == 0:
            cal_hint.append([( (int(self.SUBJECT_LIST[i].m_final) - int(self.SUBJECT_LIST[i].s_final)) * (int(self.SUBJECT_LIST[i].m_final) / 100) ), ("Final")])
            
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_project) - int(self.SUBJECT_LIST[i].s_project))*(int(self.SUBJECT_LIST[i].m_project) / 100)), ("Project")])
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_hw) - int(self.SUBJECT_LIST[i].s_hw))*(int(self.SUBJECT_LIST[i].m_hw)/ 100)), ("Homework")])
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_other) - int(self.SUBJECT_LIST[i].s_other))*(int(self.SUBJECT_LIST[i].m_other) / 100)), ("Other")])
        cal_hint.sort(reverse = True)
        number = 1
        each_y = 43
        self.tk.Label(self.hint_frame, width=25, height=6, bg='#0e451f').place(x=10,y=45)
        
        for i in cal_hint:
            self.tk.Label(self.hint_frame, text="No."+str(number)+"   "+i[1], bg='#0e451f',fg = 'white',font=('times',10)).place(x=50,y=each_y)
            number += 1
            each_y += 20

    def add_subject(self, event=""):
        """ New subject """

        self.name = self.e.get()
        if self.name == "":
            self.tk.messagebox.showinfo(message="Please enter subject name.", title="Error !")
            # self.top.destroy()
            # self.new_subject()
            self.e.focus()
            return False

        # Add subject to listbox
        self.listbox.insert("end", self.name)
        
        # New object subject
        sbj = Subject(self)
        
        sbj.s_exam_mid = self.s_exam_mid.get()
        sbj.s_final = self.s_exam_final.get()
        sbj.s_project = self.s_project.get()
        sbj.s_hw = self.s_hw.get()
        sbj.s_other = self.s_other.get()
        
        sbj.m_exam_mid = self.b_exam_mid.get()
        sbj.m_final = self.b_exam_final.get()
        sbj.m_project = self.b_project.get()
        sbj.m_hw = self.b_hw.get()
        sbj.m_other = self.b_other.get()
        sbj.weight = self.weight.get()
        

        self.tk.messagebox.showinfo(message="Success - " + str(self.name), title="Success")
        self.lb_sel_i = self.listbox.size() - 1
        print (self.lb_sel_i)
        self.SUBJECT_LIST.append(sbj)
        self.calculate()
        self.hint()
        self.set_e_text("")
        self.get_subject()
        self.e.focus()

    def onselect(self, event=""):
        # Note here that Tkinter passes an event object to onselect()
        w = event.widget
        index = int(w.curselection()[0])
        self.lb_sel_i = index
        value = w.get(index)
        self.e_s_exam_mid.delete(0, len(self.e_s_exam_mid.get()))
        self.e_s_exam_mid.insert(0, self.SUBJECT_LIST[index].s_exam_mid)

        self.e_s_exam_final.delete(0, len(self.e_s_exam_final.get()))
        self.e_s_exam_final.insert(0, self.SUBJECT_LIST[index].s_final)

        self.e_s_project.delete(0, len(self.e_s_project.get()))
        self.e_s_project.insert(0, self.SUBJECT_LIST[index].s_project)

        self.e_s_hw.delete(0, len(self.e_s_hw.get()))
        self.e_s_hw.insert(0, self.SUBJECT_LIST[index].s_hw)

        self.e_s_other.delete(0, len(self.e_s_other.get()))
        self.e_s_other.insert(0, self.SUBJECT_LIST[index].s_other)

        self.calculate()
        self.hint()
        
        print ('You selected item %d: "%s"' % (index, value))
