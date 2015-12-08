from typing import Iterable


class Element:
    _element_name = None

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
    def __init__(self, items: list = None):
        self.items = items

    def create(self):
        doc = {}

        if self.items is not None:
            doc["item"] = self.items

        return doc


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


class Condition(Element):
    _element_name = "cond"

    def __init__(self, name=None, operator=None, root_text=None):
        self.name = name
        self.operator = operator
        self.root_text = root_text

    def create(self):
        doc = {}

        if self.name is not None:
            doc["@varName"] = self.name

        if self.operator is not None:
            doc["@operator"] = self.operator

        if self.root_text is not None:
            doc["#text"] = self.root_text

        return doc


class If(Element):
    def __init__(self, match_type=None, elements=Iterable[Element]):
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


class Goto(Element):
    _element_name = "goto"

    def __init__(self, ref=None):
        self.ref = ref

    def create(self):
        doc = {}

        if self.ref is not None:
            doc["@ref"] = self.ref

        return doc


class Variable(Element):
    _element_name = "variable"

    def __init__(self, name, _type, description=None, init_value=None):
        self.name = name
        self.type = _type
        self.description = description
        self.init_value = init_value

    def create(self):
        doc = {
            "@name": self.name,
            "@type": self.type
        }
        if self.init_value is not None:
            doc["@initValue"] = self.init_value

        if self.description is not None:
            doc["@description"] = self.description

        return doc
