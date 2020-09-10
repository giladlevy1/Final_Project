def rishoni ():
    for i in range (2,num):
        if num % i == 0:
            return ("it is not a prime number")

    else:
        return ("it is a prime number")


num = int(input("enter number: "))
print(rishoni())
