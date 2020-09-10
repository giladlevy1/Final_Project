class person:
    def __init__(self,name,age,children_n):
        self.name = name
        self.age = age
        self.children = children_n

    def __str__(self):
        return (f"i'm {self.name},i'm {self.age} years old, and i have {self.children} kids")

    def haschildren(self):
        if self.children > 0:
            return (f"{self.name} has kids -",True)
        else:
            return (f"{self.name} has kids -",False)

    def agegroup(self):
        if 0 < self.age <= 18:
            return (f"{self.name} is a child")
        if 18 < self.age <= 60:
            return (f"{self.name} is an adult")
        if 60 < self.age <= 120:
            return (f"{self.name} is a senior")


kobi = person("kobi",21,3)
print("1-",kobi)
print("2-",kobi.haschildren())
print("3-",kobi.agegroup())
