from dialog.schema.elements.element import Element

__author__ = 'robdefeo'


class Action(Element):
    _element_name = "action"

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
