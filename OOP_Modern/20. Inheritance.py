class Virus:
    # name
    # reproduction rate
    # resistance
    # viral load
    def __init__(self, name, reproduction_rate, resistance):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.resistance = resistance
        self.host = None
        self.load = 1

    def infect(self, host):
        self.host = host

    def reproduce(self):
        if self.host is not None:
            self.load *= (1 + self.reproduction_rate)
            return True, f"Virus reproduced in {self.host}. Viral load: {int(self.load)}"
        raise AttributeError("Virus needs to infect a host before being able to reproduce")


class RNAVirus(Virus):
    genome = "ribonucleic"

    def reproduce(self):
        pass


class Coronavirus(RNAVirus):
    pass


class SARSCov2(Coronavirus):
    pass


v = Virus("pura", 1.2, 1.1)
v.infect("animal1")
print(v.reproduce())
