"""Temp"""

from itertools import count


class Item:
    """
    Represents an item in an order.

    Attributes:
        name (str): Name of the item.
        price (float): Price of the item.

    >>> item = Item('book', 110)
    >>> str(item)
    'Item: book, Price: 110'
    >>> item.name
    'book'
    >>> item.price
    110
    """

    def __init__(self, name: str, price: float):
        """
        Initialize an Item object.

        :param name: Name of the item.
        :param price: Price of the item.

        >>> item = Item('pen', 10.5)
        >>> item.name
        'pen'
        >>> item.price
        10.5
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        String representation of the item.

        :return: str

        >>> item = Item('notebook', 50)
        >>> str(item)
        'Item: notebook, Price: 50'
        """
        return f"Item: {self.name}, Price: {self.price}"


class Vehicle:
    """
    Represents a delivery vehicle.

    Attributes:
        vehicle_no (int): Unique vehicle number.
        is_available (bool): Availability status of the vehicle.

    >>> vehicle = Vehicle(1)
    >>> vehicle.vehicle_no
    1
    >>> vehicle.is_available
    True
    """

    def __init__(self, vehicle_no: int):
        """
        Initialize a Vehicle object.

        :param vehicle_no: Unique vehicle number.

        >>> vehicle = Vehicle(2)
        >>> vehicle.vehicle_no
        2
        >>> vehicle.is_available
        True
        """
        self.vehicle_no = vehicle_no
        self.is_available = True


class Location:
    """
    Represents a delivery location.

    Attributes:
        city (str): City of the location.
        post_office (int): Post office number.

    >>> location = Location('Lviv', 53)
    >>> location.city
    'Lviv'
    >>> location.post_office
    53
    """

    def __init__(self, city: str, post_office: int):
        """
        Initialize a Location object.

        :param city: City of the location.
        :param post_office: Post office number.

        >>> location = Location('Kyiv', 23)
        >>> location.city
        'Kyiv'
        >>> location.post_office
        23
        """
        self.city = city
        self.post_office = post_office


class Order:
    """
    Represents an order with items, location, and assigned vehicle.

    Attributes:
        order_id (int): Unique order ID.
        user_name (str): Name of the user.
        location (Location): Delivery location.
        items (list[Item]): List of items in the order.
        vehicle (Vehicle or None): Assigned vehicle.

    >>> Order.order_id_generator = count(1)  # Reset the order ID generator for consistent testing
    >>> my_items = [Item('book', 110), Item('chupachups', 44)]
    >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
    >>> my_order.order_id
    1
    >>> my_order.user_name
    'Oleg'
    >>> my_order.location.city
    'Lviv'
    >>> my_order.location.post_office
    53
    >>> my_order.calculate_amount()
    154
    >>> vehicle = Vehicle(1)
    >>> my_order.assign_vehicle(vehicle)
    >>> str(my_order)
    'Your order number is 1.'
    """

    order_id_generator = count(1)

    def __init__(self, user_name: str, city: str, post_office: int, items: list[Item]):
        """
        Initialize an Order object.

        :param user_name: Name of the user.
        :param city: City of the delivery location.
        :param post_office: Post office number.
        :param items: List of items in the order.

        >>> items = [Item('pen', 20), Item('eraser', 5)]
        >>> order = Order('Anna', 'Odesa', 12, items)
        >>> order.order_id
        2
        >>> order.user_name
        'Anna'
        >>> order.location.city
        'Odesa'
        >>> order.location.post_office
        12
        >>> len(order.items)
        2
        """
        self.order_id = next(Order.order_id_generator)
        self.user_name = user_name
        self.location = Location(city, post_office)
        self.items = items
        self.vehicle = None

    def calculate_amount(self) -> float:
        """
        Calculate the total amount for the order.

        :return: float

        >>> items = [Item('book', 100), Item('pen', 20)]
        >>> order = Order('Oleg', 'Kyiv', 10, items)
        >>> order.calculate_amount()
        120
        """
        return sum(item.price for item in self.items)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        """
        Assign a vehicle to the order.

        :param vehicle: Vehicle to assign.

        >>> vehicle = Vehicle(1)
        >>> items = [Item('notebook', 60)]
        >>> order = Order('Ivan', 'Kharkiv', 5, items)
        >>> order.assign_vehicle(vehicle)
        >>> order.vehicle.vehicle_no
        1
        >>> vehicle.is_available
        False
        """
        self.vehicle = vehicle
        vehicle.is_available = False

    def __str__(self):
        """
        String representation of the order.

        :return: str

        >>> items = [Item('apple', 30)]
        >>> order = Order('Maria', 'Poltava', 3, items)
        >>> str(order)
        'There is no available vehicle to deliver an order.'
        >>> vehicle = Vehicle(2)
        >>> order.assign_vehicle(vehicle)
        >>> str(order)
        'Your order number is 3.'
        """
        return f"Your order number is {self.order_id}." if self.vehicle else "There is no available vehicle to deliver an order."


class LogisticSystem:
    """
    Represents the logistics system managing orders and vehicles.

    >>> vehicles = [Vehicle(1), Vehicle(2)]
    >>> logSystem = LogisticSystem(vehicles)
    >>> Order.order_id_generator = count(1)  # Reset the order ID generator for consistent testing
    >>> my_items = [Item('book', 110), Item('chupachups', 44)]
    >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
    >>> logSystem.place_order(my_order)
    'Your order number is 1.'
    >>> logSystem.track_order(1)
    'Your order #1 is sent to Lviv. Total price: 154 UAH.'

    >>> my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
    >>> my_order2 = Order('Andrii', 'Odesa', 3, my_items2)
    >>> logSystem.place_order(my_order2)
    'Your order number is 2.'
    >>> logSystem.track_order(2)
    'Your order #2 is sent to Odesa. Total price: 164.33 UAH.'

    >>> my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
    >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    >>> logSystem.place_order(my_order3)
    'There is no available vehicle to deliver an order.'
    >>> logSystem.track_order(3)
    'No such order.'
    """

    def __init__(self, vehicles: list[Vehicle]):
        """
        Initialize the logistics system with a list of vehicles.

        :param vehicles: List of Vehicle objects.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> len(logSystem.vehicles)
        2
        >>> logSystem.orders
        {}
        """
        self.vehicles = vehicles
        self.orders = {}

    def place_order(self, order: Order) -> str:
        """
        Place an order and assign a vehicle if available.

        :param order: Order to place.
        :return: A message indicating the order number or that no vehicles are available.

        >>> vehicles = [Vehicle(1)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> Order.order_id_generator = count(1)  # Reset the order ID generator for consistent testing
        >>> my_items = [Item('book', 100)]
        >>> my_order = Order('Anna', 'Kyiv', 30, my_items)
        >>> logSystem.place_order(my_order)
        'Your order number is 1.'

        >>> my_items2 = [Item('pencil', 10)]
        >>> my_order2 = Order('Ivan', 'Lviv', 20, my_items2)
        >>> logSystem.place_order(my_order2)
        'There is no available vehicle to deliver an order.'
        """
        for vehicle in self.vehicles:
            if vehicle.is_available:
                order.assign_vehicle(vehicle)
                self.orders[order.order_id] = order
                return f"Your order number is {order.order_id}."
        return "There is no available vehicle to deliver an order."

    def track_order(self, order_id: int) -> str:
        """
        Track the status of an order by its ID.

        :param order_id: Order ID to track.
        :return: A message with the order details or an error if no such order exists.

        >>> vehicles = [Vehicle(1)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> Order.order_id_generator = count(1)  # Reset the order ID generator for consistent testing
        >>> my_items = [Item('book', 100)]
        >>> my_order = Order('Anna', 'Kyiv', 30, my_items)
        >>> logSystem.place_order(my_order)
        'Your order number is 1.'
        >>> logSystem.track_order(1)
        'Your order #1 is sent to Kyiv. Total price: 100 UAH.'

        >>> logSystem.track_order(2)
        'No such order.'
        """
        order = self.orders.get(order_id)
        if order:
            return (f"Your order #{order_id} is sent to {order.location.city}. "
                    f"Total price: {order.calculate_amount()} UAH.")
        return "No such order."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
