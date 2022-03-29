class MercedezBenz:
    doors = 2
    wheels = 4  # State
    model = 'G'

    def drive(self):
        return f" A Merc is driving and it is {self}"


m1 = MercedezBenz()
print(m1.drive())
m2 = MercedezBenz()
print(m2.drive())
