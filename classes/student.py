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
            new = self.tk.Button(root.frame_subject, text='New Subject',
                                        command = self.new_subject_ui)
            new.pack()
        # University
        else:
            pass
        
    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("350x350")
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

    def calculate(self):
        '''
        x.calculate_grade()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Calculate what grade do you get

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        '''
        total_score = int(self.s_exam_mid.get()) + int(self.s_exam_final.get()) + int(self.s_project.get()) + int(self.s_hw.get()) + int(self.s_other.get())
        total_score = int(total_score)
        if total_score >= 80:
            print (self.e.get() + (" Total score = ") + str(total_score)+( " : Your grade is 4.00"))
        elif total_score >= 75:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 3.50"))
        elif total_score >= 70:
            print (self.e.get()+ (" Total score = ") + str(total_score)+ (" : Your grade is 3.00"))
        elif total_score >= 65:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 2.50"))
        elif total_score >= 60:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 2.00"))
        elif total_score >= 55:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 1.50"))
        elif total_score >= 50:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 1.00"))
        elif total_score < 50:
            print (self.e.get() + (" Total score = ") + str(total_score)+ (" : Your grade is 0"))

    def hint(self):
        '''
        x.hint()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Find What part of score that you must do  for make your grade better

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        '''
        cal_hint = sorted([[((int(self.b_exam_mid.get()) - int(self.s_exam_mid.get()))*(int(self.b_exam_mid.get()) / 100)), ("Midterm Exam")],\
                    [((int(self.b_project.get()) - int(self.s_project.get()))*(int(self.b_project.get()) / 100)), ("Project")],\
                    [((int(self.b_hw.get()) - int(self.s_hw.get()))*(int(self.b_hw.get())/ 100)), ("Homework")],\
                    [((int(self.b_other.get()) - int(self.s_other.get()))*(int(self.b_other.get()) / 100)), ("Exam")],\
                    [((int(self.b_other.get()) - int(self.s_other.get()))*(int(self.b_other.get()) / 100)), ("Other")],\
                    [((int(self.b_exam_final.get()) - int(self.s_exam_final.get()))*(int(self.b_exam_final.get()) / 100)), ("Final Exam")]])
        print ("The Sequence of important score is")
        count = 0
        for i in cal_hint:
            count += 1
            print ("No."+str(count)+" "+i[1])

    def set_e_text(self, text):
        """ Set Entry Text """
        self.e.delete(0, len(self.e.get()))
        self.e.insert(0,text)
        return True

    def add_subject(self, event=""):
        """ New subject """
        self.calculate()
        self.hint()
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

    


