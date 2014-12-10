from classes.student import *

class Subject():

    def __init__(self, parent):
        self.name = parent.name
        self.tk = parent.tk
        self.root = parent.root
        self.frame_subject = parent.frame_subject

        self.STD_LIST = parent.STD_LIST

        self.student_obj = {}
        self.m_exam_mid = 0
        self.m_final = 0
        self.m_project = 0
        self.m_hw = 0
        self.m_other = 0
        self.weight = 0
        self.score = 0

    def get_text(self):
        return self.name

    def add_std(self, id, name):  
        self.student_obj[id] = Student(id, name)

    def get_std(self):
        for std in self.student_obj.values():
            print (std.get_name())