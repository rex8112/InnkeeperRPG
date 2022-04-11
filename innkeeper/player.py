from django.forms.models import model_to_dict
from typing import Optional

from .abc import UniqueObject, WorldObject
from .models import Player as PlayerModel
from .world import World


class Player(UniqueObject, WorldObject):
    __slots__ = (
        'world',
        'id',
        'name',
        'entry',
        'characters',
        'settings',
        'flags',
    )


    def __init__(self, world: World, id: int) -> None:
        self.world = world
        self.id = id
        self.name = 'New Player'
        self.entry: Optional[PlayerModel] = None
        self.characters = {}
        self.settings = {}
        self.flags = []

    # Properties
    
    # Class Methods
    @classmethod
    def from_dict(cls, world: World, data: dict) -> 'Player':
        """Create a new player from a dictionary."""
        player = cls(world, data['id'])
        player.name = data['name']
        player.settings = data['settings']
        player.flags = data['flags']
        return player

    @classmethod
    def load(cls, world: World, id: int) -> 'Player':
        """Loads a player from the database based on the given id."""
        entry: Optional[PlayerModel] = PlayerModel.objects.get(id=id)
        if (entry is None):
            return None
        data = model_to_dict(entry)
        player = cls.from_dict(world, data)
        player.entry = entry
        return player

    # Instance Methods
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'settings': self.settings,
            'flags': self.flags,
        }

    def save(self) -> None:
        self.entry = PlayerModel(**self.to_dict())
        self.entry.save()
