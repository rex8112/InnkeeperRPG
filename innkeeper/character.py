from .world import World

class Character:
    def __init__(self, world: World):
        self.world = world
        self.name = 'New Character'
        self.level = 0
        self.attributes = {}
        self.equipment = {}
        self.inventory = {}
        self.location = None
        self.activity = None
        self.currency = {}
        self.flags = []

    # Serialization
    def toJSON(self):
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

    # Deserialization
    @classmethod
    def fromJSON(cls, world: World, data: dict):
        character = cls(world)
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