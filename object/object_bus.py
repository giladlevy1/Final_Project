class bus:
    def __init__(self,sits,pas):
        self.l_sits = sits
        self.n_passangers = pas


sits = input("enter list of sits: ")
sits = sits.split(" ")
pas = int(input("enter number of passangers on bus: "))
magicbus = bus(sits,pas)
