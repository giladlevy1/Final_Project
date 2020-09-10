from random import *

class loto:
    def __init__(self):
        self.list1 = self.toss()
        self.winmax = self.maxwinprice()

    def toss(self):
        for i in range (6):
            list1.append(randint(1,45))
        return list1

    def maxwinprice(self):
        winmax = int(input("enter max winning price: "))
        return winmax

    def showlist(self):
        print("lottery result is: ",self.list1)

    def checkifinlist(self):
        truecount = 0
        if num in list1:
            print(num,"found in the list")
            truecount = truecount + 1
        else:
            print(num,"not! found in the list")
        return truecount

    def prize(self):
        truecount = self.checkifinlist()
        if truecount <= 1:
            prizemoney = 0
        if 2 <= truecount <= 5:
            prizemoney = (self.winmax * truecount) / 6
        if truecount == 6:
            prizemoney = self.winmax
        return prizemoney

truecount = 0
prizemoney = 0

list1 = []
# len(list1) = 6

agrala = loto()
print(agrala.list1)

tosscount = 1
num = int(input("enter guess: "))
while tosscount != 6 :
    if 1 <= num <= 45:
        agrala.checkifinlist()
        tosscount = tosscount + 1
        num = int(input("enter guess: "))
    else:
        print("user kicked over wrong guess")
        prizemoney = 0
        break

print("winning prize is",agrala.prize())





