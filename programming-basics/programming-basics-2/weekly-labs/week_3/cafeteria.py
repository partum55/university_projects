"""
Coffee Order & Inventory Management System
"""


RECIPE = {
    "espresso": {'espresso': 30},
    "latte": {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15},
    "macchiato": {'espresso': 60, 'foamed_milk': 15},
    "flat white": {'espresso': 60, 'steamed_milk': 120},
    "dopio": {'espresso': 60},
    "cappuccino": {'espresso': 60, 'steamed_milk': 60, 'foamed_milk': 60},
    "lungo": {'espresso': 90},
    "cortado": {'espresso': 60, 'steamed_milk': 60}
}


class Track:
    """
    Tracks coffee orders, manages inventory, and calculates total revenue.

    :param date: The date for tracking orders.
    :type date: str
    """

    MENU = {"espresso": 40, "latte": 70, "flat white": 70, "dopio": 50,
            "cappuccino": 60, "lungo": 50, "cortado": 55, "mocca": 60}
    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date):
        self.date = date
        self.orders = []

    def place_order(self, order) -> str:
        """
        Places a coffee order if it's available and inventory allows.

        :param order: The coffee order instance.
        :type order: Coffee
        :return: Confirmation message or an error message.
        :rtype: str
        """
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        if not Track.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        if order.name not in Track.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        if self.__beans - (order.espresso // 30 * 6) < 0 or (self.__milk - order.milk) < 0:
            return "Unfortunately, we don't have enough ingredients."

        self.orders.append(order)
        order.price = self.MENU[order.name] * order.count
        order.is_paid = True
        self.__beans -= order.espresso // 30 * 6
        self.__milk -= order.milk
        return "Done!"

    def total_revenue(self) -> int:
        """
        Calculates total revenue from all placed orders.

        :return: Total revenue in currency units.
        :rtype: int
        """
        return sum(i.price for i in self.orders)

    def total_milk(self) -> int:
        """
        Calculates the total milk consumption from all orders.

        :return: Total milk used in milliliters.
        :rtype: int
        """
        return sum(i.milk for i in self.orders)

    def total_beans(self) -> int:
        """
        Calculates the total coffee beans consumption.

        :return: Total coffee beans used in grams.
        :rtype: int
        """
        return sum(order.espresso for order in self.orders) // 30 * 6

    @property
    def beans(self) -> int:
        """
        Gets the remaining coffee beans in stock.

        :return: Remaining coffee beans in grams.
        :rtype: int
        """
        return self.__beans

    @property
    def milk(self) -> int:
        """
        Gets the remaining milk in stock.

        :return: Remaining milk in milliliters.
        :rtype: int
        """
        return self.__milk

    def milk_spoil(self, amount: int) -> None:
        """
        Reduces the milk stock when milk spoils.

        :param amount: The amount of spoiled milk in milliliters.
        :type amount: int
        """
        self.__milk -= amount
        self.__milk = max(0, self.__milk)

    @classmethod
    def set_limit_milk(cls, limit_milk: int):
        """
        Sets a new maximum limit for milk storage.

        :param limit_milk: The new milk limit in milliliters.
        :type limit_milk: int
        """
        cls.__milk = limit_milk

    @classmethod
    def change_air_state(cls):
        """Toggles safety status (Air alert mode)"""
        cls.safety = not cls.safety


class Coffee:
    """
    Represents a standard coffee order.

    :param name: The name of the coffee.
    :type name: str
    :param count: The number of coffee cups ordered.
    :type count: int
    """

    __recipe = {}

    def __init__(self, name, count=1):
        self.name = name
        self.count = count

        if name in Coffee.__recipe:
            self.is_paid = False

    @property
    def milk(self):
        """Temp"""
        return sum(v for k, v in Coffee.__recipe[self.name].items() if k != "espresso") * self.count

    @property
    def espresso(self):
        """Temp"""
        return Coffee.__recipe[self.name]['espresso'] * self.count

    @classmethod
    def set_recipe(cls, recipe: dict):
        """
        Sets the global coffee recipe.

        :param recipe: Dictionary containing coffee recipes.
        :type recipe: dict
        """
        cls.__recipe = recipe

    def __str__(self):
        if not self.__recipe:
            return "Order cannot be created. Recipe has not been set."
        if self.name not in Coffee.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self!r}" is created.'

    def __repr__(self):
        return f"{self.count} {self.name}"

    def __eq__(self, other):
        return isinstance(other, Coffee) and self.name == other.name and self.count == other.count


class FlavorMixin:
    """
    Provides additional flavoring options for coffee.
    """

    def add_flavor(self, sugar: int, cinammon: bool, syrup: str) -> str:
        """
        Adds flavor enhancements to the coffee.

        :param sugar: The number of sugar packets added.
        :type sugar: int
        :param cinammon: Whether cinnamon is added.
        :type cinammon: bool
        :param syrup: The type of syrup added.
        :type syrup: str
        :return: Confirmation message indicating whether flavors were added.
        :rtype: str
        """
        if not self.is_paid:
            return 'Please, pay for it.'

        self.sugar = sugar * self.count
        self.cinammon = cinammon
        self.syrup = syrup
        self.flavor = True
        return 'Done!'


class CustomCoffee(Coffee, FlavorMixin):
    """
    Represents a customizable coffee order with flavor additions.

    :param name: The name of the coffee.
    :type name: str
    :param count: The number of coffee cups ordered.
    :type count: int
    """

    def __init__(self, name, count=1):
        super().__init__(name, count)
        self.flavor = False

    def __str__(self):
        if self.flavor:
            return (f'Your best {self.name} is ready! It has: '
                    f'{f'{self.sugar} stickers of sugar, ' if self.sugar else ''}'
                    f'{'cinammon, ' if self.cinammon else ''}{self.syrup} syrup.')
        return super().__str__()

    def __repr__(self):
        return f"{self.count} custom {self.name}"

    def __eq__(self, other):
        if not hasattr(other, 'flavor') and self.flavor:
            return False
        if not hasattr(other, 'flavor') and not self.flavor:
            return super().__eq__(other)
        return super().__eq__(other) and self.flavor == other.flavor
