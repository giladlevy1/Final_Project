class student:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.grades = {}

    def __repr__(self):
        return f'{self.name} - id:{self.id}'

    def add_grade(self,subject,grade):
        self.grades.update({subject : grade})

    def calc_factor(self,subject,factor):
        grade = self.grades.get(subject) * factor
        if grade > 100:
            grade = 100
        self.grades.update({subject: grade})
        return grade

    def average(self):
        return sum(self.grades.values()) / len(self.grades.values())
