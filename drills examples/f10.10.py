def backs (x):
    if x == x[::-1]:
        return "your string is a polindrom"
    else:
        return "not a polindrom"

str1 = input("enter string: ")
newstr1 = ""
for i in range(0,len(str1)):
    if str1[i] != " ":
        newstr1 = newstr1+str1[i]
print(backs(newstr1))


