from typing import Dict, List, Union
from .world import World
from .continent import Continent

class Kingdom:
    def __init__(self, world: World) -> None:
        self.id = None
        self.world = world
        self.name = 'New Kingdom'
        self.ruler = None
        self.land = {}
        self.population = 0
        self.army = 0
        self.flags = []

    def to_dict(self) -> Dict[str, Union[str, int, List[str], None]]:
        return {
            'name': self.name,
            'ruler': self.ruler.id if self.ruler else None,
            'land': self.land,
            'population': self.population,
            'army': self.army,
            'flags': self.flags,
        }
        
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