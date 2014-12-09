from classes.student import *
from classes.teacher import *

import tkinter as tk 
class Run:

    def __init__(self):
        self.root = tk.Tk()
        self.tk = tk
        # Mode 1 = Highschool, Mode 2 = University
        self.mode = 0
        
        self.initUI()
        
    def initUI(self):
        self.root.geometry("600x500")
        self.root.resizable(0, 0)
        self.root.title('Project PSIT "Get A"')
        
        self.frame_subject = tk.Frame(self.root, bg="Blue")
        self.frame_subject.place(width=300, height=250, x=0, y=0)

        self.frame_edit = tk.Frame(self.root, width=400, height=300, bg="Red")
        self.frame_edit.place(width=300, height=250, x=300, y=0)

        self.frame_result = tk.Frame(self.root, width=800, height=300, bg="Yellow")
        self.frame_result.place(width=600, height=250, x=0, y=250)

        self.btn_1 = tk.Button(self.frame_subject, text='Highschool', command=self.set_highschool)
        self.btn_1.grid(row=0, column=0)
        self.btn_2 = tk.Button(self.frame_subject, text='University', command=self.set_university)
        self.btn_2.grid(row=0, column=1)

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
