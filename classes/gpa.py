class Gpa:
    def __init__(self, weight, grade):
        self.weight = weight
        self.grade = grade
    def cal_gpa(self): 
        sum_all += self.weight * self.grade
        lis_weight.append(self.weight)
        all_subject.append(sum_all)

lis_weight = []
all_subject = []
sum_all = 0
for subject in Subject_LIST:
    subject = Gpa(subject.weight, subject.grade)
    subject.cal_gpa

gpa = sum(all_subject)*1.0 / sum(lis_weight)
print (gpa)
