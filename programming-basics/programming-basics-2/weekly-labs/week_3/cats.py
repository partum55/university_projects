"""Temp"""


class Animal:
    """
    Temp

    >>> animal1 = Animal("chordata", "mammalia")
    >>> animal1.phylum == "chordata"
    True
    >>> animal1.clas == "mammalia"
    True
    >>> str(animal1) == "<animal class is mammalia>"
    True
    >>> animal2 = Animal("chordata", "birds")
    >>> not (animal1 == animal2)
    True
    """

    def __init__(self, phylum: str, clas: str):
        """Temp"""
        self.phylum = phylum
        self.clas = clas

    def __repr__(self):
        """Temp"""
        return f"<animal class is {self.clas}>"

    def __eq__(self, other):
        """Temp"""
        if isinstance(other, Animal):
            return self.phylum == other.phylum and self.clas == other.clas
        return False


class Cat(Animal):
    """
    Temp

    >>> animal1 = Animal("chordata", "mammalia")
    >>> cat1 = Cat("chordata", "mammalia", "felis")
    >>> cat1 == animal1
    True
    >>> cat1.sound() == "Meow"
    True
    >>> cat1.genus == "felis"
    True
    >>> isinstance(cat1, Animal)
    True
    >>> str(cat1) == "<This felis animal class is mammalia>"
    True
    """

    def __init__(self, phylum: str, clas: str, genus: str):
        """Temp"""
        super().__init__(phylum, clas)
        self.genus = genus

    @staticmethod
    def sound():
        """Temp"""
        return "Meow"

    def __repr__(self):
        """Temp"""
        return f"<This {self.genus} animal class is {self.clas}>"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
