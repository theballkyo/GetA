class Student():
    '''
    Class Student()
    For calculate everything for Funtion Student
    '''
    def __init__(self):
        '''
        init
        get a important data for calculate a Grade&Hint
        
        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        
        self.subject -> name subject.
        self.weight -> weight of subject.
        self.total -> max score or total score of subject.
        self.b_exam -> base exam score.
        self.b_project -> base project score.
        self.b_hw -> base home workscore.
        self.b_other -> base other score.
        self.g_exam -> exam score you get.
        self.g_project -> project score you get.
        self.g_hw -> home work score you get.
        self.g_other -> other score you get.

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        
        '''
        self.subject = input()
        self.weight = int(input())
        self.total = int(input())
        self.b_exam = int(input())
        self.b_project = int(input())
        self.b_hw = int(input())
        self.b_other = int(input())
        self.g_exam = int(input())
        self.g_project = int(input())
        self.g_hw = int(input())
        self.g_other = int(input())
    def calculate(self):
        '''
        x.calculate_grade()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Calculate what grade do you get

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        '''
        total_score = self.g_exam + self.g_project + self.g_hw + self.g_other
        total_score = int(total_score)
        if total_score >= 80:
            return self.subject + (" Total score = ") + str(total_score)+( " : Your grade is 4.00")
        elif total_score >= 75:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 3.50")
        elif total_score >= 70:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 3.00")
        elif total_score >= 65:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 2.50")
        elif total_score >= 60:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 2.00")
        elif total_score >= 55:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 1.50")
        elif total_score >= 50:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 1.00")
        elif total_score < 50:
            return self.subject + (" Total score = ") + str(total_score)+ (" : Your grade is 0")
    def hint(self):
        '''
        x.hint()

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

        Find What part of score that you must do  for make your grade better

        -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
        '''
        cal_hint = max([[((self.b_exam - self.g_exam)*(self.b_exam / 100)), ("Exam")],\
                    [((self.b_project - self.g_project)*(self.b_project / 100)), ("Project")],\
                    [((self.b_hw - self.g_hw)*(self.b_hw/ 100)), ("Homework")],\
                    [((self.b_other - self.g_other)*(self.b_other / 100)), ("Exam")],\
                    [((self.b_other - self.g_other)*(self.b_other / 100)), ("Other")]])
        
        return ("You must do this part for better score :  ") +  cal_hint[1]
        
