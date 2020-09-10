day=int(input("enter day: "))
month=int(input("enter month: "))
year=int(input("enter year: "))
year1=year%100

if (1<=day<=31 and 1<=month<=12 and 1950<=year<=2020):

    if 0<year1<10:
        yy="0"+str(year1)
    else:
        yy=str(year1)

    if  month<10:
        mm="0"+str(month)
    else:
        mm=str(month)

    print(str(day)+"/"+mm+"/"+yy)


if day<1 or day>31:
    print("invalid day")
if month<1 or month>12:
    print("invalid month")
if year<1950 or year>2020:
    print("invalid year")






