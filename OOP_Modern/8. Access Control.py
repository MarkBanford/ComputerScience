class Tire:
    def __init__(self, kind, distance_covered):
        self.kind = kind
        self.distance_covered = distance_covered


class MercedezBenz:
    doors = 4
    model = 'G'
    wheels = 4

    def __init__(self, colour='black'):
        self.colour = colour


# Python doesnt make member private as it favours the Uniform Access Principle

m1 = MercedezBenz("Lavender")
m1.doors += 1  # Python would allow us to set it to anything, so we need some controls
print(m1.doors)
