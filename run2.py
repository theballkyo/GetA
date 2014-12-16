from classes.studentUI import *
from classes.teacherUI import *

import tkinter as tk
from tkinter import ttk
class Run:

    def __init__(self):
        self.root = tk.Tk()
        self.tk = tk
        # Mode 1 = Highschool, Mode 2 = University
        self.mode = self.root.geometry("600x500")
        self.root.resizable(0, 0)
        self.root.title('Project PSIT "Get A"')

        bg_image = self.tk.PhotoImage(file= 'Bg.gif')
        self.background = self.tk.Label(self.root,image = bg_image)
        self.background.place(x=0, y=0)
        
        title_image = self.tk.PhotoImage(file= 'Title.gif')
        self.tk.Label(self.root,image = title_image, bg='#0e451f').place(x=100, y=30)

        std_btn_image = self.tk.PhotoImage(file= 'Student.gif')
        self.btn_std = tk.Button(self.root, text="Student",image = std_btn_image, bg='#0e451f',relief='flat', command=self.start_std_ui)
        self.btn_std.place(x=100, y=230)

        tch_btn_image = self.tk.PhotoImage(file= 'Teacher.gif')
        self.btn_tch = tk.Button(self.root, text="Teacher",image = tch_btn_image, bg='#0e451f',relief='flat', command=self.start_teah_ui)
        self.btn_tch.place(x=350, y=230)
        self.root.mainloop()
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
