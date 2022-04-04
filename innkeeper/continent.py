from .world import World

class Continent:
    def __init__(self, world: World) -> None:
        self.world = world
        self.name = 'New Continent'
        self.size = 100
        self.population = 0
        self.towns = []
        self.flags = []

    # Serialization
    def toJSON(self):
        return {
            'name': self.name,
            'size': self.size,
            'population': self.population,
            'towns': self.towns,
            'flags': self.flags,
        }

    # Deserialization
    @classmethod
    def fromJSON(cls, world: World, data: dict):
        continent = cls(world)
        continent.name = data['name']
        continent.size = data['size']
        continent.population = data['population']
        continent.towns = data['towns']
        continent.flags = data['flags']
        return continent

    def getKingdoms(self):
        return self.world._kingdoms # TODO: Filter out the kingdoms that are not in this continent