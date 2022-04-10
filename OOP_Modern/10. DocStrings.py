class Tire:
    """Defines car tire object. The docstring format used is reST, PEP 257
    :param kind: kind of tire e.g operational, spare, winter
    :param distance_covered: the distance in km the tire has covered

    """

    def __init__(self, kind, distance_covered):
        self.kind = kind
        self.distance_covered = distance_covered


print(help(Tire))
