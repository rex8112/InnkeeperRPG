from .enums.item_type import ItemType
from .exceptions import UnstackableError
from .base_classes.InnkeeperBase import BaseObject
from .world import World


class Item(BaseObject):
    def __init__(self, world: World, name: str, quantity: int = 1, type: ItemType = ItemType.MISC):
        super.__init__(world)
        self.name = name
        self.quantity = quantity
        self.type = type
        self.flags = []

    @classmethod
    def from_dict(cls, world: World, data: dict) -> 'Item':
        item = cls(world, data['name'], data['quantity'], data['type'])
        item.id = data['id']
        item.flags = data['flags']
        return item

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'quantity': self.quantity,
            'type': self.type,
            'flags': self.flags,
        }

    def add_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError('Quantity must be greater than 0.')
        if self.type == ItemType.EQUIPMENT or self.flags.count('UNSTACKABLE'):
            raise UnstackableError(f'{self.id}: {self.name} can not be stacked.')
        self.quantity += quantity
