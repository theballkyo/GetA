class Teacher():

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
        	pass
        # University
        else:
        	pass
