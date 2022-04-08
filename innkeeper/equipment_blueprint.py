from typing import Dict, List

from .attribute_blueprint import AttributeBlueprint
from .base_classes.base_object import BaseObject
from .world import World


class EquipmentBlueprint(BaseObject):
    def __init__(self, world: World):
        super.__init__(world)
        self.name = 'New Equipment Blueprint'
        self.min_level = 1
        self.max_level = 10
        self.min_rarity = 0
        self.max_rarity = 4
        self.main_attributes: List[AttributeBlueprint] = []
        self.rarity_attributes: List[AttributeBlueprint] = []

    @classmethod
    def from_dict(cls, world: World, data: dict):
        blueprint = cls(world)
        blueprint.id = data['id']
        blueprint.name = data['name']
        blueprint.min_level = data['min_level']
        blueprint.max_level = data['max_level']
        blueprint.min_rarity = data['min_rarity']
        blueprint.max_rarity = data['max_rarity']

        for d in data['main_attributes']:
            attributeBlueprint = AttributeBlueprint.from_dict(d)
            blueprint.main_attributes.append(attributeBlueprint)

        for d in data['rarity_attributes']:
            attributeBlueprint = AttributeBlueprint.from_dict(d)
            blueprint.rarity_attributes.append(attributeBlueprint)

        return blueprint

    def to_dict(self):
        return {
            'name': self.name,
            'min_level': self.min_level,
            'max_level': self.max_level,
            'min_rarity': self.min_rarity,
            'max_rarity': self.max_rarity,
            'main_attributes': self.main_attributes,
            'rarity_attributes': self.rarity_attributes,
        }
