"""Temp"""


class Mono:
    """Class Mono"""
    def __init__(self, coefficient, degree):
        if coefficient == 0:
            self.coefficient = 0
            self.degree = 0
        else:
            self.coefficient = coefficient
            self.degree = degree
        self.next = None

    def copy(self):
        """Copy this polynomial"""
        return Mono(self.coefficient, self.degree)

    def __str__(self):
        if self.coefficient == 0:
            return "Mono: 0"
        if self.degree == 0:
            return f"Mono: {self.coefficient}"
        if self.degree == 1:
            if self.coefficient == 1:
                return "Mono: x"
            if self.coefficient == -1:
                return "Mono: -x"
            return f"Mono: {self.coefficient}x"
        return f"Mono: {self.coefficient}x**{self.degree}"

    def __repr__(self):
        return f"Mono(coeff={self.coefficient}, degree={self.degree})"

    def __eq__(self, other):
        if not isinstance(other, Mono):
            return False
        return self.coefficient == other.coefficient and self.degree == other.degree

    def __hash__(self):
        return hash((self.coefficient, self.degree))


class Polynomial:
    """Class Polynomial"""

    def __init__(self, *terms):
        self.head = None
        monolist = []
        for term in terms:
            if isinstance(term, Mono):
                monolist.append(term.copy())
            elif isinstance(term, Polynomial):
                current = term.head
                while current:
                    monolist.append(current.copy())
                    current = current.next
            else:
                raise TypeError("Polynomial accepts only Mono or Polynomial objects")
        if monolist:
            self.head = monolist[0]
            current = self.head
            for m in monolist[1:]:
                current.next = m
                current = m
        else:
            self.head = Mono(0, 0)

    def copy(self):
        """Copy this polynomial"""
        return Polynomial(self)

    def __str__(self):
        parts = []
        current = self.head
        while current:
            if current.coefficient != 0:
                parts.append(str(current)[6:])
            current = current.next
        if not parts:
            parts = ["0"]
        result = parts[0]
        for part in parts[1:]:
            if part.startswith('-'):
                result += part
            else:
                result += '+' + part
        return "Polynomial: " + result

    def __repr__(self):
        parts = []
        current = self.head
        while current:
            parts.append(repr(current))
            current = current.next
        return "Polynomial(" + " -> ".join(parts) + ")"

    @property
    def degree(self):
        """Temp"""
        max_deg = 0
        current = self.head
        while current:
            max_deg = max(max_deg, current.degree)
            current = current.next
        return max_deg

    def sort(self):
        """Temp"""
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        def sort_key(m):
            if m.coefficient == 0:
                return 1, 0
            return 0, -m.degree

        nodes.sort(key=sort_key)
        if nodes:
            self.head = nodes[0]
            current = self.head
            for m in nodes[1:]:
                current.next = m
                current = m
            current.next = None

    def simplify(self):
        """Temp"""
        terms_dict = {}
        current = self.head
        while current:
            terms_dict[current.degree] = terms_dict.get(current.degree, 0) + current.coefficient
            current = current.next
        new_terms = []
        for deg, coeff in terms_dict.items():
            if coeff != 0:
                new_terms.append(Mono(coeff, deg))
        if not new_terms:
            new_terms = [Mono(0, 0)]
        new_terms.sort(key=lambda m: m.degree, reverse=True)
        self.head = new_terms[0]
        current = self.head
        for m in new_terms[1:]:
            current.next = m
            current = m
        current.next = None

    def eval_at(self, x):
        """Temp"""
        total = 0
        current = self.head
        while current:
            total += current.coefficient * (x ** current.degree)
            current = current.next
        return total

    @property
    def derivative(self):
        """Temp"""
        derived = []
        current = self.head
        while current:
            if current.degree > 0:
                new_coeff = current.coefficient * current.degree
                new_deg = current.degree - 1
                if new_coeff != 0:
                    derived.append(Mono(new_coeff, new_deg))
            current = current.next
        if not derived:
            derived = [Mono(0, 0)]
        return Polynomial(*derived)

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        new_terms = []
        current = self.head
        while current:
            new_terms.append(current.copy())
            current = current.next
        current = other.head
        while current:
            new_terms.append(current.copy())
            current = current.next
        result = Polynomial(*new_terms)
        result.simplify()
        return result

    def __neg__(self):
        new_terms = []
        current = self.head
        while current:
            new_terms.append(Mono(-current.coefficient, current.degree))
            current = current.next
        return Polynomial(*new_terms)

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_terms = []
            current = self.head
            while current:
                new_terms.append(Mono(current.coefficient * other, current.degree))
                current = current.next
            return Polynomial(*new_terms)
        if isinstance(other, Polynomial):
            new_terms = []
            current1 = self.head
            while current1:
                current2 = other.head
                while current2:
                    prod_coeff = current1.coefficient * current2.coefficient
                    prod_deg = current1.degree + current2.degree
                    new_terms.append(Mono(prod_coeff, prod_deg))
                    current2 = current2.next
                current1 = current1.next
            result = Polynomial(*new_terms)
            result.simplify()
            return result
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return False
        poly1 = self.copy()
        poly1.simplify()
        poly2 = other.copy()
        poly2.simplify()
        d1 = {}
        current = poly1.head
        while current:
            d1[current.degree] = current.coefficient
            current = current.next
        d2 = {}
        current = poly2.head
        while current:
            d2[current.degree] = current.coefficient
            current = current.next
        return d1 == d2

    def __hash__(self):
        poly = self.copy()
        poly.simplify()
        terms = []
        current = poly.head
        while current:
            terms.append((current.degree, current.coefficient))
            current = current.next
        terms.sort()
        return hash(tuple(terms))

    def __truediv__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        divisor = other.copy()
        divisor.simplify()
        if divisor.head.coefficient == 0 and divisor.head.degree == 0:
            raise ZeroDivisionError("Division by zero polynomial")
        dividend = self.copy()
        dividend.simplify()
        quotient = Polynomial(Mono(0, 0))
        quotient.simplify()
        while (dividend.degree >= divisor.degree and
               not (dividend.head.coefficient == 0 and dividend.head.degree == 0)):
            dividend.sort()
            divisor.sort()
            ld_dividend = dividend.head
            ld_divisor = divisor.head
            factor_coeff = ld_dividend.coefficient / ld_divisor.coefficient
            factor_deg = ld_dividend.degree - ld_divisor.degree
            factor = Polynomial(Mono(factor_coeff, factor_deg))
            quotient = quotient + factor
            subtraction = factor * divisor
            dividend = dividend - subtraction
            dividend.simplify()
        quotient.simplify()
        dividend.simplify()
        return quotient, dividend
