class MercedezBenz:
    doors = 4
    wheels = 4
    model = 'G'

    def __init__(self, colour):  # After instance creation, but before it is returned
        self.colour = colour

    def drive(self):
        print(f"A Merc is driving. It is {self}\n")




