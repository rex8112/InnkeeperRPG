from .abc import UniqueObject, WorldObject
from .world import World


class Player(UniqueObject, WorldObject):
    def __init__(self, world: World, id: int):
        self.id = id
        self.name = 'New Player'
        self.characters = {}
        self.settings = {}
        self.flags = []

    @classmethod
    def from_dict(cls, world: World, data: dict):
        player = cls(world)
        player.id = data['id']
        player.name = data['name']
        player.settings = data['settings']
        player.flags = data['flags']
        return player

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'settings': self.settings,
            'flags': self.flags,
        }