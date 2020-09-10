class animal:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5

    def __str__(self):
        return f"==============\ni'm an animal by name of {self.name},\n my hunger level is {self.hunger},\nand my energy level is {self.energy}\n==============="

    def eat(self):
        food_amount = int(input("enter food amount given: "))
        t = food_amount / 50
        p = food_amount / 100
        af = self.hunger * 50
        rf = food_amount - af

        self.hunger = self.hunger - t
        self.energy = self.energy - p

        if self.hunger < 0:
            self.energy = self.energy + (rf / 100)
            self.hunger = 0
            print(f"{self.name} is full but havn't finished eating")

    def play(self):
        playtime = int(input("enter play time: "))
        x = playtime / 10

        apl = self.energy * 5
        rpl = playtime - apl

        self.energy = self.energy - 2 * x
        self.hunger = self.hunger + 2 * x

        if self.energy < 0:
            self.hunger = self.hunger - (rpl / 5)
            self.energy = 0
            print(f"game finished in the middle because {self.name} is tired")
        if self.hunger > 10:
            self.hunger = 10

    def rest(self):
        resttime = int(input("enter rest time: "))
        r = resttime / 20
        y = resttime / 30

        rt = (10 - self.energy) * 20
        rrt = resttime - rt

        rt2 = (10 - self.hunger) * 30
        rrt2 = resttime - rt2

        self.energy = self.energy + r
        self.hunger = self.hunger + y

        if self.energy > 10:
            self.energy = 10
            print(f"{self.name} finished resting and wants to play")
            self.hunger = self.hunger - (rrt / 30)

        if self.hunger > 10:
            self.hunger = 10
            print(f"{self.name} finished resting and wants to eat")
            self.energy = self.energy - (rrt2 / 20)

monster = animal("killer")

# monster.eat()
# print(monster)
#
# monster.play()
# print(monster)
#
# monster.rest()
# print(monster)

cat = animal(input("enter animal name: "))
print("eat - 1, play - 2, rest - 3, 0 - finish")
num = int(input("enter action number: "))
while num != 0:
    if num == 1:
        cat.eat()
        print(cat)
        print("eat - 1, play - 2, rest - 3, 0 - finish")
    if num == 2:
        cat.play()
        print(cat)
        print("eat - 1, play - 2, rest - 3, 0 - finish")
    if num == 3:
        cat.rest()
        print(cat)
        print("eat - 1, play - 2, rest - 3, 0 - finish")

    num = int(input("enter action number: "))

print("game finshed thank you!!!")