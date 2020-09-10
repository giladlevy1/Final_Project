from random import *
def addrand():
    for i in range (20):
        list1.append(randint(1,100))
    return list1

def findcount():
    return list1.count(num)

def max65():
    return list1.index(max1)


list1 = []
print(addrand())

num = int(input("enter number: "))
print(num,"is",findcount(),"times in list1")

max1 = max(list1)
print (max65())

