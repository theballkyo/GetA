from tkinter import Toplevel
class Grade(Toplevel):

	def __init__(self, parent):
		Toplevel.__init__(self, parent.root)
		self.geometry("500x200")
		self.resizable(0, 0)
		self.parent = parent
		self.title("Subject name :: " + parent.get_text())