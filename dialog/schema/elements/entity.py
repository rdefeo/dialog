from dialog.schema.elements.value import Value
from dialog.schema.elements.element import Element
from typing import Iterable

__author__ = 'robdefeo'


class Entity(Element):
    def __init__(self, name=None, values: Iterable[Value] = None):
        self.name = name
        self.values = values

    def create(self):
        doc = {}

        if self.name is not None:
            doc["@name"] = self.name

        if any(self.values):
            doc["value"] = self.values

        return doc