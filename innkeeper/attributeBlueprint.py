import numpy
import random

from .attribute import Attribute


class AttributeBlueprint:
    def __init__(self, name: str, min: float, max: float, modifier: float, type: str = 'int') -> None:
        self.name = name
        self.max = max
        self.type = type
        self.min = min
        self.modifier = modifier

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'max': self.max,
            'type': self.type,
            'min': self.min,
            'modifier': self.modifier
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'AttributeBlueprint':
        return cls(data['name'], data['min'], data['max'], data['modifier'], data['type'])

    def get_value(self) -> float:
        return self.modifier + self.min

    def set_value(self, value: float) -> None:
        if value > self.max:
            self.modifier = self.max - self.min
        elif value < self.min:
            self.modifier = self.min
        else:
            self.modifier = value - self.min

    def randomize(self) -> None:
        """Randomize the value.
        
        This will generate a list of ten values evenly spaced between the min and max, including both endpoints.
        It will then choose a random value from the list and set the value to that.
        This value will either be an integer or a float depending on the type of the blueprint."""
        steps = 10
        step = (self.max - self.min) / steps - 1
        values = [self.min + step * i for i in range(steps)]
        index = random.randint(0, len(values) - 1)
        new_value = values[index]

        if self.type == 'int':
            new_value = int(numpy.round(new_value))
        elif self.type == 'float':
            new_value = numpy.round(new_value, 2)
        self.set_value(new_value)

    def get_attribute(self) -> Attribute:
        """Get the value as an Attribute."""
        return Attribute(self.name, self.get_value())