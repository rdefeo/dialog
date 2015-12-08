from typing import Iterable


class Element:
    def create(self):
        raise NotImplemented()


class Action(Element):
    def __init__(self, varName=None, operator=None, text=None):
        self.varName = varName
        self.operator = operator
        self.text = text

    def create(self):
        doc = {}
        if self.varName is not None:
            doc["@varName"] = self.varName
        if self.operator is not None:
            doc["@operator"] = self.operator
        if self.text is not None:
            doc["#text"] = self.text

        return doc


class Grammar(Element):
    def __init__(self, items: list):
        self.items = items

    def create(self):
        return {
            "item": self.items
        }


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


class Entity(Element):
    def __init__(self, name=None, values: Iterable[Value] = None):
        self.name = name
        self.values = values

    def create(self):
        doc = {}

        if self.name is not None:
            doc["@name"] = self.name

        if any(self.values):
            doc["value"] = [x.create() for x in self.values]

        return doc


class Entities(Element):
    def __init__(self, entities: Iterable[Entity] = None):
        self.entities = entities

    def create(self):
        return {
            "entity": self.entities
        }


class Concept(Element):
    pass
