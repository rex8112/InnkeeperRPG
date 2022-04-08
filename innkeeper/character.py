from .base_classes.InnkeeperBase import BaseObject
from .world import World


class Character(BaseObject):
    def __init__(self, world: World):
        super.__init__(world)
        self.name = 'New Character'
        self.level = 0
        self.attributes = {}
        self.equipment = {}
        self.inventory = {}
        self.location = None
        self.activity = None
        self.currency = {}
        self.flags = []

    @classmethod
    def from_dict(cls, world: World, data: dict):
        character = cls(world)
        character.id = data['id']
        character.name = data['name']
        character.level = data['level']
        character.attributes = data['attributes']
        character.equipment = data['equipment']
        character.inventory = data['inventory']
        character.location = data['location']
        character.activity = data['activity']
        character.currency = data['currency']
        character.flags = data['flags']
        return character

    def to_dict(self):
        return {
            'name': self.name,
            'level': self.level,
            'attributes': self.attributes,
            'equipment': self.equipment,
            'inventory': self.inventory,
            'location': self.location,
            'activity': self.activity,
            'currency': self.currency,
            'flags': self.flags,
        }
