from typing import TYPE_CHECKING, List
from .snowflake_generator import SnowflakeGenerator

if TYPE_CHECKING:
    from .continent import Continent
    from .kingdom import Kingdom
    from .town import Town

class World:
    def __init__(self, name: str, worker_id: int) -> None:
        self.name = name
        self.worker_id = worker_id

        self.snowflake = SnowflakeGenerator(worker_id)

        self._players = [] # TODO: Player Manager Class
        self._characters = [] # TODO: Character Manager Class

        self._continents: List[Continent] = [] # TODO: Continent Manager Class
        self._kingdoms: List[Kingdom] = [] # TODO: Kingdom Manager Class
        self._towns: List[Town] = [] # TODO: Town Manager Class
        
    def get_new_id(self) -> int:
        new_id = self.snowflake.get_new_id()
        return new_id