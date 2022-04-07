from typing import Dict, List
from .world import World
from .attribute import Attribute
from .attributeBlueprint import AttributeBlueprint

class Equipment:
    def __init__(self, world: World):
        self.world = world
        self.name = 'New Equipment'
        self.blueprint = None
        self.level = 0
        self.attributes: Dict[str, Attribute] = {}
        self.attributeBlueprints: List[AttributeBlueprint] = []
        self.slot = 'none'
        self.flags = []

    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'blueprint': self.blueprint.id if self.blueprint else None,
            'level': self.level,
            'attributes': self.attributeBlueprints,
            'slot': self.slot,
            'flags': self.flags,
        }

    @classmethod
    def from_dict(cls, world: World, data: dict) -> 'Equipment':
        equipment = cls(world)
        equipment.name = data['name']
        equipment.blueprint = data['blueprint']
        equipment.level = data['level']
        equipment.slot = data['slot']
        equipment.flags = data['flags']

        # Load the attribute blueprints
        for d in data['attributes']:
            attributeBlueprint = AttributeBlueprint.from_dict(d)
            equipment.attributeBlueprints.append(attributeBlueprint)

        equipment.load_attributes()
        return equipment

    def load_attributes(self):
        """Load the attributes from the blueprint."""
        self.attributes.clear()
        for blueprint in self.attributeBlueprints.values():
            attribute = blueprint.get_attribute()
            if self.attributes.get(attribute.name):
                self.attributes[attribute.name] += attribute
            else:
                self.attributes[attribute.name] = attribute