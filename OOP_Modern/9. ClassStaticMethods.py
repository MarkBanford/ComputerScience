'''if we want a method to be a static methods and not instance methods we use @staticmethod decorator
static methods are bound to the class, not the class instances
This means it can be called without creating an instance'''


class MercedezBenz:
    doors = 4
    wheels = 4
    model = 'G'

    def __init__(self, colour='Brown'):  # After instance creation, but before it is returned
        self.colour = colour

    def drive(self):
        print(f"A Merc is driving. It is {self}\n")

    @staticmethod
    def auto_drive():  # no parameter required
        return "Auto-driving for now..."

    @classmethod
    def create_lease(cls): #class methods can be used to modify the class on the fly
        print(f'A lease for {cls} will be created')


print(MercedezBenz.auto_drive())

a1 = MercedezBenz()
print(a1.auto_drive())
