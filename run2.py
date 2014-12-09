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
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.root.title('Project PSIT "Get A"')
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.btn_1 = tk.Button(self.frame, text='Highschool', command=self.set_highschool)
        self.btn_1.grid(row=0, column=0)
        self.btn_2 = tk.Button(self.frame, text='University', command=self.set_university)
        self.btn_2.grid(row=0, column=1)

    def remove_select_level(self):
        self.btn_1.destroy()
        self.btn_2.destroy()

    def selete_type(self):
        self.btn_1.config(text="Student", command=self.strudent)
        self.btn_2.config(text="Teacher", command=self.teacher)

    def set_highschool(self):
        """ Start m """
        # self.remove_select_level()
        # Student(self)
        self.selete_type()
        self.mode = 1
        
    def set_university(self):
        """ Start u """
        self.selete_type()
        self.mode = 2

    def strudent(self):
        """ Start Student mode """
        Student(self)

    def teacher(self):
        """ Start Teacher mode """
        Teacher(self)
        
r = Run()
