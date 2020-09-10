class curse():
    def __init__(self,cur_num,cur_name,cur_stud,max_stud):
        self.curse_number = cur_num
        self.curse_name = cur_name
        self.number_of_students_registered = cur_stud
        self.max_number_of_students_registered = max_stud

    def curse_description(self):
        return f'curse number is: {self.curse_number}, curse name is: {self.curse_name}, students: {self.number_of_students_registered}, max students: {self.max_number_of_students_registered} '

    def aviable_spots(self):
        return ("aviable spots are: "+str(curse_english.max_number_of_students_registered - curse_english.number_of_students_registered))

cur_num = int(input("enter curse number: "))
cur_name = input("enter curse name: ")
cur_stud = int(input("enter curse number of students: "))
max_stud = int(input("enter curse max number of students: "))
curse_english = curse(cur_num,cur_name,cur_stud,max_stud)

print(curse_english.curse_description())

print(curse_english.aviable_spots())



