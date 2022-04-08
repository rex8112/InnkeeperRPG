from typing import Dict, List, Union

from .base_classes.InnkeeperBase import BaseObject
from .continent import Continent
from .world import World


class Kingdom(BaseObject):
    def __init__(self, world: World) -> None:
        super.__init__(world)
        self.name = 'New Kingdom'
        self.ruler = None
        self.land = {}
        self.population = 0
        self.army = 0
        self.flags = []
        
    @classmethod
    def from_dict(cls, world: World, data: dict):
        kingdom = cls(world)
        kingdom.name = data['name']
        kingdom.ruler = data['ruler']
        kingdom.land = data['land']
        kingdom.population = data['population']
        kingdom.army = data['army']
        kingdom.flags = data['flags']
        return kingdom

    def to_dict(self) -> Dict[str, Union[str, int, List[str], None]]:
        return {
            'name': self.name,
            'ruler': self.ruler.id if self.ruler else None,
            'land': self.land,
            'population': self.population,
            'army': self.army,
            'flags': self.flags,
        }
