class MercedezBenz:
    doors = 4
    wheels = 4
    model = 'G'

    def __init__(self, colour='white'):  # After instance creation, but before it is returned
        self.colour = colour

    def drive(self):
        print(f"A Merc is driving. It is {self}\n")


m1 = MercedezBenz('Black')

setattr(m1, 'colour', 'red')

# The reason this is so useful is if we have hundreds of objects, we can loop through and update them

z1 = MercedezBenz()
z2 = MercedezBenz()
z3 = MercedezBenz()

print(z1.colour)
print(z2.doors)
print(z3.colour)

objs = [z1, z2, z3]
attribs = ["colour", "doors"]
values = ["Silver", 5]

for obj in objs:
    for attrib, val in zip(attribs, values):
        setattr(obj, attrib, val)

print(z1.colour)
print(z2.doors)
print(z3.colour)
