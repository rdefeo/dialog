from dialog.elements.element import Element
from dialog.elements.entity import Entity
from typing import Iterable


class Entities(Element):
    def __init__(self, entities: Iterable[Entity] = None):
        self.entities = entities

    def _set_dialog(self, value):
        pass

    def create(self):
        return {
            "entity": self.entities
        }
