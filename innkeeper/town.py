from .world import World
from .continent import Continent

class Town:
    def __init__(self, world: World, continent: Continent):
        self.id = None
        self.world = world
        self.continent = continent
        self.name = 'New Town'
        self.size = 10
        self.population = 0
        self.owner = None
        self.kingdom = None
        self.flags = []

    @classmethod
    def from_dict(cls, world: World, continent: Continent, data: dict):
        town = cls(world, continent)
        town.name = data['name']
        town.size = data['size']
        town.population = data['population']
        town.owner = data['owner']
        town.kingdom = data['kingdom']
        town.flags = data['flags']
        return town

    def to_dict(self):
        return {
            'name': self.name,
            'size': self.size,
            'population': self.population,
            'owner': self.owner.toJSON() if self.owner else None,
            'kingdom': self.kingdom.toJSON() if self.kingdom else None,
            'flags': self.flags,
        }