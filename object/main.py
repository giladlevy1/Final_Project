from object.class_student import student
from object.class_course import course

school = course(2,"school",30)                         #first assigment

school.subject_proffesor.update({"history" : "david"}) #second assigment
school.subject_proffesor.update({"sport" : "dagan"})
school.subject_proffesor.update({"bible" : "neli"})

id = int(input("enter student id: "))                  #third assigment
while id != 0:
    name = input("enter student name: ")
    student1 = student(id, name)
    student1.add_grade("history",int(input("enter grade for history: ")))
    student1.add_grade("sport", int(input("enter grade for sport: ")))
    student1.add_grade("bible", int(input("enter grade for bible: ")))
    school.add_student(student1)
    id = int(input("enter student id: "))

print(school.studentslist)

school.add_factor("history", 1.2)                      #fourth assigment
for student1 in school.studentslist:
    print(student1.name,"grades are", "-", student1.grades )

listaverage = []
for student1 in school.studentslist:
    listaverage.append(student.average(student1))
print(listaverage)

minaverage = min(listaverage)
for student1 in school.studentslist:
    if minaverage == student.average(student1):
        school.del_student(student1.id)

print(school.studentslist)

print("the course detailes are:")
print("subjects and proffesors are: ",school.subject_proffesor)
print("the students list is: ",school.studentslist)

for student1 in school.studentslist:
    print(student1.name,"grades are",student1.grades)






