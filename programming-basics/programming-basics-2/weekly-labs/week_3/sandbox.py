from week_3.try_deepseek import *


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
    assert order1.espresso == 120, order1.espresso
    assert order1.milk == 270
    assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
    assert str(order1) == 'Order "2 latte" is created.', str(order1)

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
    assert order1.price == 140, order1.price
    assert order1.is_paid == True
    assert str(order1) == 'Preparing 2 latte...', str(order1)
    assert len(day_track.orders) == 1

    # it is possible that we have a coffee in recipe but
    # don't have in a menu
    order2 = Coffee("macchiato")
    assert str(order2) == 'Order "1 macchiato" is created.'
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}, order2.__dict__
    assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
    assert len(day_track.orders) == 1

    order2 = Coffee("mocca")
    assert str(order2) == "Order cannot be created. We don't have recipe for it.", str(order2)
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
    assert str(order2) == 'Preparing 1 cappuccino...', str(order2)
    assert order2.price == 60

    assert order2.add_flavor(2, True, 'almond') == 'Done!'
    assert order2.sugar == 2 # number of stickers
    assert order2.cinammon == True # just to add some
    assert order2.syrup == 'almond' # type of syrup
    assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'

    # of course we track the orders
    assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]', str(day_track.orders)
    assert day_track.total_revenue() == 200
    assert day_track.total_milk() == 390
    # we need approx 6 grams of coffee beans to prepare
    # one espresso
    assert day_track.total_beans() == 36, day_track.total_beans()
    assert not isinstance(order2, Track)
    # of course we have some reserves of milk and beans
    # but they are limited. At the beginning of the day we usually
    # have 20 litres of milk and 5 kg of beans
    assert Track._Track__beans == 5000
    assert Track._Track__milk == 20000
    assert day_track.beans == 4964, day_track.beans
    assert day_track.milk == 19610

    order3 = Coffee('Irish Coffee', 3)
    # unfortunately we don't have this kind of drinks
    # please let our customer know about it
    assert day_track.orders == [order1, order2]


    order3 = CustomCoffee('latte', 2)
    assert order3 == order1, order3 == order1
    assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
    assert day_track.place_order(order3) == 'Done!'
    assert order3.add_flavor(3, False, 'green banana') == 'Done!'
    assert order3.sugar == 6, order3.sugar
    assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.', str(order3)
    # assert order3 != order1

    # Sometimes we have situation when the milk spoiled
    # in grams
    day_track.milk_spoil(19340)
    assert day_track.milk == 0, day_track.milk
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
    assert str(order6) == 'Order "1 custom lungo" is created.', str(order6)
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() ==  390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78
    print('Done!')


if __name__ == '__main__':
    test_CafeteriaClass()
