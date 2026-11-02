"""Cafeteria"""

RECIPE = {
    "espresso": {
        'espresso': 30},
    "latte": {
        'espresso': 60,
        'steamed_milk': 120,
        'foamed_milk': 15},
    "macchiato": {
        'espresso': 60,
        'foamed_milk': 15},
    "flat white": {
        'espresso': 60,
        'steamed_milk': 120},
    "dopio": {
        'espresso': 60},
    "cappuccino": {
        'espresso': 60,
        'steamed_milk': 60,
        'foamed_milk': 60},
    "lungo": {
        'espresso': 90},
    "cortado": {
        'espresso': 60,
        'steamed_milk': 60}
}


class Track:
    """Track"""
    MENU = {"espresso": 40, "latte": 70, "flat white": 70, "dopio": 50, "cappuccino": 60,
            "lungo": 50, "cortado": 55, "mocca": 60}
    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date: str):
        """
        Constructor
        >>> day = Track('14.01.2020')
        >>> day.date
        '14.01.2020'
        """
        self.date = date
        self.orders: list['Coffee'] = []

    def place_order(self, order: 'Coffee'):
        """
        Place an order
        >>> day = Track('14.01.2020')
        >>> cof = 'Coffee'
        >>> day.place_order(cof)
        "We can't create anything that is not a Coffee instance."
        >>> cof = Coffee('tea')
        >>> day.place_order(cof)
        "Unfortunately, we don't have such kind of coffee in the menu."
        >>> cof = Coffee('latte')
        >>> Coffee.set_recipe(RECIPE)
        >>> day.place_order(cof)
        'Done!'
        >>> day.beans
        4988
        >>> day.milk
        19865
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

    def total_revenue(self):
        """
        Return total revenue
        >>> day = Track('14.01.2020')
        >>> cof = Coffee('latte')
        >>> Coffee.set_recipe(RECIPE)
        >>> day.place_order(cof)
        'Done!'
        >>> day.total_revenue()
        70
        """
        return sum(order.price for order in self.orders)

    def total_milk(self):
        """
        Return total milk
        >>> day = Track('14.01.2020')
        >>> cof = Coffee('latte')
        >>> Coffee.set_recipe(RECIPE)
        >>> day.place_order(cof)
        'Done!'
        >>> day.total_milk()
        135
        """
        return sum(order.milk for order in self.orders)

    def total_beans(self):
        """
        Return total beans
        >>> day = Track('14.01.2020')
        >>> cof = Coffee('latte')
        >>> Coffee.set_recipe(RECIPE)
        >>> day.place_order(cof)
        'Done!'
        >>> day.total_beans()
        12
        """
        return sum(order.espresso for order in self.orders) // 30 * 6

    @property
    def beans(self):
        """
        Get beans stock
        """
        return self.__beans

    @property
    def milk(self):
        """
        Get milk stock
        """
        return self.__milk

    def milk_spoil(self, amount: int):
        """
        Spoil milk
        >>> day = Track('14.01.2020')
        >>> day.milk_spoil(1000)
        >>> day.milk
        19000
        """
        self.__milk -= amount
        self.__milk = max(0, self.__milk)

    @staticmethod
    def set_limit_milk(amount: int):
        """
        Set limit of milk
        >>> day = Track('14.01.2020')
        >>> Track.set_limit_milk(1000)
        >>> day.milk
        1000
        """
        Track.__milk = amount

    @staticmethod
    def change_air_state():
        """
        Change air state
        >>> day = Track('14.01.2020')
        >>> Track.change_air_state()
        >>> Track.safety
        False
        """
        Track.safety = not Track.safety

class Coffee:
    """Coffee"""
    __recipe = {}
    def __init__(self, name: str, count: int = 1):
        """
        Constructor
        >>> cof = Coffee('latte')
        >>> cof.name
        'latte'
        """
        self.name = name
        self.count = count
        if name in Coffee.__recipe:
            self.is_paid = False

    @property
    def milk(self):
        """
        Milk getter
        """
        if ('steamed_milk' in Coffee.__recipe[self.name]
                and 'foamed_milk' in Coffee.__recipe[self.name]):
            return self.count * (Coffee.__recipe[self.name]['steamed_milk']
                                 + Coffee.__recipe[self.name]['foamed_milk'])
        if 'steamed_milk' in Coffee.__recipe[self.name]:
            return self.count * Coffee.__recipe[self.name]['steamed_milk']
        if 'foamed_milk' in Coffee.__recipe[self.name]:
            return self.count * Coffee.__recipe[self.name]['foamed_milk']
        return 0

    @property
    def espresso(self):
        """
        Espresso getter
        """
        return self.count * Coffee.__recipe[self.name]['espresso']

    @classmethod
    def set_recipe(cls, recipe: dict):
        """
        Set recipe
        """
        cls.__recipe = recipe

    def __str__(self):
        """
        String representation
        >>> day = Track('14.01.2020')
        >>> cof = Coffee('latte')
        >>> str(cof)
        'Order cannot be created. Recipe has not been set.'
        >>> Coffee.set_recipe(RECIPE)
        >>> cof = Coffee('latte')
        >>> str(cof)
        'Order "1 latte" is created.'
        >>> day.place_order(cof)
        'Done!'
        >>> str(cof)
        'Preparing 1 latte...'
        """
        if not self.__recipe:
            return "Order cannot be created. Recipe has not been set."
        if self.name not in Coffee.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self!r}" is created.'

    def __repr__(self):
        """
        Representation
        """
        return f'{self.count} {self.name}'

    def __eq__(self, other):
        """
        Comparison
        >>> cof1 = Coffee('latte', 2)
        >>> cof2 = Coffee('latte', 3)
        >>> cof1 == cof2
        False
        """
        return self.name == other.name and self.count == other.count


class FlavorMixin:
    """Mixin class"""
    def add_flavor(self, sugar: int, cinammon: bool, syrup: str):
        """
        Add flavor to drink
        >>> Coffee.set_recipe(RECIPE)
        >>> cof = CustomCoffee('latte')
        >>> cof.add_flavor(0, True, 'almond')
        'Please, pay for it.'
        """
        if not self.is_paid:
            return 'Please, pay for it.'

        self.sugar = sugar * self.count
        self.cinammon = cinammon
        self.syrup = syrup
        self.flavor = True
        return 'Done!'


class CustomCoffee(Coffee, FlavorMixin):
    """Custom coffee"""
    def __init__(self, name: str, count: int = 1):
        """
        Constructor
        >>> cof = CustomCoffee('latte')
        >>> cof.flavor
        False
        """
        super().__init__(name, count)
        self.flavor = False

    def __str__(self):
        """
        String representation
        >>> Coffee.set_recipe(RECIPE)
        >>> cof = CustomCoffee('latte')
        >>> day = Track('14.01.2020')
        >>> day.place_order(cof)
        'Done!'
        >>> cof.add_flavor(3, True, 'almond')
        'Done!'
        >>> str(cof)
        'Your best latte is ready! It has: 3 stickers of sugar, cinammon, almond syrup.'
        """
        if self.flavor:
            return (f'Your best {self.name} is ready! It has: '
                    f'{f'{self.sugar} stickers of sugar, ' if self.sugar else ''}'
                    f'{'cinammon, ' if self.cinammon else ''}{self.syrup} syrup.')
        return super().__str__()

    def __repr__(self):
        """
        Representation
        """
        return f'{self.count} custom {self.name}'

    def __eq__(self, other):
        """
        Comparison
        >>> Coffee.set_recipe(RECIPE)
        >>> cof1 = CustomCoffee('latte')
        >>> cof1.add_flavor(3, True, 'almond')
        'Please, pay for it.'
        >>> cof2 = Coffee('latte')
        >>> cof1 == cof2
        False
        """
        if not hasattr(other, 'flavor') and self.flavor:
            return False
        if not hasattr(other, 'flavor') and not self.flavor:
            return super().__eq__(other)
        return super().__eq__(other) and self.flavor == other.flavor


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
    assert str(order1) == 'Order cannot be created. Recipe has not been set.'
    # We need to set the recipe before creating the instances.
    # print(order1.__dict__)
    assert order1.__dict__ == {'name': 'latte', 'count': 1}
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
        "espresso": 40,
        "latte": 70,
        "flat white": 70,
        "dopio": 50,
        "cappuccino": 60,
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
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
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
    assert order2.sugar == 2  # number of stickers
    assert order2.cinammon == True  # just to add some
    assert order2.syrup == 'almond'  # type of syrup
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
    # print(order3.flavor == order1.flavor if hasattr(order1, 'flavor') else True)
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
    print(str(order6))
    assert str(order6) == 'Order "1 custom lungo" is created.'
    # print(order6.milk)
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() == 390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78
    print('Done!')


if __name__ == '__main__':
    test_CafeteriaClass()