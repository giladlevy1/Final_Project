list_names = ["gilad", "roy", "shlomi", "goldis", "bar"]
list_grades = [88, 97, 79, 91, 91]
dict1 = {}

c = 0
for i in range(5):
    dict1.update({list_names[c]: list_grades[c]})
    c = c + 1

print(dict1)

grades_average = (sum(list_grades)) / len(list_grades)
print("grades average is ", grades_average)

for i in dict1:
    if dict1[i] > grades_average:
        print(i, dict1[i])
