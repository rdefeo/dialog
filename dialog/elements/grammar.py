from dialog.elements.element import Element


class Grammar(Element):
    _element_name = "grammar"

    def __init__(self, items: list = None):
        self.items = items

    def create(self):
        doc = {}

        if self.items is not None:
            doc["item"] = self.items

        return doc
