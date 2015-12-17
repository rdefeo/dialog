from dialog.schema.elements.element import Element
from typing import Iterable


class If(Element):
    _element_name = "if"

    def __init__(self, match_type="ALL", elements=Iterable[Element]):
        self.match_type = match_type
        self.elements = elements

    def create(self):
        doc = {}

        if self.match_type is not None:
            doc["@matchType"] = self.match_type

        if self.elements is not None:
            for index, x in enumerate(self.elements):
                doc[(index, x._element_name)] = x

        return doc
