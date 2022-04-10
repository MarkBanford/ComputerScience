import string
from random import choices
from copy import copy


class Password:
    """ Class should generate a random password having following characteristics
    low: Mix of 8 lowercase and uppercase letters only
    mid: Mix of 12 lowercase and uppercase letters and numbers
    high: Mix of 16 lowercase, uppercase, numbers and punctuation signs

    if user specifies length, then defaults are overridden
    if user does not specify strength or length, then default is "mid"

    class should implement show_input_universe() which is not specific to the instance
    The method should return a dict of lists exposing the pools of chars eg
    {"letters":['a','b'], "numbers:[0,1,2,3], "punctuation":["!","?"]}

    :param strength, user defines the strength of their password
    :type strength: str, optional
    :param length, user defines the length of their password
    :type length: str, optional

    """

    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(string.ascii_letters),
        "punctuation": list(string.punctuation)

    }

    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16

    }

    @classmethod
    def show_input_universe(cls):
        """
        :return Return input universe pool
        :rtype dictionary of lists"""

        return cls.INPUT_UNIVERSE

    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):

        """Generates password on initialisation
        :return randomly generated password
        :rtype str
        """

        population = copy(self.INPUT_UNIVERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
        else:
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
    weak = Password(strength="low", length=20)
    print("weak password " + weak.password)
    mid = Password(strength="mid", length=40)
    print("mid password " + mid.password)
    high = Password(strength="high", length=40)
    print("high password " + high.password)
    default = Password()
    print(f"default password is {default.password}")
