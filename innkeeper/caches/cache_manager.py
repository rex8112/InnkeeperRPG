import datetime
from typing import TYPE_CHECKING, Callable, Iterable, Optional, Tuple

from ..exceptions import NotFoundError

if TYPE_CHECKING:
    from ..world import World


class CacheManager:
    def __init__(self, world: World) -> None:
        self.world = world
        self._cache = {}
        self._cache_time = {}

    # Private Methods

    def _add_to_cache(self, key: str, value: object) -> None:
        self._remove_from_cache(key)
        self._cache[key] = value
        self._cache_time[key] = datetime.datetime.now()

    def _remove_from_cache(self, key: str) -> None:
        try:
            del self._cache[key]
            del self._cache_time[key]
        except KeyError:
            pass

    def _remove_expired_from_cache(self) -> None:
        for key in list(self._cache_time.keys()):
            if datetime.datetime.now() - self._cache_time[key] > datetime.timedelta(hours=1):
                self._remove_from_cache(key)

    async def _fetch_entry(self, key: str) -> Optional[object]:
        """Override this method to fetch from appropriate database table"""
        pass

    # Public Methods

    def get(self, key: str) -> Optional[object]:
        item = self._cache.get(key)
        if item:
            self._cache_time[key] = datetime.datetime.now()
            return item
        return None

    def find(self, func: Callable[[object], bool]) -> Iterable[Tuple[str, object]]:
        """
        Finds all items in cache that match the given function.
        
        Parameters:
            func (Callable): Function that returns True if the item matches the search criteria.

        Yields:
            Tuple[str, object]: Iterable of tuples containing the key and item that match the search criteria.
        """
        for key, obj in self._cache.items():
            if func(obj):
                yield key, obj

    async def fetch(self, key: str, force = True) -> object:
        if key not in self._cache or force:
            value = self._fetch_entry(key)
            if value:
                self._add_to_cache(key, value)
            else:
                raise NotFoundError(f"{key} not found")
        else:
            value = self.get(key)
        return value
