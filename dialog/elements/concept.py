from dialog.elements.element import Element
from dialog.elements.grammar import Grammar
from typing import Iterable

__author__ = 'robdefeo'


class Concept(Element):
    _element_name = "concept"

    def __init__(self, _id=None, grammars: Iterable[Grammar] = None, grammar: Grammar = None):
        if grammars is not None:
            self.grammars = grammars
        elif grammar is not None:
            self.grammars = [grammar]

        self.id = _id

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if any(self.grammars):
            doc["grammar"] = [x.create() for x in self.grammars]

        return doc