"""
Module for managing items and a backpack with a fixed capacity.
Allows adding and removing items while tracking total weight and value.
"""

class Item:
    """Represents an item with a name, weight, and value."""
    def __init__(self, name: str, weight: int, value: int):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.weight} kg, ${self.value})"

    def __repr__(self):
        return f"{self.name}"

class Backpack:
    """Represents a backpack with a fixed capacity that can store items."""
    __capacity = 10

    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        """Adds an item to the backpack if it does not exceed capacity."""
        if not self.is_item_valid(item):
            return "Item is not valid"
        if self.total_weight + item.weight <= self.__capacity:
            self._items.append(item)
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item: Item):
        """Removes an item from the backpack if it exists."""
        if item in self._items:
            self._items.remove(item)
            return "Object succesfully removed."
        return "Item not found in the backpack."

    @property
    def total_value(self):
        """Calculates the total value of items in the backpack."""
        return sum(i.value for i in self._items)

    @property
    def total_weight(self):
        """Calculates the total weight of items in the backpack."""
        return sum(i.weight for i in self._items)

    @property
    def items(self):
        """Temp"""
        return self._items

    @items.setter
    def items(self, items_list):
        """Sets the items in the backpack, ensuring total weight doesn't exceed capacity."""
        valid_items = []
        current_weight = 0
        for item in items_list:
            if isinstance(item, Item) and (current_weight + item.weight) <= self.__capacity:
                valid_items.append(item)
                current_weight += item.weight
        self._items = valid_items

    @items.deleter
    def items(self):
        """Removes all items from the backpack."""
        self._items.clear()

    @classmethod
    def set_capacity(cls, capacity: int):
        """Sets the backpack's capacity and ensures existing backpacks respect it."""
        cls.__capacity = capacity

    @staticmethod
    def is_item_valid(item):
        """Checks if an item is valid (positive weight and non-negative value)."""
        return isinstance(item, Item) and item.weight > 0 and item.value >= 0

    def __str__(self):
        l = len(self._items)
        return (f"Backpack contains {l} {'item' if l <= 1 else 'items'} with total weight "
                f"{self.total_weight} kg and total value ${self.total_value}")
