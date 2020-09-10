def dic_test1 ():
    'thtis is shittttttt'
    dict1 = {"1": 10, "2": 20, "3": 30, "4": 40, "5": 50, "abc": 60}
    key =input("enter key: ")
    while key != "0":
        if key in dict1:
            del dict1[key]
            print(dict1)
        else:
            print("key not in dict1")
        key = input("enter key: ")

    print("invalid, bye bye loser!")
help(dic_test1)
dic_test1()
