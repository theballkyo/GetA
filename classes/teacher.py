class Teacher():

<<<<<<< HEAD
    def __init__(self):
        self.member = int(input())
        self.data = []
        self.a = int(input())
        self.bp = int(input())
        self.b = int(input())
        self.cp = int(input())
        self.c = int(input())
        self.dp = int(input())
        self.d = int(input())
        for i in range(self.member):
            self.data.append([int(input()), i+1])
        self.data.sort(reverse = True)

    def initUI(self):
        pass
    
    def resault(self):
        for i in range(len(self.data)):
            print ("No."+ str(self.data[i][1])+" Score : "+str(self.data[i][0])),
            if self.a != 0:
                print ("Grade is A")
                self.a -= 1
            elif self.bp != 0:
                print ("Grade is B+")
                self.bp -= 1
            elif self.b != 0:
                print ("Grade is B")
                self.b -= 1
            elif self.cp != 0:
                print ("Grade is C+")
                self.cp -= 1
            elif self.c != 0:
                print ("Grade is C")
                self.c -= 1
            elif self.dp != 0:
                print ("Grade is D+")
                self.dp -= 1
            elif self.d != 0:
                print ("Grade is D")
                self.d -= 1
            else:
                print ("Grade is F")
            
=======
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
            new = self.tk.Button(self.root, text='New Subject',
                                        command = self.new_subject_ui)
            new.pack()
        # University
        else:
<<<<<<< HEAD
        	pass
>>>>>>> 41d5915dd841a26c28fe7954f1956ee11748d167
=======
            pass

    def new_subject_ui(self):
        """ Create UI for add new subject """
        self.top = self.tk.Toplevel()
        self.top.title("Add new subject")
        self.top.geometry("250x50")
        self.top.resizable(0, 0)
        self.top.focus()

        frame = self.tk.Frame(self.top)
        frame.pack()

        self.e = self.tk.Entry(frame)
        self.e.grid(row=0, column=0, padx=5, pady=15)
        self.e.focus()
        self.e.bind("<Return>", self.add_subject)
        
        button_ok = self.tk.Button(frame, text='OK', command=self.add_subject)
        button_ok.grid(row=0, column=1)
        buttun_clo = self.tk.Button(frame, text='Close', command=self.top.destroy).grid(row=0, column=2)

>>>>>>> 633e884448ee4388f426f8bf632c1bb22a92fd25
