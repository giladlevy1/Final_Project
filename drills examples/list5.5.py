
grades=input("write all grades: ")

listgrades=grades.split(" ")

# print(listgrades)
counthigh=0
countlow=0
for i in listgrades:
    if 0<int(i)<60:
        # print(i,"fail")
        countlow=countlow+1

    if 100>int(i)>=60:
        # print(i,"passed")
        counthigh=counthigh+1

print("number of passed: ",counthigh)
print("number of fails: ",countlow)



