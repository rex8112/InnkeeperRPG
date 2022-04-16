from django.forms.models import model_to_dict
from typing import TYPE_CHECKING, Optional

from .abc import UniqueObject, WorldObject
from .models import Player as PlayerModel

if TYPE_CHECKING:
    from django.contrib.auth.models import User
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


    def __init__(self, world: 'World', user: 'User') -> None:
        self.world = world
        self.name = 'New Player'
        self.entry: Optional[PlayerModel] = None
        self.user = user
        self.characters = {}
        self.settings = {}
        self.flags = []

    # Properties
    
    # Class Methods
    @classmethod
    def from_dict(cls, world: 'World', data: dict) -> 'Player':
        """Create a new player from a dictionary."""
        player = cls(world, data['user'])
        player.settings = data['settings']
        player.flags = data['flags']
        return player

    @classmethod
    def load(cls, world: 'World', user: 'User') -> 'Player':
        """Loads a player from the database based on the given User model instance."""
        entry: Optional[PlayerModel] = PlayerModel.objects.get(user=user)
        if (entry is None):
            return None
        data = model_to_dict(entry)
        player = cls.from_dict(world, data)
        player.entry = entry
        player.user = entry.user
        return player

    # Instance Methods
    def to_dict(self) -> dict:
        return {
            'user': self.user,
            'settings': self.settings,
            'flags': self.flags,
        }

    def save(self) -> None:
        """Saves the player to the database."""
        if (self.user is None):
            raise ValueError('Player must have a user.')
        self.entry = PlayerModel(**self.to_dict())
        self.entry.save()
