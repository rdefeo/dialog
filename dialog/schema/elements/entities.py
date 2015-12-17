from dialog.schema.elements.element import Element
from dialog.schema.elements.entity import Entity
from typing import Iterable

__author__ = 'robdefeo'


class Entities(Element):
    def __init__(self, entities: Iterable[Entity] = None):
        self.entities = entities

    def create(self):
        return {
            "entity": self.entities
        }