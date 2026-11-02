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


class Coffee:
    __recipe = {}

    def __init__(self, name, count=1):
        self.name = name
        self.count = count
        if name in Coffee.__recipe:
            self.is_paid = False

    @classmethod
    def set_recipe(cls, recipe):
        cls.__recipe = recipe

    def __str__(self):
        if not Coffee.__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in Coffee.__recipe:
            return 'Order cannot be created. We don\'t have recipe for it.'
        if not self.is_paid:
            return f'Order "{self.count} {self.name}" is created.'
        else:
            return f'Preparing {self.count} {self.name}...'

    def __repr__(self):
        return f"{self.count} {self.name}"

    @property
    def espresso(self):
        if not (Coffee.__recipe and self.name in Coffee.__recipe):
            return 0
        return self.__recipe[self.name].get('espresso', 0) * self.count

    @property
    def milk(self):
        if not (Coffee.__recipe and self.name in Coffee.__recipe):
            return 0
        milk_components = ['steamed_milk', 'foamed_milk']
        return sum(self.__recipe[self.name].get(key, 0) for key in milk_components) * self.count

    def __eq__(self, other):
        if not isinstance(other, Coffee):
            return False
        return self.name == other.name and self.count == other.count and self.is_paid == other.is_paid


class FlavorMixin:
    def add_flavor(self, sugar, cinnamon, syrup):
        if not self.is_paid:
            return 'Please, pay for it.'
        self.sugar = sugar
        self.cinnamon = cinnamon
        self.syrup = syrup
        self.flavor = True
        return 'Done!'


class CustomCoffee(Coffee, FlavorMixin):
    def __init__(self, name, count=1):
        super().__init__(name, count)
        self.flavor = False

    def __str__(self):
        if not self.is_paid:
            return super().__str__()
        parts = []
        if hasattr(self, 'sugar') and self.sugar > 0:
            parts.append(f'{self.sugar} stickers of sugar')
        if hasattr(self, 'cinnamon') and self.cinnamon:
            parts.append('cinammon')
        if hasattr(self, 'syrup') and self.syrup:
            parts.append(f'{self.syrup} syrup')
        flavor_str = ', '.join(parts)
        return f'Your best {self.name} is ready! It has: {flavor_str}.'

    def __repr__(self):
        return f"{self.count} custom {self.name}"


class Track:
    MENU = {
        "espresso": 40,
        "latte": 70,
        "flat white": 70,
        "dopio": 50,
        "cappuccino": 60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }

    __beans = 5000  # in grams
    __milk = 20000  # in milliliters
    safety = True  # class-level attribute for air state

    def __init__(self, date):
        self.date = date
        self.orders = []

    def place_order(self, order):
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        # if not (order.__recipe and order.name in order.__recipe):
        #     return "Order cannot be created. Recipe has not been set."
        if not Track.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        if order.name not in self.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        required_beans = order.espresso * 0.2
        required_milk = order.milk
        if required_beans > Track.__beans or required_milk > Track.__milk:
            return "Unfortunately, we don't have enough ingredients."
        Track.__beans -= required_beans
        Track.__milk -= required_milk
        order.price = order.count * self.MENU[order.name]
        order.is_paid = True
        self.orders.append(order)
        return 'Done!'

    def total_revenue(self):
        return sum(order.price for order in self.orders)

    def total_milk(self):
        return sum(order.milk for order in self.orders)

    def total_beans(self):
        return int(sum(order.espresso * 0.2 for order in self.orders))

    @classmethod
    def set_limit_milk(cls, limit):
        cls.__milk = limit

    @classmethod
    def change_air_state(cls):
        cls.safety = not cls.safety

    def milk_spoil(self, amount):
        Track.__milk = max(0, Track.__milk - amount)

    @property
    def beans(self):
        return Track.__beans

    @property
    def milk(self):
        return Track.__milk
