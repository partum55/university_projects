"""Temp"""


class AngleADT:
    """
    Abstract Data Type for calculating camera rotation angles
    when transmitting a message using hexadecimal symbols.
    """

    HEX_DIGITS = "0123456789ABCDEF"
    TOTAL_ANGLES = 16
    BASE_ANGLE = 360.0 / TOTAL_ANGLES

    def __init__(self):
        self.current_angle = 0.0

    def _char_to_hex(self, char: str) -> str:
        """Converts a character to its hexadecimal representation."""
        return format(ord(char), '02X')

    def _hex_to_angle(self, hex_digit: str) -> float:
        """Converts a hexadecimal digit to its corresponding angle."""
        return self.HEX_DIGITS.index(hex_digit) * self.BASE_ANGLE

    def encode_message(self, message: str):
        """
        Encodes a message into a sequence of camera rotation angles.
        :param message: The message as a string.
        :return: A list of relative rotation angles.
        """
        self.current_angle = 0.0
        angles = []
        for char in message:
            hex_repr = self._char_to_hex(char)
            for digit in hex_repr:
                new_angle = self._hex_to_angle(digit)
                relative_angle = new_angle - self.current_angle
                if relative_angle == 0:
                    relative_angle = 360.0
                angles.append(relative_angle)
                self.current_angle = new_angle
        return angles


if __name__ == "__main__":
    a = AngleADT()
    print(a.encode_message("hello"))
    print(a.encode_message("python"))
