"""Temp"""

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
    """Represents a coffee order."""
    _recipe = None

    def __init__(self, name: str, count=1):
        self.name = name
        self.count = count
        if not Coffee._recipe or name not in Coffee._recipe:
            return
        self.is_valid = True
        self.is_paid = False
        self.espresso = Coffee._recipe[name]["espresso"] * count
        self.milk = sum(v for k, v in Coffee._recipe[name].items() if k != "espresso") * count

    @classmethod
    def set_recipe(cls, recipe):
        cls._recipe = recipe

    def __str__(self):
        if not self.is_valid:
            return f'Order cannot be created. Recipe has not been set.'
        return f'Order "{self.count} {self.name}" is created.' if not self.is_paid else f'Preparing {self.count} {self.name}...'


class FlavorMixin:
    """Mixin for flavored coffee."""

    def __init__(self):
        self.syrup = None
        self.cinnamon = None
        self.sugar = 0

    def add_flavor(self, sugar=0, cinnamon=False, syrup=None):
        if not getattr(self, 'is_paid', False):
            return "Please, pay for it."
        self.sugar += sugar
        self.cinnamon = cinnamon
        self.syrup = syrup
        return "Done!"


class CustomCoffee(Coffee, FlavorMixin):
    """Custom coffee that allows additional flavors."""

    def __init__(self, name: str, count=1):
        super().__init__(name, count)
        FlavorMixin.__init__(self)
        self.flavor = False

    def __str__(self):
        if self.sugar or self.cinnamon or self.syrup:
            additions = []
            if self.sugar:
                additions.append(f"{self.sugar} packets of sugar")
            if self.cinnamon:
                additions.append("cinnamon")
            if self.syrup:
                additions.append(f"{self.syrup} syrup")
            return f'Your best {self.name} is ready! It has: {', '.join(additions)}.'
        return super().__str__()


class Track:
    """Tracks orders and manages inventory."""
    MENU = {
        "espresso": 40, "latte": 70, "flat white": 70, "dopio": 50,
        "cappuccino": 60, "lungo": 50, "cortado": 55, "mocca": 60,
    }
    _beans = 5000
    _milk = 20000
    safety = True

    def __init__(self, date):
        self.date = date
        self.orders = []
        self.beans = Track._beans
        self.milk = Track._milk

    def place_order(self, order):
        if not isinstance(order, Coffee) or not order.is_valid:
            return "Invalid order."
        if not Track.safety:
            return "Unfortunately, it is not safe to make coffee now."
        if order.name not in Track.MENU:
            return "Unfortunately, we don't have this coffee in the menu."
        if self.milk < order.milk or self.beans < (order.espresso // 6):
            return "Unfortunately, we don't have enough ingredients."

        order.is_paid = True
        self.milk -= order.milk
        self.beans -= (order.espresso // 6)
        order.price = Track.MENU[order.name] * order.count
        self.orders.append(order)
        return "Done!"

    def total_revenue(self):
        return sum(order.price for order in self.orders)

    def total_milk(self):
        return sum(order.milk for order in self.orders)

    def total_beans(self):
        return sum(order.espresso // 6 for order in self.orders)

    def milk_spoil(self, amount):
        self.milk = max(0, self.milk - amount)

    @classmethod
    def set_limit_milk(cls, amount):
        cls._milk = amount

    @classmethod
    def change_air_state(cls):
        cls.safety = not cls.safety


def test_CafeteriaClass():
    """
    Print Done if all tests passed
    """
    print("Testing Cafeteria class...")
    # We track the orders during the day
    day_track = Track('07.02.2024')
    day_track.date = '07.02.2024'
    # Our cafeteria has a lot of different beverages in the menu and
    # all of them are connected to coffee.
    # The cafeteria use classical RECIPE that provided as a
    # constant.
    order1 = Coffee('latte')
    assert str(order1) == 'Order cannot be created. Recipe has not been set.', str(order1)
    # We need to set the recipe before creating the instances.
    assert order1.__dict__ == {'name': 'latte', 'count': 1}, order1.__dict__
    Coffee.set_recipe(RECIPE)
    # A client can order only some kind of coffee.
    order1 = Coffee('latte', 2)
    assert order1.name == 'latte'
    assert order1.count == 2
    # also when the client ask for some order the is_paid attribute is
    # created and it is False from the start.
    assert order1.is_paid is False
    # Coffee have three main ingredients that provide variety of the drinks:
    # espresso, steamed milk and foamed milk. But on the side of the client we
    # provide only name of the drink and total amount of espresso
    # and milk in ml.
    assert order1.espresso == 120
    assert order1.milk == 270
    assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
    assert str(order1) == 'Order "2 latte" is created.'

    # now we are ready to place this order
    assert Track.MENU == {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    assert day_track.place_order(order1) == 'Done!'
    assert order1.price == 140
    assert order1.is_paid == True
    assert str(order1) == 'Preparing 2 latte...'
    assert len(day_track.orders) == 1

    # it is possible that we have a coffee in recipe but
    # don't have in a menu
    order2 = Coffee("macchiato")
    assert str(order2) == 'Order "1 macchiato" is created.'
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}, order2.__dict__
    assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
    assert len(day_track.orders) == 1

    order2 = Coffee("mocca")
    assert str(order2) == "Order cannot be created. We don't have recipe for it."
    assert order2.__dict__ == {'name': 'mocca', 'count': 1}
    # Each customer can ask for adding sugar, cinammon or syrup
    # thus creating custom coffee.
    order2 = CustomCoffee('cappuccino')
    assert isinstance(order2, CustomCoffee)
    assert isinstance(order2, Coffee)
    assert isinstance(order2, FlavorMixin)
    assert not isinstance(order1, CustomCoffee)
    assert not isinstance(order1, FlavorMixin)

    assert order2.name == 'cappuccino'
    assert order2.count == 1
    assert order2.espresso == 60
    assert order2.milk == 120
    assert order2.flavor == False

    assert day_track.place_order(order2) == 'Done!'
    assert len(day_track.orders) == 2
    assert str(order2) == 'Preparing 1 cappuccino...'
    assert order2.price == 60

    assert order2.add_flavor(2, True, 'almond') == 'Done!'
    assert order2.sugar == 2 # number of stickers
    assert order2.cinammon == True # just to add some
    assert order2.syrup == 'almond' # type of syrup
    assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'

    # of course we track the orders
    assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
    assert day_track.total_revenue() == 200
    assert day_track.total_milk() == 390
    # we need approx 6 grams of coffee beans to prepare
    # one espresso
    assert day_track.total_beans() == 36
    assert not isinstance(order2, Track)
    # of course we have some reserves of milk and beans
    # but they are limited. At the beginning of the day we usually
    # have 20 litres of milk and 5 kg of beans
    assert Track._Track__beans == 5000
    assert Track._Track__milk == 20000
    assert day_track.beans == 4964
    assert day_track.milk == 19610

    order3 = Coffee('Irish Coffee', 3)
    # unfortunately we don't have this kind of drinks
    # please let our customer know about it
    assert day_track.orders == [order1, order2]


    order3 = CustomCoffee('latte', 2)
    assert order3 == order1
    assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
    assert day_track.place_order(order3) == 'Done!'
    assert order3.add_flavor(3, False, 'green banana') == 'Done!'
    assert order3.sugar == 6
    assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
    assert order3 != order1

    # Sometimes we have situation when the milk spoiled
    # in grams
    day_track.milk_spoil(19340)
    assert day_track.milk == 0
    order4 = Coffee('latte', 2)
    assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
    assert len(day_track.orders) == 3
    # oneday our founder bought new fridge
    # and we can store more milk
    Track.set_limit_milk(30000)
    assert Track._Track__milk == 30000


    order5 = "Coffee"
    assert not isinstance(order5, CustomCoffee)
    assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."

    # and sure we don't work in air alert time
    Track.change_air_state()
    assert Track.safety == False
    order6 = CustomCoffee('lungo', 2)
    assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
    Track.change_air_state()
    assert Track.safety == True
    order6 = CustomCoffee('lungo')
    assert str(order6) == 'Order "1 custom lungo" is created.'
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() ==  390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78
    print('Done!')


if __name__ == '__main__':
    test_CafeteriaClass()
