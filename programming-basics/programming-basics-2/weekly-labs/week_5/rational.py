"""
Module for Rational number arithmetic.
"""

import math

class Rational:
    """A class representing a rational number."""
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: "Rational") -> "Rational":
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        g = math.gcd(new_num, new_den)
        return Rational(new_num // g, new_den // g)

    def __sub__(self, other: "Rational") -> "Rational":
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        g = math.gcd(new_num, new_den)
        return Rational(new_num // g, new_den // g)

    def __mul__(self, other: "Rational") -> "Rational":
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        g = math.gcd(new_num, new_den)
        return Rational(new_num // g, new_den // g)

    def __truediv__(self, other: "Rational") -> "Rational":
        if other.numerator == 0:
            raise ValueError("Denominator cannot be zero.")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        g = math.gcd(new_num, new_den)
        return Rational(new_num // g, new_den // g)

    def reduce(self) -> "Rational":
        """
        type param: None
        return: Rational, a new Rational object in reduced form.
        """
        g = math.gcd(self.numerator, self.denominator)
        return Rational(self.numerator // g, self.denominator // g)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other: "Rational") -> bool:
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other: "Rational") -> bool:
        return self < other or self == other

    @property
    def mixed_form(self) -> str:
        """
        type param: None
        return: str, the mixed number representation.
        """
        if self.numerator == 0:
            return "0"
        if abs(self.numerator) < self.denominator:
            return str(self)
        whole = abs(self.numerator) // self.denominator
        remainder = abs(self.numerator) % self.denominator
        sign = "-" if self.numerator < 0 else ""
        if remainder == 0:
            return f"{sign}{whole}"
        return f"{sign}{whole} {remainder}/{self.denominator}"

    @mixed_form.setter
    def mixed_form(self, value: str) -> None:
        try:
            value = value.strip()
            if " " in value:
                parts = value.split()
                if len(parts) != 2:
                    raise ValueError("Invalid mixed fraction format.")
                whole_part, fraction_part = parts
                whole = int(whole_part)
                num, den = map(int, fraction_part.split("/"))
                if den == 0:
                    raise ValueError("Denominator cannot be zero.")
                if num < 0 or num >= den:
                    raise ValueError(
                        "Invalid mixed fraction: fractional part must be a proper fraction."
                    )
                new_num = abs(whole) * den + num
                if whole < 0:
                    new_num = -new_num
                new_den = den
            else:
                num, den = map(int, value.split("/"))
                if den == 0:
                    raise ValueError("Denominator cannot be zero.")
                new_num, new_den = num, den
            if new_den < 0:
                new_num, new_den = -new_num, -new_den
            self.numerator, self.denominator = new_num, new_den
        except ValueError as exc:
            raise ValueError(f"Invalid input for mixed fraction: {value}. Error: {exc}") from exc
