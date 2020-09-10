list1=list(range(1,11))

print(list1)

# print(list1[7:10])
#
# print("===================")
#
# print(list1[::-1])
#
# print("===================")
#
# print(list1[1::2])
#
# print("===================")
#
# print(list1[::2])
#
# print("===================")
#
# num1=input("write number 1: ")
# num2=input("write number 2: ")
# num3=input("write number 3: ")
#
# list1[4]=num1
# list1[5]=num2
# list1[-1]=num3
#
# print(list1)

print("===================")

list2=[]
for i in list1:
    i=i*2
    list2.append(i)
print(list2)

list6=[]

list6.append(list1[0])
list6.append(list1[-1])

print(list6)


