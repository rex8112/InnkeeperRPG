from abc import ABC, abstractmethod
from datetime import datetime

from .snowflake_generator import SnowflakeGenerator
from .world import World


class UniqueObject(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @abstractmethod
    async def save(self) -> None:
        pass

    @abstractmethod
    @classmethod
    async def load(cls, world: World, id: int) -> 'UniqueObject':
        pass

    @property
    def created_at(self) -> datetime:
        return SnowflakeGenerator.get_datetime_from_id(self.id)

class WorldObject(ABC):
    @property
    @abstractmethod
    def world(self) -> World:
        pass
