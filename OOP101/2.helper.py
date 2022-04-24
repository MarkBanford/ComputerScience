# when to use class methods and when to use static method


class Item:
    @staticmethod
    def is_integer():
        pass

    # should do something that has a relationship with the class, but not something that must be unique per instance
    # Static methods do not pass self, they act like regular functions

    @classmethod
    def instantiate_from_csv(cls):
        pass

    # To do with class, but usually to manipulate structures of data to instantiate objects



