import tkinter as tk
from classes.subject import *

root = tk.Tk()
root.geometry("800x600")
root.title('Project PSIT "Get A"')

class Run(object):
    """ Run GetA """
    
    def __init__(self):
        #self.s = subject.Subject(root, "Test")
        self.SUBJECT_LIST = []
        new_subject = tk.Button(root, text='New Subject', command = self.new_subject)
        new_subject.pack()
        
    def new_subject(self):
        top = tk.Toplevel()
        top.title("Add new subject")
        top.geometry("250x50")
        top.focus()

        frame = tk.Frame(top)
        frame.pack()
        self.e = tk.Entry(frame)
        self.e.grid(row=0, column=0, padx=5, pady=15)
        self.e.focus()
        button_ok = tk.Button(frame, text='OK', command=self.add_subject2)
        button_ok.grid(row=0, column=1)

    # def add_subject(self):
    #     print (self.e.get())
    #     self.b = tk.Button(root, text=self.e.get())
    #     self.b.pack()

    def add_subject(self):
        """ New subject """
        if len(self.SUBJECT_LIST) > 20:
            tk.messagebox.showinfo(message="Subjects is maximum", title="Error !")
            return False

        name = self.e.get()
        if name == "":
            tk.messagebox.showinfo(message="Please enter subject name.", title="Error !")
            self.new_subject()
            return False

        btn = Subject(tk, root, name)
        self.SUBJECT_LIST.append(btn)
        self.get_subject()

    def get_subject(self):
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")
r = Run()
