from random import choice

from dialog.elements.element import Element
from dialog.process import ProcessRequest
from typing import Iterable


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

    def process(self, process_request: ProcessRequest):
        if self.selection_type == "RANDOM":
            return choice(self.items)
        else:
            raise NotImplemented()
