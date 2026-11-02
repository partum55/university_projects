"""Temp"""


class Furniture:
    """
    Temp

    >>> furniture1 = Furniture("empire", "bedroom")
    >>> furniture2 = Furniture("modern", "bathroom")
    >>> not (furniture1 == furniture2)
    True
    >>> furniture1.style == "empire"
    True
    >>> furniture1.assign == "bedroom"
    True
    >>> str(furniture1) == "<furniture style is empire>"
    True
    """

    def __init__(self, style, assign):
        """Temp"""
        self.style = style
        self.assign = assign

    def __repr__(self):
        """Temp"""
        return f"<furniture style is {self.style}>"

    def __eq__(self, other):
        """Temp"""
        if isinstance(other, Furniture):
            return (self.style == other.style) and (self.assign == other.assign)
        return False


class Chair(Furniture):
    """
    Temp

    >>> chair1 = Chair("empire", "bedroom", "armchair")
    >>> chair1.tipe == "armchair"
    True
    >>> isinstance(chair1, Furniture)
    True
    >>> str(chair1) == "<This armchair furniture style is empire>"
    True
    >>> chair1.get_assign() == "bedroom"
    True
    """

    def __init__(self, style: str, assign: str, tipe: str):
        """Temp"""
        super().__init__(style, assign)
        self.tipe = tipe

    def __repr__(self):
        """Temp"""
        return f"<This {self.tipe} furniture style is {self.style}>"

    def get_assign(self):
        """Temp"""
        return self.assign


if __name__ == "__main__":
    import doctest
    doctest.testmod()
