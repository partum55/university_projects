"""Temp"""


class Classroom:
    """Temp"""

    def __init__(self, num: str, cap: int, equip: list[str]):
        """
        Temp

        :param num:
        :param cap:
        :param equip:
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        """
        self.number = num
        self.capacity = cap
        self.equipment = equip

    def __str__(self):
        """
        Temp

        :return:

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the \
following equipment: PC, projector, mic.
        """
        return (f"Classroom {self.number} has a capacity of {self.capacity} "
                f"persons and has the following equipment: {", ".join(self.equipment)}.")

    def is_larger(self, other):
        """
        Temp

        :param other:
        :return:

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return self.capacity > other.capacity

    def equipment_differences(self, other):
        """
        Temp

        :param other:
        :return:

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'mic', 'projector']
        """
        return sorted(i for i in self.equipment if i not in other.equipment)

    def __repr__(self):
        """
        Temp

        :return:
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """
        return f"Classroom('{self.number}', {self.capacity}, {self.equipment})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
