class Student:
    def __init__(self, id, name):
        self.name = name

        self.weight = 0
        self.exam_mid = 0
        self.final = 0
        self.project = 0
        self.hw = 0
        self.other = 0

    def get_name(self):
        return self.name