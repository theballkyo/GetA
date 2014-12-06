from classes.gui import *
from classes.highschool import *
from classes.university import *
class Run(Gui, Highschool):

    def __init__(self):
        Gui.__init__(self)
        self.initUI()
        
    def initUI(self):
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.root.title('Project PSIT "Get A"')
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.btn_1 = tk.Button(self.frame, text='Highschool', command=self.start_m)
        self.btn_1.grid(row=0, column=0)
        self.btn_2 = tk.Button(self.frame, text='University', command=self.start_u)
        self.btn_2.grid(row=0, column=1)

    def remove_select_level(self):
        self.btn_1.destroy()
        self.btn_2.destroy()

    def start_m(self):
        """ Start m """
        self.remove_select_level()
        Highschool(self)
        
    def start_u(self):
        """ Start u """
        self.remove_select_level()
        University.__init__(self)
        
r = Run()
