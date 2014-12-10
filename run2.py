from classes.studentUI import *
from classes.teacherUI import *

import tkinter as tk 
class Run:

    def __init__(self):
        self.root = tk.Tk()
        self.tk = tk
        # Mode 1 = Highschool, Mode 2 = University
        self.mode = 0
        
        #self.studentUI()
        self.initUI()
        
    def initUI(self):
        self.root.geometry("600x500")
        self.root.resizable(0, 0)
        self.root.title('Project PSIT "Get A"')
        
        self.btn_std = tk.Button(self.root, text="Student", command=self.start_std_ui)
        self.btn_std.place(x=200, y=200)

        self.btn_tch = tk.Button(self.root, text="Teacher", command=self.start_teah_ui)
        self.btn_tch.place(x=400, y=200)
        
    def start_std_ui(self):
        StudentUI(self)

    def start_teah_ui(self):
        TeacherUI(self)

    def remove_select_level(self):
        self.btn_1.destroy()
        self.btn_2.destroy()

    def select_type(self):
        self.btn_1.config(text="Student", command=self.student)
        self.btn_2.config(text="Teacher", command=self.teacher)

    def set_highschool(self):
        """ Start m """
        # self.remove_select_level()
        # Student(self)
        self.select_type()
        self.mode = 1
        
    def set_university(self):
        """ Start u """
        self.select_type()
        self.mode = 2

    def student(self):
        """ Start Student mode """
        Student(self)

    def teacher(self):
        """ Start Teacher mode """
        Teacher(self)
        
r = Run()
