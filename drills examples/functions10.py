def valid():
    if 70 <= grade <= 100:
        return True
    if 0<= grade < 70:
        return False
    if grade < 0 or grade > 100:
        return "invalid grade"

count = 0
grade = int(input("enter grade: "))
while count != 5:
    if 0<=grade<=120:
        count+=1
    if valid() == True:
        print("pass")
    if valid() == False:
        print("fail")
    if valid() == "invalid grade":
        print("invalid grade")
    grade = int(input("enter grade: "))




