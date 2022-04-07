from typing import List


class Attribute:
    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value

    # Magic methods
    def __str__(self) -> str:
        return f'{self.name}: {self.value}'

    def __repr__(self) -> str:
        return f'Attribute(\'{self.name}\', {self.value})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Attribute):
            return self.name == other.name and self.value == other.value
        return NotImplemented

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Attribute):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, Attribute):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Attribute):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Attribute):
            return self.value >= other.value
        return NotImplemented

    def __add__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value + other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value + other)
        return NotImplemented

    def __iadd__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value += other.value
            return self
        if isinstance(other, (int, float)):
            self.value += other
            return self
        return NotImplemented

    def __sub__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value - other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value - other)
        return NotImplemented

    def __isub__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value -= other.value
            return self
        if isinstance(other, (int, float)):
            self.value -= other
            return self
        return NotImplemented

    def __mul__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value * other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value * other)
        return NotImplemented

    def __imul__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value *= other.value
            return self
        if isinstance(other, (int, float)):
            self.value *= other
            return self
        return NotImplemented

    def __truediv__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value / other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value / other)
        return NotImplemented

    def __itruediv__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value /= other.value
            return self
        if isinstance(other, (int, float)):
            self.value /= other
            return self
        return NotImplemented

    def __floordiv__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value // other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value // other)
        return NotImplemented

    def __ifloordiv__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value //= other.value
            return self
        if isinstance(other, (int, float)):
            self.value //= other
            return self
        return NotImplemented

    def __mod__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value % other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value % other)
        return NotImplemented

    def __imod__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value %= other.value
            return self
        if isinstance(other, (int, float)):
            self.value %= other
            return self
        return NotImplemented

    def __pow__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            return Attribute(self.name, self.value ** other.value)
        if isinstance(other, (int, float)):
            return Attribute(self.name, self.value ** other)
        return NotImplemented

    def __ipow__(self, other) -> 'Attribute':
        if isinstance(other, Attribute):
            self.value **= other.value
            return self
        if isinstance(other, (int, float)):
            self.value **= other
            return self
        return NotImplemented

    def __neg__(self) -> 'Attribute':
        return Attribute(self.name, -self.value)

    def __pos__(self) -> 'Attribute':
        return Attribute(self.name, +self.value)

    def __abs__(self) -> 'Attribute':
        return Attribute(self.name, abs(self.value))

    # Methods
    def to_dict(self) -> dict:
        return {'name': self.name, 'value': self.value}