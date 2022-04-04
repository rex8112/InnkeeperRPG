from typing import List

from .continent import Continent

class World:
    def __init__(self, name: str) -> None:
        self.name = name
        self._players = [] # TODO: Player Manager Class
        self._characters = [] # TODO: Character Manager Class

        self._continents: List[Continent] = [] # TODO: Continent Manager Class
        self._kingdoms = [] # TODO: Kingdom Manager Class
        self._towns = [] # TODO: Town Manager Class
        

    