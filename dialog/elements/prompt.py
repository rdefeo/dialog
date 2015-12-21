from random import choice

from dialog.elements.element import Element
from dialog.process import ProcessRequest
from typing import Iterable


class Prompt(Element):
    _element_name = "prompt"

    def __init__(self, selection_type="RANDOM", items=Iterable[str]):
        settings = {
            "selection_type": selection_type
        }
        super().__init__(settings, [])
        self.items = items

    def create(self):
        doc = {}

        if "selection_type" in self.settings:
            doc["@selectionType"] = self.settings["selection_type"]

        if self.items is not None:
            doc["item"] = self.items

        return doc

    @property
    def selection_type(self):
        return self.settings["selection_type"]

    # def process(self, process_request: ProcessRequest):
    #     if self.settings["selection_type"] == "RANDOM":
    #         return choice(self.items)
    #     else:
    #         raise NotImplemented()
