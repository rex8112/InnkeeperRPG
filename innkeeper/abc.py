from abc import ABC, abstractmethod

from .world import World

class UniqueObject(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

class WorldObject(ABC):
    @property
    @abstractmethod
    def world(self) -> World:
        pass