from random import getrandbits


class Virus:
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

            should_mutate = getrandbits(1)
            print(f"Should mutate: {should_mutate}")

            if should_mutate:
                try:
                    self.mutate()  # handled in subclass
                except AttributeError:
                    pass

            return True, f"Virus reproduced in {self.host}. Viral load: {int(self.load)}"
        raise AttributeError("Virus needs to infect a host before being able to reproduce")


class RNAVirus(Virus):
    genome = "ribonucleic"

    def reproduce(self):
        success, status = Virus.reproduce(self)

        if success:
            print(f"{self.name} just replicated in the {self.host} host")


class DNAVirus(Virus):
    genome = "deoxy"

    def reproduce(self):
        success, status = Virus.reproduce(self)

        if success:
            print(f"{self.name} just replicated in the {self.host} host")


class Coronavirus(RNAVirus):
    pass


class SARSCov2(Coronavirus):
    def mutate(self):
        print(f"The {self.name} virus just mutated")


cv = SARSCov2("Original", 2.9, 1.2)
cv.infect("Toby")

for _ in range(4):
    print(cv.reproduce(), "\n")
