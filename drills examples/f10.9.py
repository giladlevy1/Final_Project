list1 = []
num = int(input("enter number: "))
while num != 0:
    list1.append(num)
    num = int(input("enter number: "))

sum = 0
for i in list1:
    if i % 2 == 0:
        sum = sum + i

print("the sum of zugiim is",sum)
