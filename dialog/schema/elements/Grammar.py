from dialog.schema.elements.element import Element



class Grammar(Element):
    def __init__(self, items: list = None):
        self.items = items

    def create(self):
        doc = {}

        if self.items is not None:
            doc["item"] = self.items

        return doc