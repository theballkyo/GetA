import tkinter as tk
from classes.subject import *

root = tk.Tk()
root.geometry("800x600")
root.title('Project PSIT "Get A"')

class Run(object):
    """ Run GetA """
    SUBJECT_LIST = []
    def __init__(self):
        #self.s = subject.Subject(root, "Test")
        
        new_subject = tk.Button(root, text='New Subject', command = self.new_subject)
        new_subject.pack()
        
    def new_subject(self):
        top = tk.Toplevel()
        top.title("Add new subject")
        top.geometry("200x50")
        top.focus()
        self.e = tk.Entry(top)
        self.e.pack()
        self.e.focus()
        button_ok = tk.Button(top, text='OK', command=self.add_subject2)
        button_ok.pack()

    def add_subject(self):
        print (self.e.get())
        self.b = tk.Button(root, text=self.e.get())
        self.b.pack()

    def add_subject2(self):
        """ New subject """
        name = self.e.get()
        btn = Subject(tk, root, name)
        Run.SUBJECT_LIST.append(btn)
        self.get_subject()

    def get_subject(self):
        for i in range(len(Run.SUBJECT_LIST)):
            print (i, Run.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")
r = Run()
