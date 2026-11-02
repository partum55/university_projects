class A:

    def __init__(self):
        self.__x = 3

    def get_x(self):
        return self.__x


class B(A):

    def __init__(self):
        super().__init__()
        self.__x = 4
        self._y = 5


b = B()
