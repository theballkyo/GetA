from tkinter import Toplevel
class Grade(Toplevel):

	def __init__(self, parent):
		Toplevel.__init__(self, parent.root)

		self.parent = parent
		self.title(parent.get_text())