from typing import TYPE_CHECKING, Optional

from .cache_manager import CacheManager
from ..player import Player

if TYPE_CHECKING:
    from django.contrib.auth.models import User
    from ..world import World


class PlayerCache(CacheManager):
    def __init__(self, world: 'World') -> None:
        super().__init__(world)

    # Public Methods

    def fetch_entry(self, key: 'User') -> Optional[object]:
        player = Player.load(self.world, key)
        return player
