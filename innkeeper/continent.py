from typing import Dict, List, Union

from .abc import UniqueObject, WorldObject
from .town import Town
from .world import World


class Continent(UniqueObject, WorldObject):
    def __init__(self, world: World, id: int) -> None:
        super.__init__(world)
        self.id = id
        self.name = 'New Continent'
        self.size = 100
        self.population = 0
        self.towns: List[Town] = []
        self.flags = []

    @classmethod
    def from_dict(cls, world: World, data: dict):
        continent = cls(world)
        continent.id = data['id']
        continent.name = data['name']
        continent.size = data['size']
        continent.population = data['population']
        continent.towns = data['towns']
        continent.flags = data['flags']
        return continent

    def to_dict(self) -> Dict[str, Union[str, int, float, None]]:
        return {
            'id': self.id,
            'name': self.name,
            'size': self.size,
            'population': self.population,
            'towns': [town.id for town in self.towns],
            'flags': self.flags,
        }

    def getKingdoms(self):
        return self.world._kingdoms # TODO: Filter out the kingdoms that are not in this continent
