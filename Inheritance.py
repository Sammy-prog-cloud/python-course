class Animal:
    def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
        self.__birth_type = birth_type
        self.__appearance = appearance
        self.__blooded = blooded

    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it has {} it is {}".format(type(self).__name__, self.birth_type, self.appearance, self.blooded)


class Mammal(Animal):
    def __init__(self, birth_type="Born Alive", appearance="Hair or Fur", blooded="Warm Blooded", nurse_young=True):
        Animal.__init__(self, birth_type, appearance, blooded)
        self.__nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        self.__nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + "and it is {} they nurse their young".format(self.nurse_young)


class Reptile(Animal):
    def __init__(self, birth_type="Born in an egg or born alive", appearance="Dry Scales", blooded="Cold Blooded"):
        Animal.__init__(self, birth_type, appearance, blooded)


def main():
    animal1 = Animal("Born Alive")
    print(animal1.birth_type)
    print(animal1)


main()
