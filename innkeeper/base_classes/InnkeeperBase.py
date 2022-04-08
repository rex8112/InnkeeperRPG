from ..world import World

class BaseObject:
    def __init__(self, world: World) -> None:
        self.world = world
        self.id = None