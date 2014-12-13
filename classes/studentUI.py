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

        self.progress = Progressbar(self.frame_result, 20, 200, 100)
        self.progress.update(0)
        
        self.listbox = self.tk.Listbox(self.frame_subject, width=28, height = 11)
        self.listbox.place(x=30, y=40)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        new = self.tk.Button(self.frame_subject, text='New Subject',
                            command = self.new_subject_ui)
        new.grid(row=0, column=0)

        b = self.tk.Button(self.frame_subject, text="Delete", command=self.del_sbj)
        b.place(x=220, y=200)
        
        self.edit_score = self.tk.LabelFrame(self.frame_edit, text="Edit Score", padx=5, pady=5)
        self.edit_score.place(x=30, y=30)

        self.tk.Message(self.edit_score, text="Midterm :", width=80).grid(row=0, column=0)
        self.e_s_exam_mid = self.tk.Entry(self.edit_score, width=5)
        self.e_s_exam_mid.grid(row=0, column=1)
        self.tk.Message(self.edit_score, text="Final :", width=50).grid(row=1, column=0)
        self.e_s_exam_final = self.tk.Entry(self.edit_score, width=5)
        self.e_s_exam_final.grid(row=1, column=1)
        self.tk.Message(self.edit_score, text="Project :", width=50).grid(row=2, column=0)
        self.e_s_project = self.tk.Entry(self.edit_score, width=5)
        self.e_s_project.grid(row=2, column=1)
        self.tk.Message(self.edit_score, text="Homework :", width=80).grid(row=3, column=0)
        self.e_s_hw = self.tk.Entry(self.edit_score, width=5)
        self.e_s_hw.grid(row=3, column=1)
        self.tk.Message(self.edit_score, text="Other :", width=50).grid(row=4, column=0)
        self.e_s_other = self.tk.Entry(self.edit_score, width=5)
        self.e_s_other.grid(row=4, column=1)

        self.edit_btn = self.tk.Button(self.edit_score, text="Edit", command=self.s_edit)
        self.edit_btn.grid(row=5, column=1)

        self.grade_frame = self.tk.Frame(self.frame_result, width=150, height=150, relief='raised')
        self.tk.Label(self.grade_frame, text=' Your Grade is : ').place(x=75, y=10, width=300, anchor='n')
        self.grade_frame.place(x=110, y=50)

        self.hint_frame = self.tk.LabelFrame(self.frame_result, text='Hint!!!', width=270, height=215)
        self.hint_frame.place(x=310, y=15)
        self.tk.Label(self.hint_frame, text="The Sequence of important score is").place(x=130, y=10, anchor='n')
        
    def del_sbj(self):
        index = int(self.listbox.curselection()[0]) - 1
        del(self.SUBJECT_LIST[index])
        self.listbox.delete("anchor")
    def s_edit(self):
        # index = int(self.listbox.curselection()[0])
        index = self.lb_sel_i
        if index == -1:
            return False
        print (index)
        self.SUBJECT_LIST[index].s_exam_mid = self.e_s_exam_mid.get()
        self.SUBJECT_LIST[index].s_final = self.e_s_exam_final.get()
        self.SUBJECT_LIST[index].s_project = self.e_s_project.get()
        self.SUBJECT_LIST[index].s_hw = self.e_s_hw.get()
        self.SUBJECT_LIST[index].s_other = self.e_s_other.get()
        self.calculate()
        self.hint()

    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("300x260")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.tk.Message(frame, text="Subject Name : ").grid(row=0, column=0)
        self.e = self.tk.Entry(frame, width=10)
        self.e.grid(row=0, column=1, padx=5, pady=5)
        self.e.focus()
        self.e.bind("<Return>", self.add_subject)
        
        self.tk.Message(frame, text="Weight :", width=50).grid(row=0, column=2)
        self.weight = self.tk.Entry(frame, width=3)
        self.weight.grid(row=0, column=3, padx=5, pady=5)

        self.tk.Message(frame, text="Score", width=50).grid(row=1, column=1)
        self.tk.Message(frame, text="Max", width=50).grid(row=1, column=2)
        
        self.tk.Message(frame, text="Midterm :", width=80).grid(row=2, column=0)
        self.s_exam_mid = self.tk.Entry(frame, width=5)
        self.s_exam_mid.grid(row=2, column=1)
        self.b_exam_mid = self.tk.Entry(frame, width=5)
        self.b_exam_mid.grid(row=2, column=2)

        self.tk.Message(frame, text="Final :", width=50).grid(row=3, column=0)
        self.s_exam_final = self.tk.Entry(frame, width=5)
        self.s_exam_final.grid(row=3, column=1)
        self.b_exam_final = self.tk.Entry(frame, width=5)
        self.b_exam_final.grid(row=3, column=2)

        self.tk.Message(frame, text="Project :", width=50).grid(row=4, column=0)
        self.s_project = self.tk.Entry(frame, width=5)
        self.s_project.grid(row=4, column=1)
        self.b_project = self.tk.Entry(frame, width=5)
        self.b_project.grid(row=4, column=2)

        self.tk.Message(frame, text="Homework :", width=80).grid(row=5, column=0)
        self.s_hw = self.tk.Entry(frame, width=5)
        self.s_hw.grid(row=5, column=1)
        self.b_hw = self.tk.Entry(frame, width=5)
        self.b_hw.grid(row=5, column=2)

        self.tk.Message(frame, text="Other :", width=50).grid(row=6, column=0)
        self.s_other = self.tk.Entry(frame, width=5)
        self.s_other.grid(row=6, column=1)
        self.b_other = self.tk.Entry(frame, width=5)
        self.b_other.grid(row=6, column=2)
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=7, column=1)
        buttun_clo = self.tk.Button(frame, text='Close', command=self.top.destroy).grid(row=7, column=2)

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
        i = self.lb_sel_i
        self.total_score = int(self.SUBJECT_LIST[i].s_exam_mid) + int(self.SUBJECT_LIST[i].s_final) + int(self.SUBJECT_LIST[i].s_project) \
                         + int(self.SUBJECT_LIST[i].s_hw) + int(self.SUBJECT_LIST[i].s_other)
        self.total_score = int(self.total_score)
        if self.total_score >= 80:
            self.tk.Label(self.grade_frame, text='A', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 75:
            self.tk.Label(self.grade_frame, text='B+', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 70:
            self.tk.Label(self.grade_frame, text='B', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 65:
            self.tk.Label(self.grade_frame, text='C+', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 60:
            self.tk.Label(self.grade_frame, text='C', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 55:
            self.tk.Label(self.grade_frame, text='D+', font=('times',60)).place(x=45, y=30)
        elif self.total_score >= 50:
            self.tk.Label(self.grade_frame, text='D', font=('times',60)).place(x=45, y=30)
        elif self.total_score < 50:
            self.tk.Message(self.grade_frame, text='F', font=('times',60)).place(x=45, y=30)
            
        self.tk.Label(self.grade_frame, text='Total Score =  '+str(self.total_score)).place(x=25, y=120)

        self.progress.update(self.total_score)

    def hint(self):
        '''
        x.hint()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Find What part of score that you must do  for make your grade better

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        '''
        cal_hint = []
        i = self.lb_sel_i
        if int(self.SUBJECT_LIST[i].s_exam_mid) == 0:
            cal_hint.append([((int(self.SUBJECT_LIST[i].m_exam_mid) - int(self.SUBJECT_LIST[i].s_exam_mid))*(int(self.SUBJECT_LIST[i].m_exam_mid) / 100)), ("Midterm Exam")])
        if int(self.SUBJECT_LIST[i].s_final) == 0:
            cal_hint.append([( (int(self.SUBJECT_LIST[i].m_final) - int(self.SUBJECT_LIST[i].s_final)) * (int(self.SUBJECT_LIST[i].m_final) / 100) ), ("Final Exam")])
            
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_project) - int(self.SUBJECT_LIST[i].s_project))*(int(self.SUBJECT_LIST[i].m_project) / 100)), ("Project")])
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_hw) - int(self.SUBJECT_LIST[i].s_hw))*(int(self.SUBJECT_LIST[i].m_hw)/ 100)), ("Homework")])
        cal_hint.append([((int(self.SUBJECT_LIST[i].m_other) - int(self.SUBJECT_LIST[i].s_other))*(int(self.SUBJECT_LIST[i].m_other) / 100)), ("Other")])
        cal_hint.sort(reverse = True)
        number = 1
        each_y = 50

        for i in cal_hint:
            self.tk.Message(self.hint_frame, text="No."+str(number)+"   "+i[1], width=100).place(x=80,y=each_y)
            number += 1
            each_y += 25

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
        

        self.SUBJECT_LIST.append(sbj)
        self.tk.messagebox.showinfo(message="Success - " + str(self.name), title="Success")
        self.lb_sel_i = self.listbox.size() - 1
        print (self.lb_sel_i)
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
        self.e_s_exam_final.insert(0, self.SUBJECT_LIST[index].m_final)

        self.e_s_project.delete(0, len(self.e_s_project.get()))
        self.e_s_project.insert(0, self.SUBJECT_LIST[index].m_project)

        self.e_s_hw.delete(0, len(self.e_s_hw.get()))
        self.e_s_hw.insert(0, self.SUBJECT_LIST[index].m_hw)

        self.e_s_other.delete(0, len(self.e_s_other.get()))
        self.e_s_other.insert(0, self.SUBJECT_LIST[index].weight)

        self.calculate()
        self.hint()
        
        print ('You selected item %d: "%s"' % (index, value))
