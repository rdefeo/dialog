from dialog.elements.element import Element


class Condition(Element):
    _element_name = "cond"

    def __init__(self, name=None, operator=None, root_text=None):
        self.name = name
        self.operator = operator
        self.root_text = root_text

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}

        if self.name is not None:
            doc["@varName"] = self.name

        if self.operator is not None:
            doc["@operator"] = self.operator

        if self.root_text is not None:
            doc["#text"] = self.root_text

        return doc
