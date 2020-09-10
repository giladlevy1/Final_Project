from object.class_student import student

class course:
    def __init__(self,number,name,max_students):
        self.number = number
        self.name = name
        self.subject_proffesor = {}
        self.studentslist = []
        self.maxstudents = max_students

    def __str__(self):
        f'{self.name} - {self.number}'

    def add_student(self,student):
        if len(self.studentslist) <= self.maxstudents:
            self.studentslist.append(student)
            return student.name, "entered the course"
        else:
            return "no room in the course"

    def add_factor(self,subject,factor):
        if subject in self.subject_proffesor:
            for student in self.studentslist:
                student.calc_factor(subject,factor)

    def del_student(self, id):
        for student in self.studentslist:
            if student.id == id:
                self.studentslist.remove(student)

    def calc_avg(self):
        summing = 0
        for student in self.studentslist:
            summing = summing + student.average()
        return summing / len(self.studentslist)














