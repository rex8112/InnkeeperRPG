from .world import World

class Continent:
    def __init__(self, world: World) -> None:
        self.world = world
        self.name = 'New Continent'
        self.size = 100
        
        self._towns = {}
        self._kingdoms = {}