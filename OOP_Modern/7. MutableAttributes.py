class Tire:
    def __init__(self, kind, distance_covered):
        self.kind = kind
        self.distance_covered = distance_covered


class MercedezBenz:
    '''Classes have their own attribute namespace
    It is accessed using __dict__
    unlike instances, class __dict__ is a mapping proxy, which is more restricted
    the class __dict__ contains all of the instance, class and static methods we define
    It also contains some descriptors and other class dunders'''
    doors = 4
    model = 'G'
    wheels = 4

    tires = [Tire("Operational", 10) for i in range(4)]

    def __init__(self, colour='black'):
        self.colour = colour

    def drive(self):
        return f"Merc is driving, It is  {self}\n"

    @staticmethod
    def auto_drive():
        return "Auto-driving for now..."

    @classmethod
    def create_lease(cls):
        print(f"A lease for {cls} will be created")


m1 = MercedezBenz()
m2 = MercedezBenz()

m1.tires.append(Tire(kind="spare", distance_covered=100))  # This has affected m2 as well as m1, because its a class var
print(m1.tires)
print(m2.tires)