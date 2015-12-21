from dialog.elements.element import Element
from typing import Iterable


class If(Element):
    _element_name = "if"

    def __init__(self, _id=None, match_type="ALL", elements=Iterable[Element]):
        settings = {
            "match_type": match_type
        }
        if _id is not None:
            settings["id"] = _id

        super().__init__(settings, elements)

    def _set_dialog(self, value):
        self.dialog = value
        if self.children is not None:
            for x in self.children:
                x._set_dialog(value)

    def create(self):
        doc = {
            "@matchType": self.settings["match_type"]
        }

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]

        if self.children is not None:
            for index, x in enumerate(self.children):
                doc[(index, x._element_name)] = x

        return doc
