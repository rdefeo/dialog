from dialog.schema.elements.element import Element
from typing import Iterable

__author__ = 'robdefeo'


class Prompt(Element):
    _element_name = "prompt"

    def __init__(self, selection_type="RANDOM", items=Iterable[str]):
        self.selection_type = selection_type
        self.items = items

    def create(self):
        doc = {}

        if self.selection_type is not None:
            doc["@selectionType"] = self.selection_type

        if self.items is not None:
            doc["item"] = self.items

        return doc