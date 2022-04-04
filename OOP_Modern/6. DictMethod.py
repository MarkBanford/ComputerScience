class MercedezBenz:
    doors = 4
    model = 'G'
    wheels = 4

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


m1 = MercedezBenz("lavender")  # Different namespaces, m1 and m2
m2 = MercedezBenz("purple")

# where is this instance attribute binding stored? ie m1.colour. We can use the __dict__ method

print(m1.__dict__)
print(m2.__dict__)

# We can show this by adding a new attribute to m2 and then call m1 dict. __dict__ lives in the class namespace

m2.horse_power = 490
print(m2.__dict__)
print(m1.__dict__)

m1.__dict__["horse_power"] = 290
print(m2.__dict__)
print(m1.__dict__)


print(type(MercedezBenz.__dict__))  # notice this is a mapping proxy. A read only "dictionary like" structure
# Keys are always strings due to Method Resolution order (optimisation)

print(MercedezBenz.__dict__)