"""birds module"""

class Egg:
    """Represents an egg laid by a bird."""


class Bird:
    """A base class for birds that can lay eggs and fly."""

    def __init__(self, name: str):
        """
        Initializes a Bird with a given name.

        :param name: The species name of the bird.
        :type name: str
        """
        self.name = name
        self.eggs = []

    def fly(self) -> str:
        """
        Returns the ability of the bird to fly.

        :return: A message indicating flight capability.
        :rtype: str
        """
        return "I can fly!"

    def count_eggs(self) -> int:
        """
        Returns the number of eggs the bird has laid.

        :return: The number of eggs.
        :rtype: int
        """
        return len(self.eggs)

    def get_eggs(self):
        """
        Returns a copy of the eggs list to prevent external modification.

        :return: A list of Egg objects.
        :rtype: list
        """
        return self.eggs[:]

    def lay_egg(self) -> None:
        """
        Lays an egg and adds it to the bird's eggs list.

        :return: None
        """
        self.eggs.append(Egg())

    def __repr__(self) -> str:
        """
        Returns a string representation of the bird.

        :return: A string stating the bird's name and egg count.
        :rtype: str
        """
        return f"{self.name} has {len(self.eggs)} {'eggs' if len(self.eggs) != 1 else 'egg'}"


class Penguin(Bird):
    """A subclass of Bird that cannot fly but can swim."""

    def fly(self) -> str:
        """
        Penguins cannot fly.

        :return: A message indicating the inability to fly.
        :rtype: str
        """
        return "No flying for me."

    def swim(self) -> str:
        """
        Returns the ability of the penguin to swim.

        :return: A message indicating swimming capability.
        :rtype: str
        """
        return "I can swim!"


class MessengerBird(Bird):
    """A subclass of Bird that can carry messages."""

    def __init__(self, name: str, message: str = ""):
        """
        Initializes a MessengerBird with a name and an optional message.

        :param name: The species name of the bird.
        :type name: str
        :param message: The message the bird carries (default is an empty string).
        :type message: str
        """
        super().__init__(name)
        self.message = message

    def deliver_message(self) -> str:
        """
        Returns the message carried by the MessengerBird.

        :return: The message stored in the bird.
        :rtype: str
        """
        return self.message
