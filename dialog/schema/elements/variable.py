from dialog.schema.elements.element import Element

__author__ = 'robdefeo'


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