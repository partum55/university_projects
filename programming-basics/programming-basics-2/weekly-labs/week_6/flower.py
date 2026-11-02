"""Temp"""


class Flower:
    """Class Flower"""

    def __init__(self, color, petals, price):
        if not isinstance(color, str):
            raise ValueError("Color must be a string")
        if not (isinstance(petals, int) and petals >= 0):
            raise ValueError("Petals must be a non-negative integer")
        if not (isinstance(price, int) and price >= 0):
            raise ValueError("Price must be a non-negative integer")
        self.color = color
        self.petals = petals
        self.price = price

class Tulip(Flower):
    """Class Tulip"""

    def __init__(self, petals, price):
        super().__init__('pink', petals, price)

class Rose(Flower):
    """Class Rose"""

    def __init__(self, petals, price):
        super().__init__('red', petals, price)

class Chamomile(Flower):
    """Class Chamomile"""

    def __init__(self, petals, price):
        super().__init__('white', petals, price)

class FlowerSet:
    """Class FlowerSet"""

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower: Flower):
        """Add a flower to the flower list"""
        if not isinstance(flower, Flower):
            raise ValueError("Only objects of type Flower can be added")
        self.flowers.append(flower)

    def total_price(self):
        """Returns total price"""
        return sum(flower.price for flower in self.flowers)

class Bucket:
    def __init__(self):
        self.flower_sets = []

    def add_set(self, flower_set: FlowerSet):
        """Adding set of flowers"""
        if not isinstance(flower_set, FlowerSet):
            raise ValueError("Only objects of type FlowerSet can be added")
        self.flower_sets.append(flower_set)

    def total_price(self):
        """Total price of all flower sets"""
        return sum(flower_set.total_price() for flower_set in self.flower_sets)
