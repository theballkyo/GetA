import tkinter as tk
from classes.subject import *

root = tk.Tk()

# Setting windows
root.geometry("800x600")
root.resizable(0, 0)
root.title('Project PSIT "Get A"')

class Run(object):
    """ Run GetA """
    
    def __init__(self):
        #self.s = subject.Subject(root, "Test")
        self.SUBJECT_LIST = []
        new_subject = tk.Button(root, text='New Subject', command = self.new_subject)
        new_subject.pack()
        
    def new_subject(self):
        self.top = tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("250x50")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = tk.Frame(self.top)
        frame.pack()

        self.e = tk.Entry(frame)
        self.e.grid(row=0, column=0, padx=5, pady=15)
        self.e.focus()
        self.e.bind("<Return>", self.add_subject)
        button_ok = tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=0, column=1)

    def set_e_text(self, text):
        self.e.delete(0, len(self.e.get()))
        self.e.insert(0,text)
        return True

    # def add_subject(self):
    #     print (self.e.get())
    #     self.b = tk.Button(root, text=self.e.get())
    #     self.b.pack()

    def add_subject(self, event=""):
        """ New subject """
        if len(self.SUBJECT_LIST) > 20:
            tk.messagebox.showinfo(message="Subjects is maximum", title="Error !")
            self.top.destroy()
            return False

        name = self.e.get()
        if name == "":
            tk.messagebox.showinfo(message="Please enter subject name.", title="Error !")
            # self.top.destroy()
            # self.new_subject()
            self.e.focus()
            return False

        btn = Subject(tk, root, name)
        self.SUBJECT_LIST.append(btn)
        self.set_e_text("")
        self.get_subject()

    def get_subject(self):
        for i in range(len(self.SUBJECT_LIST)):
            print (i, self.SUBJECT_LIST[i].get_text())
        print ("------------------------------------")

# Run now
r = Run()
