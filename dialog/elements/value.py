from dialog.elements.element import Element
from dialog.elements.grammar import Grammar


class Value(Element):
    def __init__(self, name=None, value=None, grammar: Grammar = None):
        self.name = name
        self.value = value
        self.grammar = grammar

    def create(self):
        doc = {}
        if self.name is not None:
            doc["@name"] = self.name

        if self.value is not None:
            doc["@value"] = self.value

        if self.grammar is not None:
            doc["grammar"] = self.grammar.create()

        return doc