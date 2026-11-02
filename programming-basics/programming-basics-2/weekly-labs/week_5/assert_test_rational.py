from rational import *


def test_rational():
    """Testing class Rational ..."""
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert rational1.numerator == 1
    assert rational1.denominator == 4
    assert isinstance(rational1, Rational)
    assert str(rational1) == "1/4"

    try:
        rational2 = Rational(1, 0)
    except ValueError as e:
        assert f'{e}' == "Denominator cannot be zero."

    rational2 = Rational(2, 4)
    assert rational2.numerator == 2
    assert rational2.denominator == 4
    assert isinstance(rational2, Rational)
    assert str(rational2) == "2/4"
    rational2 = rational2.reduce()
    assert str(rational2) == "1/2"

    # here you can add two numbers
    rational2 = Rational(2, 5)
    assert str(rational1 + rational2) == "13/20", str(rational1 + rational2)

    # here is a substraction
    assert str(rational1 - rational2) == "-3/20"

    # multiplication
    assert str(rational1 * rational2) == "1/10"

    # division
    assert str(rational1 / rational2) == "5/8"

    assert str(rational1 / rational2*rational1-rational1) == "-3/32"

    rational3 = Rational(2, 8)
    assert str(rational3) == "2/8"

    assert rational1 == rational3

    assert rational1 < rational2

    assert rational1 <= rational2

    assert rational1 <= rational3

    rational3 = Rational(2, -8)
    assert str(rational3) == "-2/8"

    rational4 = Rational(10, 8)
    assert str(rational4) == "10/8"
    assert rational4.mixed_form == "1 2/8"

    rational4.mixed_form = '2 3/5'
    assert str(rational4) == '13/5'
    assert isinstance(rational4, Rational)

    rational4.mixed_form = '3/5'
    assert str(rational4) == '3/5'

    rational5 = Rational(0, -4)
    assert str(rational5) == '0/4'
    assert str(rational5.reduce()) == '0/1'

    rational6 = Rational(10, -8)
    assert str(rational6) == "-10/8"
    assert rational6.mixed_form == "-1 2/8"

    rational7 = Rational(-10, 8)
    assert str(rational7) == "-10/8"
    assert rational7.mixed_form == "-1 2/8"

    rational4.mixed_form = "-1 2/8"
    assert str(rational4) == '-10/8'
    assert rational4.numerator == -10
    assert rational4.denominator == 8
    assert isinstance(rational4, Rational)

    rational4.mixed_form = "-1 0/8"
    assert rational4.mixed_form == '0', rational4.mixed_form

    print("Done!")


if __name__ == '__main__':
    test_rational()
