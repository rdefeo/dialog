from dialog.elements.element import Element
from dialog.elements.grammar import Grammar
from typing import Iterable

__author__ = 'robdefeo'


class Concept(Element):
    def __init__(self, id=None, grammars: Iterable[Grammar] = None, grammar: Grammar = None):
        if grammars is not None:
            self.grammars = grammars
        elif grammar is not None:
            self.grammars = [grammar]

        self.id = id

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if any(self.grammars):
            doc["grammar"] = [x.create() for x in self.grammars]

        return doc