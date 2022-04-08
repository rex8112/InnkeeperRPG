from typing import Optional

from ..exceptions import NotFoundError
from ..world import World

class CacheManager:
    def __init__(self, world: World) -> None:
        self.world = world
        self._cache = {}

    # Private Methods

    def _add_to_cache(self, key: str, value: object) -> None:
        self._cache[key] = value

    async def _fetch_entry(self, key: str) -> Optional[object]:
        """Override this method to fetch from appropriate database table"""
        pass

    # Public Methods

    def get(self, key: str) -> Optional[object]:
        return self._cache.get(key, None)

    async def fetch(self, key: str, force = True) -> object:
        if key not in self._cache:
            value = self._fetch_entry(key)
            if value:
                self._add_to_cache(key, value)
            else:
                raise NotFoundError(f"{key} not found")
        else:
            value = self.get(key)
        return value