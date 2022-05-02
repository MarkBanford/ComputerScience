# instance > class > superclass(s) > object

class TempVirus:
    attr = "some_class_attr"
    attr_other = "some_other_class_attr"

    def __init__(self, attr):
        self.attr = attr  # binds attribute to instance


class RNAVirus(TempVirus):
    pass


v1 = TempVirus("instance_attribute")
print(v1.attr)
print(v1.__dict__)

print(v1.attr_other)  # checks instance namespace, if not found it goes to class namespace
print(v1.__class__.__dict__)

print(TempVirus.__bases__)  # checks for parents (<class 'object'>,)
print(RNAVirus.__mro__)  # whole chain (<class '__main__.RNAVirus'>, <class '__main__.TempVirus'>, <class 'object'>)
