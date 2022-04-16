from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from .snowflake_generator import SnowflakeGenerator

if TYPE_CHECKING:
    from .world import World


class UniqueObject(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def entry(self) -> Optional[object]:
        pass

    @abstractmethod
    async def save(self) -> None:
        pass

    @classmethod
    @abstractmethod
    async def load(cls, world: 'World', id: int) -> 'UniqueObject':
        pass

    @property
    def created_at(self) -> datetime:
        return SnowflakeGenerator.get_datetime_from_id(self.id)

class WorldObject(ABC):
    @property
    @abstractmethod
    def world(self) -> 'World':
        pass
