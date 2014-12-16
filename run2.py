from classes.studentUI import *
from classes.teacherUI import *

import tkinter as tk
from tkinter import ttk
class Run:

    def __init__(self):
        self.root = tk.Tk()
        self.tk = tk
        self.initUI()
        
    def initUI(self):
        

        self.mode = self.root.geometry(self.find_center(600, 500))
        #self.mode = self.root.geometry("600x500")
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

    def find_center(self, w, h):

        # get screen width and height
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        return '%dx%d+%d+%d' % (w, h, x, y)
    def back(self):
        self.root.destroy()
        self.__init__()
    
r = Run()
